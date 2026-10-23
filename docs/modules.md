# Choose your Æion modules

<!-- Generated from ecosystem.json by tools/ecosystem.py render. -->

Every repository can be used independently. There is no mandatory suite installation,
Git submodule tree or dependency on a running SpaceShip service. Factory is the shared
method; adopting that method does not require cloning another repository.

| Module | Use it for | Available today |
| --- | --- | --- |
| [Æion Factory](https://github.com/OualidGuennif/aeion-factory) | Start coding with clear instructions, linked knowledge and checks. | Usable scaffold |
| [Æion OPS](https://github.com/OualidGuennif/aeion-ops) | Define secure execution boundaries and maintain a pinned security-audit toolkit. | Framework and maintenance tools |
| [Æion CROA](https://github.com/OualidGuennif/aeion-croa) | Assess evidence for a deterministic foundation using an attributed CROA audit kit. | Usable offline audit kit |
| [Æion Observability](https://github.com/OualidGuennif/aeion-observability) | Connect session telemetry to verified outcomes, cost and completion time. | Framework and runnable synthetic examples |
| [Æion SpaceShip](https://github.com/OualidGuennif/aeion-spaceship) | Compose the modules into a software-factory framework with deterministic authority. | Integration blueprint and catalog tools |

Start with one module. Combine only the contracts you need. SpaceShip documents
their integration; the integrated cockpit and execution path are not available yet.

## Æion Factory

Start coding with clear instructions, linked knowledge and checks.

Prerequisites: Git, Python 3.

```sh
git clone https://github.com/OualidGuennif/aeion-factory.git
cd aeion-factory
python3 tools/knowledge/knowledge-check
```

Documentation check reports PASS. No model call is made.

Available: Repository scaffold, development method, hooks and checks.

Planned or outside this module: No hosted service or mandatory integration.

License: MIT; upstream content retains its own license.

## Æion OPS

Define secure execution boundaries and maintain a pinned security-audit toolkit.

Prerequisites: Git, Python 3.9+.

```sh
git clone https://github.com/OualidGuennif/aeion-ops.git
cd aeion-ops
python3 tools/check_security_audit_upstream.py --integrity-only
```

Reports integrity_verified and 22 verified files. This does not run an audit or qualify isolation.

Available: 16-control security contract; Complete pinned Cloudflare audit skill and offline integrity checker.

Planned or outside this module: Qualified sandbox and credential mediation.

License: MIT; upstream content retains its own license.

## Æion CROA

Assess evidence for a deterministic foundation using an attributed CROA audit kit.

Prerequisites: Git, Python 3.9+.

```sh
git clone https://github.com/OualidGuennif/aeion-croa.git
cd aeion-croa
python3 tools/croa/audit.py init --system demo
```

Prints an unassessed audit packet. It does not inspect a target or award conformance.

Available: Offline audit-packet init, validation and report CLI; Pinned CROA references and optional callable skill.

Planned or outside this module: Independent deployed-scope assessment; no automatic certification.

License: MIT code and CC BY 4.0 CROA-derived content.

## Æion Observability

Connect session telemetry to verified outcomes, cost and completion time.

Prerequisites: Git, Python 3.9+ for the example.

```sh
git clone https://github.com/OualidGuennif/aeion-observability.git
cd aeion-observability
python3 examples/compare_cohorts.py
```

Prints synthetic cohort costs and cost per autonomous success. This is not a benchmark.

Available: Telemetry, quality and optimization contracts; Offline synthetic cohort comparison.

Planned or outside this module: Live collector, qualified adapters and routing controller.

License: MIT; upstream content retains its own license.

## Æion SpaceShip

Compose the modules into a software-factory framework with deterministic authority.

Prerequisites: Git, Python 3.9+ for the catalog tools.

```sh
git clone https://github.com/OualidGuennif/aeion-spaceship.git
cd aeion-spaceship
python3 tools/ecosystem.py check
```

Checks the module catalog, generated documentation, links and inactive fixtures. It does not start a cockpit.

Available: Modular ecosystem catalog and adoption guide; Architecture, contracts and staged implementation plan.

Planned or outside this module: Integrated cockpit, governed agent execution and delivery adapters.

License: MIT; upstream content retains its own license.
