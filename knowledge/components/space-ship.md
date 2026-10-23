---
type: Component
title: "Deterministic software-factory control plane"
description: "SpaceShip ownership, trusted inputs, explicit outputs, authority invariants and release acceptance contract."
status: draft
sources:
  - id: baseline
    resource: ../../PLAN.md
    title: "Owner scope and architecture decisions"
  - id: evidence
    resource: ../references/research-register.md
    title: "Source evidence and limits"
---

# SpaceShip component contract

## Intent

Provide one understandable control surface for bounded software work across Factory, OPS,
CROA and Observability. Centralize **authorization decisions**, not every tool's implementation.
Keep task execution useful while making company constraints enforceable without model judgment.
Start locally with Docker and graduate to isolated per-company installations.

## Data sources

| Source | Trust and authority | Freshness / failure behavior |
| --- | --- | --- |
| Company policy registry | Approved, protected policy versions | Missing, expired or invalid required policy refuses the action |
| GitHub/API observations | Forge facts with installation/repo identity | Refresh before effects; webhook hints are revalidated |
| Runtime supervisor | Enforcement and lifecycle evidence | Host/profile-specific qualification; stale proof blocks admission |
| Trusted verifier | Checks for an exact source/artifact and trusted check definition | Workload cannot supply its own passing result |
| Accounting ledger/provider | Reserved, settled and uncertain exposure | Atomic admission; unknown spend retains exposure |
| Enterprise identity | User, role and action-bound step-up evidence | Validate scope, freshness, audience and revocation |
| Agent, memory, plugin, issue body | Untrusted proposals and context | Never a source of capability grants or verified success |
| Observability store | Measured outcomes and recommendations | Delayed/incomplete data labelled; no direct permission writes |

## Inputs

An admission request contains company/project/repository identities; task family and acceptance
contract; approved source revision; policy revision; requested bounded capabilities; data class;
auth/profile reference; resource envelope; budget exposure; deadline; evidence requirements;
requested delivery target and an idempotency key. Secrets are resolved externally by reference.

Protected action requests additionally bind candidate/base identity, artifact digest, check
definitions/results, required approvals, receiver identity, environment, expiry and action nonce.
The [example contracts](../../examples/contracts.md) name proposed fields, not existing APIs.

Repository text cannot become company policy merely by being named `policy.json`. Imported
configuration begins as an untrusted proposal until an authorized owner publishes it.

## Outputs

- Deterministic `allow`, `deny`, `needs_human` or `needs_step_up` decisions with reason codes.
- Versioned task/run/check/approval/effect records and quarantined artifacts.
- Preview or delivered GitHub tickets and PRs, with honest delivery/unknown status.
- Build/deployment receipts bound to the exact artifact and target generation.
- Usage, exposure, intervention and verified-outcome facts with provenance/completeness.
- Evidence exports for CROA and operational incidents, excluding secrets and default content capture.

## Invariants

| ID | Required property | Decisive acceptance evidence |
| --- | --- | --- |
| SS-01 | Repository/agent data cannot expand authority | Injection fixtures cannot alter effective policy or access a protected receiver |
| SS-02 | One company cannot access another's state/capabilities | Negative identity, DB, artifact, memory and runner tests |
| SS-03 | Every protected action binds current exact inputs | Head/base/policy/artifact changes invalidate prior decisions |
| SS-04 | Required audit precedes protected transition | Journal failure prevents dispatch/transition; async trace success is irrelevant |
| SS-05 | Admission accounts for concurrent exposure | Reservation race, uncertain stream and duplicate-charge fixtures |
| SS-06 | Effects have explicit lifecycle and reconciliation | Crash-before/after-send and lost-response tests; no blind retry |
| SS-07 | Worker ownership is exclusive and fenced | Lease expiry blocks the old worker at the receiving service |
| SS-08 | Unknown mandatory evidence cannot grant eligibility | Missing/forged/stale facts produce deterministic refusal |
| SS-09 | Independent checks establish task completion | Agent `done`/confidence cannot close a verified-outcome record |
| SS-10 | Human approval is scoped and nonreplayable | Wrong action/SHA/environment/company, expiry and replay rejected |
| SS-11 | Policy publication cannot approve itself | Agent-authored policy/CI changes need separate authority |
| SS-12 | Stop, recovery and cleanup preserve uncertainty | Cancellation does not erase charges, effects or contaminated workspace evidence |
| SS-13 | Optimization stays within published scope | No new model, region, tool or permission without qualification/policy publication |
| SS-14 | Product claims match support evidence | Unsupported paths visibly fail/disable; no fake certification or synthetic benchmark |

## Determinism

The authority function evaluates a frozen policy against validated, provenance-bearing facts and
recorded state. Time, provider health and external responses are captured inputs. Policy code
does not read a live clock, random source, mutable memory or network during replay. Ordering,
decimal arithmetic, tie breaking, rule precedence and schema versions are explicit.

A deterministic decision can still be wrong when its implementation, trusted facts or policy
are wrong. Correctness needs independent tests, protected policy publication and receiver-side
enforcement. Determinism is neither proof of security nor a guarantee of deterministic LLM output.

## Acceptance checks

Every SS invariant maps to at least one negative and one positive scenario in the
[implementation plan](../operations/implementation-and-poc.md). Release evidence includes
source/policy/toolchain/runtime/harness versions, exact inputs, executed checks, failures,
skips and support limits. A missing check is unknown, not a pass.

Acceptance proceeds through a real local mission, a bounded GitHub demo, separate merge and
deployment gates, crash recovery, both retained auth paths, and measured task outcomes. Production
and unattended modes remain disabled until their specific evidence is accepted by the owner.

## Out of scope

Perfect security, universal autonomous success, replacing the four Æion projects, a new agent
harness/container runtime/LLM gateway, shared SaaS tenancy in v1, autonomous policy administration,
hidden reasoning capture, public disclosure of security findings, and compliance certification.
