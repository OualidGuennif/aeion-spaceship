---
type: Design
title: "Build, deployment, verification and recovery"
description: "Separate merge and release authority, immutable artifacts, target fencing, migrations, health checks and rollback."
status: draft
---

# Delivery and recovery

## Separate the delivery authorities

A coding run produces an untrusted patch. A trusted verifier checks it. GitHub may merge the
reviewed source. A build service produces an immutable artifact. A deployment service changes a
specific environment. An outcome verifier observes the resulting behavior. These steps may share
infrastructure, but each needs its own identity, inputs and authorization.

An issue label, model `done` message, successful push, green PR or accepted deployment request
does not establish that the intended application version is serving correctly. Show these facts
separately in Mission Control. Deployment policies can be stricter than merge policies.

## Proposed pipeline

| Stage | Inputs and authority | Output and failure treatment |
| --- | --- | --- |
| Quarantine | Bounded patch/artifact export from OPS | Safe regular-file inventory; reject traversal/symlinks/devices/unexpected executables |
| Verify candidate | Protected check definition + exact source and toolchain | Signed/identified result; missing coverage remains unknown |
| Merge | Current head/base policy + scoped forge service | Observed merge commit; queued/pending is not merged |
| Build | Approved source, reviewed build definition, dependency provenance | Content-addressed artifact, SBOM/provenance as required |
| Release admission | Artifact digest, target policy, approvals, health/rollback prerequisites | Durable exact-target intent or explicit refusal |
| Deploy | Receiver-scoped short-lived authority and expected target generation | Observed target receipt, not just request acceptance |
| Verify outcome | Trusted probes against expected version/contract | Verified, failed or unknown; retain intervention and latency |
| Close / recover | Declared observation horizon and effect state | Resolution evidence, rollback or human recovery |

Treat build scripts and package lifecycle hooks as untrusted execution too. A privileged builder
is not safe merely because the code passed an LLM review. Use isolated ephemeral build workers,
minimal network/setup policy, no production credentials and protected release definitions.

## Artifact identity and provenance

Build once for a release and promote the same digest. Record source commit, build definition,
toolchain/image/dependency identities, inputs, producer identity, artifact type/size and verification
results. A mutable image tag or filename is not the release identity. Verify provenance/signature
requirements at the deployment receiver, not just in the UI.

An agent-authored provenance file is not trusted build attestation. Use an established build and
signing mechanism when needed, with a documented trust root and verification policy. Do not invent
a signature format or claim SLSA conformance merely because a JSON receipt exists. Key access and
release permission stay outside coding workers.

Use GitHub Actions OIDC for cloud credentials where the target supports a correctly restricted
trust relationship. Bind allowed repository/workflow/environment/subject/audience claims and
review changes to that trust policy. Short-lived credentials reduce exposure but do not fix an
overbroad role. Private company targets may use another established workload identity mechanism.

## Target adapter contract

A deployment target declares supported artifact types, health probes, concurrency model,
credential scope, rollback capability, migration policy and evidence. Its interface must support
observation and safe reconciliation in addition to requesting a change.

```text
observe target → validate expected generation → authorize exact artifact/action
→ commit intent → receiver admits current fencing generation → apply
→ observe target artifact/generation → verify health → record result
```

Logical adapter operations are `preflight`, `observe`, `apply`, `cancel`, `reconcile` and, only
when supported, `rollback`. These names describe requirements, not existing vendor SDK methods.
Every effect binds company, target, environment, digest, expected prior state, policy and expiry.
Refuse a target that cannot enforce a required scope or safe concurrent-update condition.

The first target is a disposable local preview. Later targets are qualified one at a time,
using their native APIs and documented semantics. Do not generate a generic shell string and
execute it on arbitrary enterprise servers. No Kubernetes requirement is introduced for a
single local preview.

## Concurrency and unknown effects

Serialize effects for one environment and use receiver-side compare-and-set/fencing where
available. GitHub workflow concurrency groups can help scheduling but are not a substitute for
target-side authority or a complete distributed lock. A stale worker must not deploy after a
newer run acquired ownership.

| Failure point | Required response |
| --- | --- |
| Crash before intent commit | No authority exists; safe to retry admission |
| Crash after commit before send | Reclaim outbox lease and revalidate current authority |
| Timeout during send | Mark unknown; observe/reconcile target before another mutation |
| Receiver reports conflict/new generation | Invalidate intent; collect fresh facts |
| Controller stopped after target applied | Recover by observed digest/generation; do not deploy twice blindly |
| Health result missing | Remain unverified; do not close ticket or fabricate rollback success |
| Cancellation sent | Track acknowledged stop and final target state separately |
| Rollback response lost | Preserve unknown state and reconcile; do not oscillate releases |

Idempotent requests need a receiver contract. A locally unique ID alone cannot prevent duplicate
effects on an API that ignores it. Retain reconciliation identities beyond maximum delivery/
retry windows. A lease timeout must not authorize a destructive replacement while effects remain
unresolved.

## Health, canaries and rollback

Define health before release: version identity, startup readiness, contract probes, error/latency
conditions and observation horizon. A healthy HTTP 200 from an old version is not proof that the
new artifact deployed. Use bounded synthetic fixtures and protected probes; agent-authored
“looks good” screenshots cannot replace required checks.

For a preview, a short bounded probe may suffice. For a company environment, canary size,
traffic window, comparison baseline, rollback triggers and approving roles are explicit. Do not
present example percentages or minutes as universally safe thresholds. Collect real baseline
behavior and account for delayed regression detection.

Rollback restores a supported known artifact/configuration through the same target authorization
path. Confirm its resulting version and health. It cannot undo leaked data, irreversible external
actions or an incompatible database migration. Preserve incident state even when the application
returns healthy.

## Data and migrations

Migration plans name reversibility, backup/restore evidence, backward compatibility, dual-version
behavior, lock/timeout effects and an owner. Schema, destructive data operations and irreversible
steps require the company's explicit gate. A source-code rollback is not a database recovery
strategy. Never let a coding agent discover live credentials and run migrations as a repair tactic.

For the first POC, use an application without a shared production database and no real customer
data. Demonstrate migration refusal with a synthetic fixture instead of building a migration
platform before the ordinary delivery path works.

## Release evidence and closure

Record all-in elapsed time from task admission to verified outcome, including queued review,
build/retry/canary and recovery. Split active machine time, required human approval wait and
corrective human effort. Keep failures in the denominator of performance reports.

A release receipt binds source, artifact, checks, policy, approval, receiver state and observed
outcome. Export sanitized evidence to CROA and Observability. Retention/deletion rules preserve
required audit integrity without default collection of source, prompts or hidden reasoning.
