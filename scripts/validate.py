#!/usr/bin/env python3
"""Validate catalog IDs, generated files, citations and local Markdown links."""
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main():
    catalog = json.loads((ROOT / 'data/resources.json').read_text())
    resources = catalog['resources']
    ids = [r['id'] for r in resources]
    errors = []
    if len(ids) != len(set(ids)):
        errors.append('Duplicate resource IDs')
    for r in resources:
        if not re.fullmatch(r'[a-z0-9-]+', r['id']):
            errors.append(f'Invalid ID: {r["id"]}')
        for lang in ('en', 'zh'):
            if not r['description'][lang].strip():
                errors.append(f'Missing description: {r["id"]}/{lang}')
        for url in r['links'].values():
            if urlsplit(url).scheme not in ('https', 'http') or not urlsplit(url).netloc:
                errors.append(f'Invalid URL: {url}')
    bib = (ROOT / 'papers.bib').read_text()
    keys = re.findall(r'@\w+\{([^,]+),', bib)
    expected = {r['id'] for r in resources if 'Paper' in r['links']}
    if set(keys) != expected or len(keys) != len(set(keys)):
        errors.append(f'Citation keys mismatch: {set(keys) ^ expected}')
    for path in ROOT.rglob('*.md'):
        content = path.read_text()
        anchors = re.findall(r'<a id="([^"]+)"', content)
        if len(anchors) != len(set(anchors)):
            errors.append(f'Duplicate anchors in {path.name}')
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', content):
            if urlsplit(target).scheme:
                continue
            rel, _, anchor = target.partition('#')
            local = (path.parent / unquote(rel)).resolve() if rel else path
            if not local.is_file():
                errors.append(f'{path.relative_to(ROOT)}: missing {target}')
            elif anchor and f'id="{anchor}"' not in local.read_text():
                errors.append(f'{path.relative_to(ROOT)}: unresolved anchor {target}')
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/render.py'), '--check'])
    if result.returncode:
        errors.append('Generated files are stale')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Validated {len(resources)} resources, {len(keys)} citations and all local Markdown links.')


if __name__ == '__main__':
    main()
