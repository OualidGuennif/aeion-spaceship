---
type: Design
title: "Cost, speed and verified autonomous quality"
description: "Use the Observability contract for bounded profile selection, trustworthy accounting, delayed outcomes and controlled experiments."
status: draft
---

# Optimize the delivery triangle

## Reuse the Observability framework

Æion Observability already defines telemetry, provider capabilities, quality evaluation and
observe/shadow/canary/bounded-adaptive modes. SpaceShip implements the authorized decision path
and displays those measurements. It must not create a competing token ledger or redefine
autonomous success to make its own dashboard look better.

The primary product outcome is a verified task completed without corrective human intervention,
within its declared acceptance horizon. A mandatory approval is governance, not corrective rescue.
Human code repair, missing-input rescue and environment help remain distinct assistance signals.
If intervention coverage or outcome labels are missing, quality is unknown.

## Decision objective

First enforce permissions, privacy, runtime qualification, budget, required evidence and deadline.
Then choose among eligible approved profiles using a published preference. One useful objective:

```text
minimize predicted all-in cost per verified autonomous success
subject to conservative quality evidence meeting the task-family floor
           conservative completion-time evidence meeting the task deadline
           every enterprise authority constraint remaining satisfied
```

These are uncertain estimates, not guarantees. Do not sum request p95 values and call the result
a task p95. Do not calculate a cost-per-success metric from successful calls while dropping failed
tasks, human rescue, reviewer/evaluator calls, sandbox cost and retries.

Offer understandable presets: “economical within my deadline”, “fast within my budget” and
“quality floor first”. Show the resulting concrete constraints before publication. Avoid an
unexplained weighted score whose arbitrary coefficients can trade away a mandatory quality floor.
Security is a hard constraint, not a fourth term in a negotiable utility function.

## Three control speeds

| Loop | Required direct observations | Permitted action |
| --- | --- | --- |
| Request operations | Request timer, health, current reservation, current policy | Admit, bounded retry/backoff, approved same-profile route, cancel |
| Task checkpoint | Verified progress, artifacts, unresolved tools/effects, remaining envelope | Continue, approved escalation/restart or defer |
| Policy improvement | Mature comparable outcomes, total cost, intervention coverage | Propose/evaluate/publish a future policy under owner authority |

Start with one sticky profile per task. Do not switch models on every tool call. Later allow one
qualified checkpoint escalation only when state portability, tool completion and privacy remain
valid. Include re-prefill/cache loss, repeated setup, summaries and abandoned attempts in cost.
Use bounded dwell time/switch count to prevent oscillation.

## Profile selection algorithm

1. Validate the approved catalog/policy scope, freshness and task binding.
2. Filter by auth/protocol, context/tool support, data region/privacy, runtime and provider scope.
3. Exclude unhealthy/expired profiles and unsupported required parameters.
4. Require defensible request exposure and available atomic admission; never infer zero cost.
5. Apply quality/time evidence gates from comparable mature tasks. If evidence is insufficient,
   use only an explicitly approved measurement baseline and label uncertainty.
6. Select by the published preference and deterministic tie breaking; record all exclusions.
7. Reserve exposure atomically, recheck cancellation/current authority and dispatch through the
   qualified adapter. Record effective-application acknowledgement where observable.

Model-generated difficulty estimates are optional features only after showing benefit against
simple task-family rules. A second LLM on every scheduling step adds cost and correlated errors;
it is not part of the authority algorithm.

## API paths and parameter controls

| Path | Proposed actuation | Qualification / limitation |
| --- | --- | --- |
| Claude subscription CLI | Supported task-level model/effort and bounded runtime behavior | Do not assume a per-call invoice or arbitrary provider controls |
| OpenRouter API / compatible harness | Explicit model/provider allowlist and supported parameter bundle | Required parameters, fallback, privacy and serving-provider behavior must be tested |
| DeepInfra API / compatible harness | Model-specific reasoning, output/service-tier/cache controls where supported | Accepted values and effective behavior vary by model and protocol |

OpenRouter documents provider-routing preferences; preference is not a hard latency guarantee.
When required, use its documented required-parameter behavior and verify the selected profile.
Price-per-token filters are not cumulative spend caps. DeepInfra documents model-dependent
reasoning controls; do not map every provider's effort labels through one interchangeable enum.
Use the existing Observability provider matrix for detailed payloads and caveats, refreshing it
before implementation. No live model identifiers or guessed parameters are preapproved here.

For each setting retain requested value, adapter support, provider acknowledgement and unknown
effective values separately. If a harness cannot expose or apply a required control, classify the
profile unsupported rather than silently remove the setting. Interrupted streams may lack final
usage. Cancellation does not prove the provider stopped billing.

## Financial admission

Maintain exact currency/unit semantics, integer minor units or decimal arithmetic, and explicit
price snapshots for estimates. Preserve native cache/reasoning token meanings; subsets must not
be counted twice. Deduplicate duplicate telemetry for one billable attempt, while separately
billable retries remain distinct charges.

Reserve before dispatch under the one authoritative transaction path. Track held, settled,
released and uncertain exposure. A provider overrun is recorded as a breach; it is not discarded
to keep the ledger within its cap. Provider-side/key caps can add protection but do not replace
admission or establish zero overshoot. A reservation based on an estimate is not a contractual
upper bound on a provider bill.

Paperclip has relevant accounting/reservation source. Qualify reuse and the precise dispatch
boundary before implementing another ledger. Observability receives a projection with lineage;
it cannot release a hold because an agent span ended.

## Telemetry and outcome joins

Join company/project/task/run/attempt, logical inference call, provider request, source/artifact,
check, decision, effect and outcome IDs. Keep IDs in traces/logs rather than unbounded metric
labels. Preserve producer identity and trust class: workload-reported, runtime-observed,
forge-confirmed, provider-reported or trusted-verifier result.

The cockpit shows spend versus reserved/uncertain exposure; end-to-end and queue/active/approval
latency; verified autonomous success, assisted success, failure and unknown; retry/escalation;
policy denials; cleanup and telemetry gaps. Default content capture is off. Do not store hidden
reasoning, prompts, code, tool payloads or raw headers merely to obtain session charts.

## Experiments and promotion

Begin with a small comparable task corpus, frozen acceptance tests and a fixed control profile.
Separate task families/risk classes. Predeclare quality floors, time/cost targets, minimum
evidence, exposure cap, stopping rules and rollback before testing candidates. Record assignment
probabilities when a randomized policy is used. Never label unfinished tasks as successes.

Promote only after compatibility/privacy/OPS gates and sufficient mature outcome evidence.
Count evaluator and experimentation cost. Check whether a faster/cheaper profile still wins after
human repair and retries. Guard against correlated LLM judge errors with deterministic acceptance
and calibrated independent evidence. Offline synthetic examples cannot rank real models.

Online bandits are a later optional method, not the initial controller. They require compatible
arms, logged assignments, delayed-label treatment and a bounded exploration budget. A learned
recommendation becomes a published policy proposal; it cannot bypass the allowed model catalog.

## Degradation and stop conditions

If analytics fail, stop learning and show the gap. A fixed approved baseline may continue only
while required audit, financial admission and runtime controls remain available. If required
accounting or authority evidence fails, stop new dispatch. Quality regression stops candidate
promotion; privacy/control violations trigger containment. Restore a compatible approved policy
for future tasks while preserving in-flight uncertainty and evidence.
