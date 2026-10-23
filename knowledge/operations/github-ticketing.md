---
type: Design
title: "Loop findings to GitHub tickets and controlled work"
description: "Finding intake, certainty, deduplication, GitHub delivery, feedback loops and issue-to-release lifecycle."
status: draft
---

# GitHub ticketing

## Extend the existing Factory protocol

Factory already defines `loop:outer`, severity labels, `agent-ready` and `needs-owner`, one finding
per issue and a search-before-create habit. Keep these concepts. SpaceShip adds durable intake,
concurrent deduplication, repository authorization, rate controls and delivery reconciliation.
It does not ask every agent to hold a general `gh` write credential.

An outer loop observes and proposes work. It cannot deploy, change production configuration or
promote itself into an authorized fixer. Inner work starts only after deterministic intake and
the applicable human triage. Labels are a user interface to state, not the source of authority.

## Finding envelope and certainty

An accepted finding contains source company/project/repository IDs, rule/tool/version, source
revision and relevant file/range, observed symptom, acceptance invariant, bounded evidence
references, certainty, sensitivity, suggested smallest fix, verification plan and producer identity.
Descriptions are untrusted text. Limit bytes, links, attachment count and supported formats.

| Certainty | Meaning | Default handling |
| --- | --- | --- |
| Reproduced functional defect | Trusted check demonstrates expected versus observed behavior | Ticket candidate; not automatically safe to fix |
| Confirmed security finding | Established boundary failure with current-source evidence | Private security intake; severity only on established impact |
| Needs validation | Specific source-grounded hypothesis with an unresolved fact | Owner/validation queue, no passing or confirmed badge |
| Rejected | Candidate disproved by current evidence | Retain reason; suppress only the same unchanged failed claim |
| Advisory | Improvement or best-practice deviation | Separate backlog; do not label it a vulnerability |

Cloudflare findings retain their original verdict, fingerprint and source provenance in a namespaced
payload. Validate schema and coverage artifacts with the pinned validator, then apply Æion's
trusted intake rules. Schema validity is not proof of a bug. A partial audit cannot create a
“whole repository secure” ticket closure or silently suppress uncovered units.

## Deterministic fingerprint and deduplication

Define a fingerprint from canonical company/repository identity, stable rule ID, normalized
affected boundary/component and root-cause identity **where established**. Preserve code revision
as evidence rather than always making it part of the dedup key: otherwise every commit reopens
the same incident. Include a schema version for fingerprint migrations.

A stack trace hash alone is unstable; an LLM-generated title alone is neither stable nor safe.
If no defensible root-cause key exists, create a bounded provisional candidate and ask for triage.
Semantic similarity can suggest duplicates but cannot silently discard a distinct failure.

Use a unique database constraint for the canonical fingerprint and one transaction to upsert the
finding, append its observation and enqueue the external intent. Concurrent loop results converge
on one local ticket. Closed findings reappear according to an explicit recurrence rule: unchanged
failure reopens with new evidence; a different root cause creates a related issue. Keep occurrences
and first/last seen without flooding GitHub with a comment for every sample.

## GitHub App and receiving scope

For a company install, use a GitHub App installed only on approved repositories. Mint short-lived
installation credentials outside workloads. A ticket-only connector requests the minimum issue
permissions it needs; PR creation, merge and deployment use separate receiving roles/services.
Permission names and endpoint requirements must be checked against the chosen API version.
An `issues:write` grant is not a merge grant, and a broad installation token is not made safe by
asking the model to use it carefully.

Bind requests to installation ID and numeric repository ID, then resolve the current canonical
name through trusted configuration. Do not accept a repository URL from a finding as a credential
destination. Validate redirects/hostnames for allowed GitHub or declared Enterprise Server hosts.
Apply company/project limits before opening any external ticket.

## Outbox delivery and unknown outcomes

```text
finding accepted
  → local ticket upsert + issue-create intent committed atomically
  → connector claims bounded lease
  → authorization and repo scope rechecked
  → existing opaque marker reconciled, if a previous send is possible
  → create or update issue
  → receiver ID/URL/result recorded
```

