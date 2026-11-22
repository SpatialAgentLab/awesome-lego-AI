#!/usr/bin/env python3
"""Record HTTP HEAD observations. Requires curl; does not download datasets."""
import concurrent.futures
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def check(url):
    result = subprocess.run(
        ['curl', '-sS', '-I', '-L', '--max-time', '20', '--connect-timeout', '7',
         '--max-redirs', '8', '-o', '/dev/null', '-w', '%{http_code}\n%{url_effective}', url],
        capture_output=True, text=True,
    )
    lines = result.stdout.splitlines()
    return {
        'url': url,
        'http_status': int(lines[0]) if lines and lines[0].isdigit() else 0,
        'effective_url': lines[1] if len(lines) > 1 else url,
        'curl_exit': result.returncode,
        'error': result.stderr.strip(),
    }


def main():
    catalog = json.loads((ROOT / 'data/resources.json').read_text())
    urls = sorted({u for r in catalog['resources'] for u in r['links'].values()})
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(check, urls))
    report = {
        'checked_at': datetime.now(timezone.utc).isoformat(),
        'method': 'curl HEAD with redirects; no dataset downloads',
        'interpretation': 'A 2xx status does not prove content, video playback, artifact completeness or reuse rights. 403/429/timeouts may reflect bot protection rather than dead links.',
        'results': results,
    }
    (ROOT / 'data/link-check.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    issues = [r for r in results if r['curl_exit'] or not 200 <= r['http_status'] < 300]
    print(f'Checked {len(urls)} unique URLs; {len(issues)} need interpretation or follow-up.')
    for r in issues:
        print(r['http_status'], r['url'], r['error'][:100])


if __name__ == '__main__':
    main()
