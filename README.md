# Æion SpaceShip

**An open-source framework for a modular software factory, with deterministic authority.**

Four independent modules. One integration framework. Start with what you need: the minimum
coding method, security directives, an evidence-led audit kit, or observability. SpaceShip
documents how to compose them into governed agent work and delivery.

**Today:** a researched architecture, module catalog, runnable offline examples and implementation
plan. **Planned:** the integrated Mission Control cockpit, runtime adapters, live GitHub ticketing,
action-bound MFA and deployment services. This repository does not start that application yet.

## Choose your starting point

| Module | Choose it for | Available today |
| --- | --- | --- |
| [Factory](https://github.com/OualidGuennif/aeion-factory) | The smallest useful coding-agent setup | Repository scaffold, method, hooks and checks |
| [OPS](https://github.com/OualidGuennif/aeion-ops) | Agent security and operations directives | Framework, Cloudflare snapshot and maintenance checker |
| [CROA](https://github.com/OualidGuennif/aeion-croa) | Assessing the deterministic foundation | Offline evidence-packet CLI; no certification |
| [Observability](https://github.com/OualidGuennif/aeion-observability) | Cost, speed and verified autonomous quality | Contracts, research and runnable synthetic examples |
| **SpaceShip** | Composing a complete software factory | Integration blueprint, catalog and adoption tooling |

**Each repository works independently.** There is no mandatory suite installation, Git submodule
tree or dependency on a running SpaceShip service. Factory remains the shared method; using that
method does not require cloning Factory alongside every module.

## Try one module

For example, inspect the Observability arithmetic with Python 3.9+ and no provider account:

```sh
git clone https://github.com/OualidGuennif/aeion-observability.git
cd aeion-observability
python3 examples/compare_cohorts.py
```

It compares fictional task cohorts, including failures and assistance. It makes no model call
and reports no measured performance gain. Every module has its own
[quickstart and expected result](docs/modules.md).

## Explore SpaceShip

```sh
git clone https://github.com/OualidGuennif/aeion-spaceship.git
cd aeion-spaceship
python3 tools/ecosystem.py check
```

This checks the five-module catalog, generated guide, local links and inactive fixtures. It
does not install upstream tools, run agents, spend provider quota or publish an issue.

| Read | Purpose |
| --- | --- |
| [Module guide](docs/modules.md) | Pick a module; copy a small working example |
| [Getting started](docs/getting-started.md) | Adopt one module or combine selected contracts |
| [Integration contract](knowledge/operations/module-integration.md) | Independent use, optional relationships and upgrade responsibility |
| [Architecture plan](PLAN.md) | Deterministic authority, policies and delivery milestones |
| [Complete technical map](knowledge/index.md) | Security, GitHub, MFA, telemetry, recovery and acceptance |
| [Nine-tool reuse study](knowledge/operations/integrations-and-reuse.md) | Paperclip, OpenShell, Hindsight, ECC, both Anthropic collections, Graphify, Archify and Orca |
| [Website content kit](website/README.md) | Canonical English/French content and publication rules |

The canonical machine-readable catalog is [ecosystem.json](ecosystem.json). The module guide is
generated from it; CI detects drift. [Upstream research pins](knowledge/references/upstreams.lock.json)
serve a different purpose: provenance for the nine-tool study, not automatic installation.

## Deterministic authority

Agents propose and work within a bounded scope. Explicit policies decide permissions, budgets,
validations and protected effects. Model scores, memories and issue comments cannot grant authority.
Manual, hybrid and scoped autonomous modes are designed; failed checks and protected policy
changes cannot be waved through by an agent.

Paperclip is the first work/cockpit foundation to qualify, OpenShell the runtime candidate, and
SpaceShip Gate the proposed policy/effect boundary. Optional memory, graph and plugin tools are
selected only when they add useful capability. No integration is claimed complete because its
logo or name appears in this repository.

The first integrated demonstration is the planned **ParcelDesk** website: a reproducible shipping
bug, deduplicated ticket, bounded correction, trusted checks, policy decision and verified preview.
See the [phased implementation plan and 64 future acceptance scenarios](knowledge/operations/implementation-and-poc.md).

## Open source

Original SpaceShip material is [MIT](LICENSE). Modules and upstream projects retain their own
licences and attribution, including CROA's content-specific terms. See [credits](CREDITS.md) and
[validation evidence](work/validation.md). There is no claim of certification or production readiness.
