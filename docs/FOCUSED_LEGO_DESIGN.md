# Research Guide to Functional LEGO Design Agents

[简体中文](FOCUSED_LEGO_DESIGN.zh-CN.md) · [Full resource list](../README.md)
Sources checked: **2026-11-23** · 20 selected resources and 1 watchlist item

**Research question: Can AI use design software to build LEGO part systems that meet functional requirements, and verify that they can be assembled and work as intended?**

For example, give an AI a box of Technic parts and ask: “For every three input revolutions, the output must turn once in the opposite direction, within this size limit.” It must choose gears, position shafts, add supports, inspect and repair the design, then deliver a model, assembly steps and functional test results. Here, an agent means an AI that repeatedly uses tools, reads feedback and revises its work.

This guide focuses on **LEGO, especially Technic gears, axles, beams, pins and linkages**. Functions should be measurable: rotation direction, speed ratio, lifting distance or endpoint trajectory. Appearance-only generation, general CAD and furniture assembly are outside the main scope.

Start with six resources: [Nova](#nova) for building with tools, [Mecha](#mecha) for understanding motion, [BrickWright](#brickwright) for feedback-driven repair, [BrickBench](#brickbench) for agent evaluation, [ComputeTechnic](#computetechnic) for prior Technic design research, and [ReLink](#relink) for designing linkages from desired motion.

Navigation: [Data and benchmarks](#data) · [Agents](#agents) · [Mechanism design](#mechanisms) · [Design software](#editors) · [Verification and measurement](#verification) · [Parts and references](#assets) · [Research starting point](#roadmap)

## What counts as a successful design?

| Level | Plain-language meaning | What it does not establish |
| --- | --- | --- |
| Valid geometry and connections | Parts do not visibly intersect; connection locations and types are correct. | Valid final positions do not establish a path for inserting each part. |
| Assemblability | Parts can be installed in a feasible order, including axles, pins and beams. | Human assembly does not establish feasibility for a particular robot. |
| Correct motion | Output direction, ratio, travel or trajectory matches the requirement. This is kinematics. | An animation does not establish sufficient motor torque or operation under load. |
| Dynamics or hardware validation | Forces, friction, gravity and loads are considered, or the mechanism is physically tested. | One successful example does not establish generalization to other inventories, dimensions or loads. |

Report these outcomes separately. Existing tools cover different parts of this process. The suggested uses below are research recommendations, not claims that a complete pipeline already exists.

<a id="data"></a>
## Data first: what is ready, and what needs preparation?

A **training set** supplies examples to learn from. A **benchmark** provides test tasks and scoring rules. A **generator** creates more examples. An **asset library** supplies parts, models or videos, usually without the functional labels needed here. These are different resources.

| Source | Available material | Research use and limitation |
| --- | --- | --- |
| [BrickBench / BrickAgent](https://github.com/kulits/BrickAgent) | 100 tasks each for Model, Set and Alt-Build: 300 total, with environment and evaluation code. | Start by evaluating LEGO tool use; add separate Technic function tasks and scores. |
| [Nova mechanism examples](https://github.com/anteloc/ldraw-nova/tree/master/examples/mechanism-atlas) | Mechanism references; the repository also includes build plans and scripts. | Derive build–check–repair tasks; this is not a standardized training/test corpus of action trajectories. |
| [Mecha example archives](https://github.com/anteloc/ldraw-mecha/blob/master/examples/README.md) | Drivetrain, steering, engine and suspension models, plans, check records and Blender assets. | Extract motion-understanding tasks; some assets need Git LFS. Examples are not an independent benchmark. |
| [ComputeTechnic cases](https://github.com/xuhaocuhk/ComputeTechnic/tree/main/LEGO_Technic_data) | Project cases, including fan, lifting and robot-arm directories. | Study part and connection representations. Functional labels, valid samples and splits need preparation; directory count is not sample count. |
| [ReLink target curves](https://github.com/ETHZ-EDAC/ReLink/tree/main/assets/curves) | Seven `.npy` curve files, plus mechanism-generation and optimization code in the repository. | Build target-trajectory tasks. More mechanisms require running the generator; do not describe this as a downloaded large training corpus. |
| [TechnicSimulation test fixtures](https://github.com/yoff/LegoTechnicSimulation/blob/main/tests/fixtures/README.md) | Small friction-pin, frictionless-pin, gear and motor models with expected outcomes. | Check whether a validator recognizes connections and motion correctly. These are engineering fixtures, not a large dataset. |
| [LDCad Shadow Library](https://github.com/RolandMelkert/LDCadShadowLibrary) | Snapping and connection-location metadata for some parts. | Reduce manual annotation of connection points; coverage and force parameters remain incomplete. |
| [LDraw OMR](https://library.ldraw.org/omr) | Community-maintained digital models of official sets. | Filter Technic models as source material; add joint, function and test annotations. |
| [Philo motor measurements](https://www.philohome.com/motors/motorcomp.htm) / [BEC part measurements](https://brickexperimentchannel.wordpress.com/2023/11/15/characteristics-of-lego-parts/) | Tables, curves and experimental descriptions for motors or parts. | Inform plausible loads and performance ranges. Prepare the data manually and preserve measurement conditions. |

**Among the resources reviewed, we have not confirmed a unified public dataset covering functional requirements → software actions → failures and revisions → assembly verification → hardware function tests.** This suggests a useful data-building direction, but this search alone cannot establish that no other dataset exists.

Preserve provenance, licenses, part-library versions and mechanism families. Split by original set, mechanism structure or family; recolored models and alternate views of the same mechanism should not leak across training and testing. A code license does not automatically cover upstream models, part libraries or videos.

<a id="agents"></a>
## 1. Agents that build, inspect and revise models

<a id="nova"></a>
### 1. LDraw Nova — a close candidate for a LEGO design assistant

**What it does:** Provides agent-oriented tools for finding real parts, writing build plans, producing LDraw models, rendering and revising them. LDraw is a common LEGO model format; MPD can package multiple submodels.

**How to use it:** Explore a design agent that repairs gear spacing, shaft support or locked-input problems using Technic diagnostics.

**Available:** Code, agent workflows and mechanism examples; AGPL-3.0 code. **Limit:** Passing checks does not prove insertion paths, strength or real-world fit. Inspect the coverage of individual checks.

[Code](https://github.com/anteloc/ldraw-nova) · [Mechanism workflow](https://github.com/anteloc/ldraw-nova/blob/master/docs/agent/guides/mechanisms.md) · [Validation scope](https://github.com/anteloc/ldraw-nova/blob/master/docs/agent/reference/validation.md)

<a id="mecha"></a>
### 2. LDraw Mecha — turning static models into inspectable mechanisms

**What it does:** Infers mechanisms from MPD models, creates motion plans and Blender rigs, and checks ratios, rod lengths, loop closure and sampled poses.

**How to use it:** Study whether an agent understands how an assembly moves and whether revisions preserve the intended motion. Read this and Nova early: their existing capabilities overlap substantially with this research question.

**Available:** Code, tutorial videos, saved cases and check records; AGPL-3.0 code. **Limit:** It is not a complete force-based simulation. Animation does not validate gravity, inertia, friction or loads. Some assets require Git LFS.

[Code and tutorials](https://github.com/anteloc/ldraw-mecha) · [Validation](https://github.com/anteloc/ldraw-mecha/blob/master/docs/validation.md) · [Examples](https://github.com/anteloc/ldraw-mecha/blob/master/examples/README.md)

<a id="brickwright"></a>
### 3. BrickWright / BrickLayer — coding with build-check feedback

**What it does:** A 2026 framework in which agents construct LEGO builds using the BrickLayer Python toolkit and receive feedback on real parts, collisions, floating parts and connectivity.

**How to use it:** Compare design with and without validation feedback, or evaluate BrickLayer as the design interface.

**Available:** Paper, agent code, SDK and LDraw export. **Limit:** Structural validity does not establish gear transmission or load-bearing function. Check Technic part and connection coverage before extending it. Treat SDK and upstream part-data licenses separately.

[Paper](https://arxiv.org/abs/2610.31651) · [Code](https://github.com/AvaLovelace1/brickwright) · [BrickLayer SDK](https://github.com/AvaLovelace1/brickwright/tree/main/packages/bricklayer)

<a id="brickbench"></a>
### 4. BrickBench / BrickAgent — a reusable agent evaluation framework

**What it does:** A 2026 benchmark for text-conditioned LEGO design, with a coding-agent environment for querying, connecting, building, viewing and validating parts.

**How to use it:** Learn how to define repeatable tasks with requirements and inventories, then add functional Technic tasks.

**Available:** Paper, 300 tasks, environment and evaluation code. **Limit:** Collision, inventory, connectivity and stability scores are not mechanical-function scores. Its stability simulation treats connected components as rigid bodies, so it cannot establish internal gear motion.

[Paper](https://arxiv.org/abs/2610.12452) · [Project](https://brickben.ch/) · [Code and tasks](https://github.com/kulits/BrickAgent)

<a id="mechanisms"></a>
## 2. Designing mechanisms from desired motion

<a id="computetechnic"></a>
### 5. Computational LEGO Technic Design — essential prior work

**What it does:** A SIGGRAPH Asia 2019 method that generates Technic structures from sketches and optional motion annotations, considering connections, balance, stress and assembly.

**How to use it:** Study computational representations of beams, pins and axles, and establish what prior functional Technic design already covers.

**Available:** Paper, supplements, demonstration video, code, cases and a separate sketch-interface repository. **Limit:** Its main inputs are sketches and motion annotations, rather than a natural-language software agent. Check code and case licenses individually before reuse.

[Paper, video and supplements](https://xuhaocuhk.github.io/projects/compute_technic/index.html) · [Code](https://github.com/xuhaocuhk/ComputeTechnic) · [Sketch interface](https://github.com/edward1997104/ComputeTechSketchUI)

<a id="relink"></a>
### 6. ReLink — choosing beams and pins to trace a target curve

**What it does:** Submitted in 2025 and revised in 2026, this work generates planar linkages from a fixed inventory, or searches for a mechanism whose endpoint follows a target curve. Parts are abstracted as Technic-like liftarms and pins.

**How to use it:** Build trajectory-matching tasks and compare agents with non-LLM search or optimization baselines.

**Available:** Paper, MIT code, interface, kinematic solver, generation and optimization tools, and seven target curves. **Limit:** Planar abstractions need adaptation for real LEGO thickness, connections and assembly. Matching a path does not validate loads.

[Paper](https://arxiv.org/abs/2506.19657) · [Code and demonstrations](https://github.com/ETHZ-EDAC/ReLink) · [Target curves](https://github.com/ETHZ-EDAC/ReLink/tree/main/assets/curves)

<a id="walkers"></a>
### 7. Make it Walk: Computational Design of LEGO Walkers — success means moving

**What it does:** A 2026 preprint designing LEGO walking mechanisms and control around target gait and appearance, with physical walking demonstrations.

**How to use it:** Study how functional objectives connect mechanism design to measured behavior, beyond visual similarity.

**Available:** Paper; a separate code or dataset download was not confirmed in this review. **Limit:** The method includes 3D-printed non-circular gears. Compare custom-part designs separately if the research requires standard LEGO parts only.

[Paper](https://arxiv.org/abs/2610.29505)

<a id="classic-synthesis"></a>
### 8. Conceptual Synthesis of Mechanisms from Qualitative Specifications of Behaviour — early function-to-LEGO research

**What it does:** A 1992 study that decomposes motion requirements and composes mechanisms in a Technic LEGO setting, including a walking mechanism.

**How to use it:** Understand the relationship between functional descriptions, mechanism composition and geometric constraints. The broad idea of automatically designing LEGO from functional requirements is not new.

**Available:** Author page and paper PDF. **Limit:** Useful methodological and historical context; modern runnable code or a dataset was not confirmed.

[Author page](https://www3.cs.stonybrook.edu/~stoller/synthesis.html) · [Paper PDF](https://www3.cs.stonybrook.edu/~stoller/papers/synthesis-of-mechanisms.pdf)

<a id="editors"></a>
## 3. LEGO software the agent could operate

<a id="ldcad"></a>
### 9. LDCad — a LEGO editor with scripting

**What it does:** A model editor with scripting capabilities for models, submodels, macros and animation.

**How to use it:** Explore an agent editing and inspecting mechanisms through scripts or macros in an actual LEGO design application.

**Available:** Software, API documentation, examples and a gear-animation tutorial. **Limit:** The linked API documentation is for 1.7 Alpha; official platforms are Windows and Linux. Scripted animation is not a physical-validity guarantee. Pin the software version.

[Features](https://www.melkert.net/LDCad/features) · [API](https://www.melkert.net/LDCad/docs/scriptAPI2) · [Examples](https://www.melkert.net/LDCad/docs/scriptExamples) · [Gear-animation video](https://www.youtube.com/watch?v=BezWmMlbejQ)

<a id="studio"></a>
### 10. BrickLink Studio — manual inspection and GUI tasks

**What it does:** LEGO building software with collision and stability checks.

**How to use it:** Inspect generated models manually, or consider it for mouse-and-keyboard agent tasks.

**Available:** Software and official help documentation. **Limit:** The documentation describes collision-check limitations for complex or non-rigid parts and conservative stability checks. These are not final mechanical-function judgments. A general, officially supported automation API for editing was not confirmed in this review.

[Software](https://store.bricklink.com/v2/build/studio.page) · [Collision checks](https://studiohelp.bricklink.com/hc/en-us/articles/5412820155927-Collision) · [Stability checks](https://studiohelp.bricklink.com/hc/en-us/articles/6501498505111-Stability-check)

<a id="leocad"></a>
### 11. LeoCAD — open-source viewing, editing and rendering

**What it does:** An open-source LEGO editor supporting LDraw on Windows, macOS and Linux.

**How to use it:** Inspect generated models or export images from the command line to give the agent visual feedback on its own designs.

**Available:** Software, source-code links and command-line documentation. **Limit:** Command-line rendering and export are not a complete remote-editing API. This is not a mechanism physics simulator.

[Website and source links](https://www.leocad.org/) · [Command-line documentation](https://www.leocad.org/docs/cli.html)

<a id="verification"></a>
## 4. Checking assembly and function

<a id="technic-sim"></a>
### 12. LegoTechnicSimulation — converting models into motion and simulation representations

**What it does:** A community prototype that interprets LDraw connections as rigid bodies, joints, motors and gear relationships, producing Blender animation or MuJoCo models.

**How to use it:** Start with small gear and pin fixtures to assess its suitability as part of a functional validator.

**Available:** Code, fixtures and conversion instructions. **Limit:** Special connectors have limited coverage; convex hulls simplify collisions. Gear constraints are not tooth-contact simulation. Reading back an imposed ratio is not independent verification. Reuse licensing needs confirmation.

[Code and limitations](https://github.com/yoff/LegoTechnicSimulation) · [Fixtures](https://github.com/yoff/LegoTechnicSimulation/blob/main/tests/fixtures/README.md)

<a id="bricksim"></a>
### 13. BrickSim — how a robot physically assembles bricks

**What it does:** A 2026 simulation project for interlocking-brick assembly and manipulation, with assembly, teleoperation and recording/replay examples.

**How to use it:** Study contact modeling, robot execution and demonstration collection if physical robotic assembly becomes part of the project.

**Available:** Paper, code, videos and examples. **Limit:** Current installation targets x86-64 Linux with compatible NVIDIA hardware. Do not assume support for every Technic gear, axle and joint. Robot assembly is an adjacent stage to designing a mechanism for specified motion.

[Paper](https://arxiv.org/abs/2603.16853) · [Code and videos](https://github.com/intelligent-control-lab/BrickSim)

<a id="sariel"></a>
### 14. Sariel's gear tools — checking ratio arithmetic

**What it does:** A LEGO Technic builder's gear-ratio calculator and reference table.

**How to use it:** Create and manually check simple gear-ratio tasks, including deliberately incorrect examples.

**Available:** Web calculator and PDF table. **Limit:** Correct tooth-count arithmetic does not establish that gears mesh at the proposed positions, or that efficiency, loads and supports are acceptable. Define the ratio convention and rotation direction explicitly.

[Calculator](https://gears.sariel.pl/) · [Ratio table](https://sariel.pl/down/gear-ratios-table.pdf)

<a id="pybricks"></a>
### 15. Pybricks — driving real motors and collecting measurements

**What it does:** Python-based control of compatible LEGO hardware, with motor movement, angle and speed readings, plus status and estimated quantities.

**How to use it:** Apply a controlled input to an assembled mechanism and independently measure output direction, speed or travel.

**Available:** Software, documentation and examples. **Limit:** `load()` estimates load; it is not an independent torque sensor. The `gears` parameter rescales readings using the supplied ratio. Those readings cannot establish that the real ratio is correct: measure the output independently. This is neither a simulator nor a training corpus.

[Project](https://pybricks.com/) · [Motor control and measurement](https://docs.pybricks.com/en/stable/pupdevices/motor.html)

<a id="assets"></a>
## 5. Parts, connections, models and physical references

<a id="ldraw"></a>
### 16. LDraw parts and format — grounding designs in real part identifiers

**What it does:** Supplies digital part geometry and a model format representing part references, positions, orientations and steps.

**How to use it:** Establish a shared basis for part identifiers, model exchange and rendering, rather than generating shapes with no corresponding parts.

**Available:** Part files, specifications and updates. **Limit:** Geometry generally does not directly specify friction, load capacity, joint semantics or insertion paths. Add these separately and pin the part-library version.

[Format specification](https://www.ldraw.org/article/218.html) · [Part-library updates](https://library.ldraw.org/updates)

<a id="shadow"></a>
### 17. LDCad Shadow Library — where parts can connect

**What it does:** Adds snapping, connection-location and mirroring information to LDraw parts through corresponding metadata files.

**How to use it:** Generate candidate connections without inferring every hole, axle and pin from raw meshes.

**Available:** Metadata and format documentation; the repository specifies CC BY-SA 4.0. **Limit:** Coverage is incomplete. A valid snap does not establish real friction, axial retention or torque transmission.

[Metadata repository](https://github.com/RolandMelkert/LDCadShadowLibrary) · [Format documentation](https://www.melkert.net/LDCad/tech/shadowLib)

<a id="omr"></a>
### 18. LDraw OMR — extracting mechanisms from existing sets

**What it does:** A community-maintained digital model repository for official sets.

**How to use it:** Select drivetrains, steering, suspension and lifting mechanisms; annotate inputs, outputs, connections and expected behavior. Another task could remove a critical part and ask the agent to repair the mechanism.

**Available:** Downloadable models. **Limit:** “Official sets” describes the sets represented, not LEGO engineering certification of every digital model. Check completeness, licensing and duplicates; these are not ready-made functional training examples.

[Model repository](https://library.ldraw.org/omr)

<a id="philo"></a>
### 19. Philo's motor measurements — checking whether a motor can drive the design

**What it does:** Empirical LEGO motor comparisons, including speed, torque, current and test conditions.

**How to use it:** Select hardware and initial load ranges, or organize the measurements to calibrate assumptions.

**Available:** Charts, experimental descriptions and technical articles. **Limit:** Results depend on supply, operating conditions, motor model and measurement method. Preserve those conditions rather than treating the values as universal motor parameters. Measure important outcomes on the actual apparatus.

[Motor comparisons](https://www.philohome.com/motors/motorcomp.htm) · [Technical articles](https://www.philohome.com/tech.htm)

<a id="bec"></a>
### 20. Brick Experiment Channel — physical mechanism videos and measurements

**What it does:** Author-produced LEGO mechanism demonstrations and experiments, including combined mechanisms and part or motor measurements.

**How to use it:** Learn gear, crank-slider and rack mechanisms visually, then turn examples into tasks with explicit inputs, outputs and pass conditions.

**Available:** Original videos, articles and measurements. **Limit:** Videos are not annotated benchmark datasets. Some measurements involve compatible parts, so preserve part provenance. Public viewing does not imply permission to redistribute videos as training data.

[20 mechanical principles video](https://www.youtube.com/watch?v=M1-YeqGynlw) · [Measured part characteristics](https://brickexperimentchannel.wordpress.com/2023/11/15/characteristics-of-lego-parts/)

## Watchlist: do not schedule experiments around it yet

[GrafXP/TechnicsSimulator](https://github.com/GrafXP/TechnicsSimulator) contains Technic simulation design material and model assets. At review time its README explicitly described a research/design stage with no runnable application; an overall software license was also unconfirmed. It is separate from the 20 selected resources. Planned capabilities should not be presented as implemented features.

<a id="roadmap"></a>
## A practical research starting point

The following is a **proposed experiment**, not an existing benchmark supplied by the projects above.

### Step 1: start with gears, then add linkage trajectories

Define the first task family using a standard LEGO inventory, size limits, input/output shaft locations and a required direction and speed ratio. For example, state **output angular velocity / input angular velocity = −1/3**, where the minus sign means reverse rotation. The agent must handle axles, supports and connections as well as choosing gears.

Manually construct a small set of valid designs and deliberate failures: wrong gear positions, unsupported shafts, insufficient engagement, incorrect rotation direction and blocked insertion paths. Use these to assess the validator first. Allow “unknown” for unsupported cases. A validator that cannot distinguish these examples is not ready to score agents.

Then add ReLink-style tasks: a fixed inventory of beams and pins, with a target endpoint trajectory. This progresses from simple ratio requirements to more complex mechanism design.

### Step 2: choose one design environment and record revisions

Start with Nova, BrickAgent or BrickLayer and complete a read–query–build–check–repair–export loop. Connecting every tool immediately is unnecessary; formats, units, part identifiers and connection semantics may require adapters.

With the same model, tasks and tool-call budget, compare **no checking feedback, geometry/connection feedback, and geometry plus function feedback**. Include rule-based or search baselines. Mouse-and-keyboard GUI operation and Python/command-line tool use should be reported as different experimental settings.

### Step 3: require independent evidence of function

Do not insert a 1:3 ratio into a simulation constraint, read it back, and claim the design has been verified. Derive motion relationships from the actual parts and connections, then cross-check with an independent implementation or hardware measurement.

Assembly tests examine order and insertion clearance. Motion tests measure direction, ratio, travel or trajectory. Hardware tests additionally record motor, input speed, load and stalls. Pybricks can control the input while an additional sensor or video measures the output. Report passed, untested and unsupported checks separately.

### Data to save from day one

| Record | Purpose |
| --- | --- |
| Requirements, inventory, size limits, input/output definitions, software and part-library versions | Make the same task reproducible. |
| Every tool call, model revision and view | Study the design process, not only the final file. |
| Diagnostics, failure causes and repairs | Analyze whether feedback helps; collect potential training examples. |
| Assembly steps, independent function tests, hardware conditions and results | Distinguish plausible geometry, assemblability and working hardware. |
| Provenance, licenses, original set/mechanism family and split assignment | Support reuse and reduce evaluation leakage. |

Report connection validity, assembly success, functional success, joint success across all three, repair count and tool cost. Assess validator false acceptance and rejection on manually checked positive and negative cases. Then test unseen inventories, dimensions and mechanism families to measure generalization.

### Where could the research contribution lie?

[Awesome Brick Assembly & Robot Creativity](https://github.com/intelligent-control-lab/Awesome-Brick-Assembly-Robot-Creativity) already covers design, assembly and robotics. Nova, Mecha and other projects already implement parts of agent design and verification. The broad phrase “AI designs LEGO” is therefore insufficient to establish a distinct contribution.

A more specific focus is **measurable functional tasks using standard LEGO Technic parts, complete records of agent tool use and repair, and evaluation supported by independent assembly and function evidence**. Novelty must ultimately be established through particular data, tasks, methods or reliability results, with continuing comparison against new work.

This guide reviews public papers, repository documentation and official references. It does not report local reproduction of these tools or acquisition and reconstruction of complete training corpora.