Add an opaque machine marker to issue bodies so a lost response can be reconciled. GitHub's
issue-create endpoint is not assumed to support an idempotency key. A successful local transaction
cannot make a remote POST exactly once. When a response is lost, record `effect_unknown`, list
the relevant repository issues through a bounded reconciliation query, and match exact markers
and App identity. Search indexing alone may lag. If duplicates remain possible, stop blind
creation and surface the uncertainty; reconcile duplicates under a documented owner action.

Webhook ingestion verifies the raw body HMAC before parsing, applies body/time limits and
deduplicates delivery IDs. GitHub delivery identity is not an event-order guarantee. Re-read
the authoritative issue/PR state before a protected transition. Verify installation/repository
scope independently of user-supplied text. Handle redelivery, deletion, transfer and lost access.

Retries classify transient/rate-limit errors versus permanent permission/schema errors. Respect
receiver backoff signals, bound attempts and deadlines, and retain a visible dead-letter record.
Do not retry an uncertain mutation as if it were a failed read. A human can reconcile or cancel
an intent; cancellation after send cannot pretend the issue was never created.

## Issue body and labels

The trusted formatter produces:

1. Observed symptom and expected invariant.
2. Exact current source and relevant location, with sanitized evidence references.
3. Certainty and sensitivity; limitations or missing deployment facts.
4. Smallest proposed correction and trusted verification steps.
5. Run/finding identity, occurrences and policy reason for routing.
6. Opaque machine reconciliation marker.

Escape or remove unsolicited mentions and unsupported external links. Never include credentials,
private prompt/source content, raw environment, unrestricted exploit instructions or unrelated
customer records. Security-sensitive material stays in protected storage; a public issue can
contain only an explicitly approved sanitized summary.

Retain Factory labels and add bounded labels only if useful: `source:spaceship`, `kind:bug`,
`kind:security`, `state:needs-validation`, `state:blocked`, `risk:critical`, `area:<catalog-key>`.
Keep detailed state in the authoritative store rather than an ever-growing label vocabulary.
GitHub labels and assignable users must exist/resolve before mutation; failure remains visible.

## When may a ticket become agent-ready?

All required conditions must hold: approved repo/source, reproducible or accepted work contract,
clear acceptance criteria, allowed data/runtime/profile, available reservation, narrow capability
scope, no unresolved high-impact decision, and no conflicting active owner. A model can propose
these facts; a trusted service verifies applicable conditions. An owner promotion does not grant
undeclared network, deployment or financial capabilities.

The first implementation uses one issue per run and one active worker. A worker creates a branch
and a PR referencing the issue. Its patch remains untrusted. CI/review/merge/release follow
separate policies. A loop must never recursively spawn more work without per-project caps,
deduplication and backpressure.

## Routine catalog and suppression

| Routine | Trigger | Output / authority |
| --- | --- | --- |
| Functional health | Explicit schedule or trusted check failure | Reproduced defect candidate |
| Docs / source drift | Versioned scheduled scan | Documentation proposal |
| Security source audit | Approved scope/budget and pinned skill | Findings and coverage gaps, private by default |
| Dependency/upstream watch | At least weekly for designated tools | Maintenance proposal with exact diff |
| PR freshness | Forge event plus reconciliation | Invalidate stale decisions; no self-approval |
| Outcome watch | Deployment/acceptance horizon | Verified resolution, regression or unknown outcome |

Schedules are deterministic records with timezone, overlap policy, deadline, jitter seed when
used, and missed-run behavior. Disable catch-up storms. Suppressions have rule/scope/reason/owner/
expiry; they are visible and cannot turn unknown coverage into a passing audit.

## Closure and measurements

Close as resolved only when the policy's resolution condition is established. For a local code
defect, trusted tests on the merged artifact may suffice. For a deployed failure, require target
verification and the declared observation horizon. Regressions reopen or link to the original.

Measure actionable findings, duplicate rate, rejected hypotheses, time to triage/fix/verify,
external-delivery unknowns, issue spam prevented, corrective human time and total cost per verified
resolution. The number of tickets created is not a productivity target.
