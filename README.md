# Æion SpaceShip

**Mission Control for a software factory. Deterministic authority, bounded agent execution.**

SpaceShip is the proposed local-first application that assembles the Æion projects and selected
open-source tools into a governed software-delivery system. People describe work; agents may
propose solutions; explicit policies decide what may run, spend, merge and deploy.

**Current release: researched architecture and implementation plan, 2026-10-23.**
There is no runnable cockpit, agent runtime, GitHub writer, MFA service or deployer in this
repository yet. Examples are inactive design fixtures. The ParcelDesk demonstration is specified,
not implemented. This distinction is part of the product contract.

## The five projects

| Project | Use it when you need | SpaceShip relationship |
| --- | --- | --- |
| [Æion Factory](https://github.com/OualidGuennif/aeion-factory) | The minimum useful agent coding factory | Fixed development method; preserve it |
| Æion Agentic OPS | Security and operational directives | Qualified sandbox, credentials and execution boundary |
| [Æion CROA](https://github.com/OualidGuennif/aeion-croa) | Evidence-led assessment of the deterministic foundation | Audit packets and gaps; no automatic certification |
| Æion Observability | Measured cost, speed and autonomous task quality | Telemetry, evaluations and bounded optimization |
| **Æion SpaceShip** | A complete cockpit and controlled delivery process | Compose the above with deterministic authorization |

Each project remains independently useful and has its own repository lifecycle. OPS and
Observability were inspected as local sibling projects; no public URL is invented for them.
Integration is by pinned contracts and releases, not a copy of four repositories into one.

## Read the plan

Start with [PLAN.md](PLAN.md), then the [complete reading map](knowledge/index.md).
The plan includes:

- A [deterministic core and state model](knowledge/operations/architecture-and-state.md).
- [Enterprise constraints](knowledge/operations/enterprise-policy.md) and a
  [nonexpert cockpit](knowledge/operations/cockpit-and-user-journeys.md).
- [GitHub ticketing](knowledge/operations/github-ticketing.md),
  [manual / hybrid / autonomous PR modes and MFA](knowledge/operations/pr-approvals-and-mfa.md).
- [Build, deployment and recovery](knowledge/operations/delivery-and-recovery.md).
- [Cost / speed / quality control](knowledge/operations/optimization-and-telemetry.md).
- [Security boundaries](knowledge/operations/security-and-runtime.md),
  [maintenance](knowledge/operations/operations-and-upstream.md), and
  [a phased build plan with acceptance scenarios](knowledge/operations/implementation-and-poc.md).
- [All nine requested tools](knowledge/operations/integrations-and-reuse.md), with exact upstream
  revisions in [upstreams.lock.json](knowledge/references/upstreams.lock.json).

## Selected approach

Evaluate **Paperclip as the work/cockpit foundation**, **OpenShell as the sandbox candidate**,
and a small **SpaceShip Gate** for authoritative policy decisions and protected effects.
Reuse existing accounting and workflow mechanisms where qualification proves them suitable.
Do not build another general task manager, install nine overlapping orchestrators, or make an
LLM the system administrator.

Hindsight supplies optional memory; Graphify supplies source analysis; Archify supplies checked
diagrams; ECC and Anthropic repositories supply selected skills/plugins; Orca is an optional
developer interface. Every one has a concrete proposed role, an integration gate and a failure
policy. None gets a blanket trust grant because it appears on this list.

## What “deterministic only” means

Given the same validated facts, policy revision and recorded state, the authority layer returns
the same decision and reason codes. External observations and time are explicit versioned inputs.
Model outputs, API scores, retrieved memories and issue comments remain untrusted information.
They cannot expand permissions or approve their own delivery.

The autonomous mode permits unattended delivery inside an explicitly preauthorized scope. It
does not bypass security controls, missing evidence, budget admission or GitHub protection.
Security and control-policy changes require separate authority. A tiny PR with green CI and a
high model score can still be blocked.

## First implementation target

One local Docker installation, one company, one demonstration repository, one agent at a time.
**ParcelDesk** will calculate shipping prices and contain a reproducible rounding bug. The
first milestone must demonstrate detection → deduplicated ticket → bounded correction →
independent checks → policy decision → preview deployment → verified outcome, including crash
recovery and denied attempts. A prewritten repair is permitted in the offline demonstration
only when explicitly labelled; it cannot be reported as autonomous AI performance.

## Open source and attribution

Original SpaceShip materials are under [MIT](LICENSE). Referenced projects retain their own
licenses, trademarks and authorship. See [CREDITS.md](CREDITS.md). Referencing a project does
not imply endorsement, integration availability or a completed security review.
