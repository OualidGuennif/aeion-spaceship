---
type: Design
title: "Independent adoption and optional module integration"
description: "Module ownership, standalone use, optional contracts and how publication differs from runtime integration."
status: draft
---

# Independent modules, explicit integration

SpaceShip is the assembly framework. The four other repositories are independent projects, not
Git submodules, plugins requiring a central daemon, or compulsory product tiers. Use one module,
a selected combination or the full intended architecture.

| Module | Owns | Use independently | Optional integration |
| --- | --- | --- | --- |
| Factory | Method, instructions, linked knowledge and checks | Start a project or adopt selected practices | Supply task/acceptance proposals |
| OPS | Security controls, qualification and audit-tool maintenance | Apply directives to an existing workflow; use the checker | Enforce a qualified manifest and emit lifecycle evidence |
| CROA | Attributed audit questions, evidence packets and offline CLI | Assess an existing system using staged evidence | Consume control/effect evidence, without granting authority |
| Observability | Telemetry, outcomes, quality/cost contracts and examples | Instrument an existing harness against the contracts | Analyze projections and propose future profiles |
| SpaceShip | Composition, authority design, catalog and roadmap | Read the plan and use catalog tools | Implement the integrated runtime through its gates |

Factory remains the common method. CROA includes its inherited scaffold; its CLI needs no second
Factory clone. OPS/Observability can be used with another existing workflow. Independence means
no mandatory Æion installation dependency; it does not erase attribution or engineering provenance.

## Contract boundaries

The [integration envelopes](../../examples/contracts.md) define proposed task/run/artifact/audit/
telemetry/effect interfaces. Each module owns its canonical specification; SpaceShip references
it instead of copying every framework. JSON parsing or a UI badge does not prove a live adapter.

Join company/project/task/run/attempt/source/artifact/check/policy/effect identities. Preserve
producer trust, native usage semantics and unknown states. Model outputs remain proposals.
Runtime, ledger, verifier and receiving-service evidence serve different purposes.

## Versions and ownership

The catalog is a discovery/website contract, not a dependency lock. Current documentation links
use `main`; production adopters must pin reviewed releases/commits and qualified combinations.
Keep compatibility evidence with the implementing adapter. Research pins are provenance only.

Each repository owns its licence, credits, local commands and maturity. When capabilities change,
update the central catalog, regenerate the guide and review website copy. Do not force identical
version numbers or a five-repository release for an isolated module change.

## Adoption paths

- Minimum coding setup: Factory alone; adopt only practices that solve a problem.
- Existing workflow with security needs: OPS directives/checker; qualify the actual runtime separately.
- Deterministic-foundation assessment: CROA alone, with current sanitized evidence and visible gaps.
- Measurement: Observability contracts/example, followed by an observe-only pilot.
- Full software factory: combine selected contracts and follow SpaceShip's implementation gates.

The last path remains a roadmap. It is not a one-command production platform today.
