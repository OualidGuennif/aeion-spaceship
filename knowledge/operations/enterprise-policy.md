---
type: Design
title: "Enterprise constraints and policy publication"
description: "Company profiles, scope attenuation, policy precedence, data constraints and exact decision contracts."
status: draft
---

# Enterprise policy

## Translate intent into explicit constraints

Onboarding asks about repositories, environments, data, permitted providers, budgets, approval
roles and delivery expectations. The UI converts answers to a proposed policy and shows a
readable diff. A human with the policy-owner role approves the result. An LLM may explain a
question or draft a proposal; it cannot infer permission from “do whatever is necessary.”

Separate three layers: product templates, company policy and run-time fact snapshots. A template
is a starting point, not evidence of a company's actual needs or legal obligations. A fact
snapshot describes observed conditions; it cannot rewrite the policy it is being evaluated against.

## Policy dimensions

| Dimension | Required declaration | Conservative missing-value behavior |
| --- | --- | --- |
| Identity | Company/installation IDs; operator IdP; allowed roles | No protected mutation |
| Forge | GitHub installation, numeric repo IDs, branch and environment scopes | Preview only |
| Governance | Manual/hybrid/autonomous scope, sensitive paths, ownership | Human review; no inferred low risk |
| Data | Classification, allowed region/provider/retention/content rules | No external model dispatch |
| Authentication | Claude subscription or API path, user/service binding | No credential resolution |
| Runtime | Image/runtime/harness versions, required OPS controls | No workload admission |
| Capabilities | Paths, network destinations, API actions, artifacts | Deny undeclared access |
| Resources | CPU/RAM/PID/disk/output/time/concurrency | Refuse unsupported or unbounded envelope |
| Economics | Currency/unit, budget window, exposure and retry rules | No unreserved paid request |
| Quality | Acceptance tests, trusted verifiers, mature-outcome definition | No success or promotion claim |
| Delivery | Build identity, target, health/rollback/migration strategy | No deployment |
| Evidence | Required durable journal, optional analytics, retention | Required-evidence loss blocks the transition |

The [company policy example](../../examples/company-policy.json) is deliberately inactive. It
contains unresolved repository IDs, empty approved model profiles and no qualified runtime.
It must fail real admission until those facts are supplied and approved.

## Precedence and attenuation

Installation invariants apply first. Company policy may narrow the allowed actions; project and
task policy may narrow them again. An exception is separately authorized and cannot override an
unwaivable invariant. Deny overrides allow. A missing classification is unknown rather than the
least restrictive class. A malformed key is an error, not an ignored optional setting.

For sets of allowed capabilities, take the intersection of parent and child grants. For maximum
resources and expiry, take the tighter bound. For evidence obligations, preserve all applicable
requirements. For total exposure, reserve against the shared cumulative scope. Two child grants
of $4 do not fit a parent's remaining $5 merely because each child fits individually.

Keep typed fields for values that affect decisions. Do not evaluate natural-language conditions,
arbitrary JavaScript, shell fragments or a model's interpretation of a Markdown rule. Safe path
and host patterns need one documented matching grammar and exhaustive fixtures. Reject ambiguous
case, traversal, Unicode normalization and platform separator behavior where unsupported.

## Profile catalog

A profile is an immutable bundle, not just a model name:

- Runtime/harness/protocol/auth path and their exact qualified versions.
- Model ID and revision where exposed; allowed serving providers and geographic/privacy constraints.
- Supported inference parameters with requested/effective provenance and fallback semantics.
- Context/tool capability; cost exposure rule; cancellation and retry behavior.
- Required OPS checks; evaluator/outcome evidence; expiry and rollback-compatible predecessor.

Keep a profile's lifecycle `proposed → evaluated → shadow → canary → approved → retired`.
Approval is scoped to company, task families, data class and runtime, not a global “good model”
badge. Provider aliases or serving revisions may drift; mandatory requalification triggers must
be explicit. An unavailable approved profile does not authorize an unreviewed substitute.

Claude subscription tokens remain a supported design path alongside OpenRouter; DeepInfra is an
additional API path. A subscription is user-bound and has distinct billing/automation/visibility
limits. Do not assume its CLI can change every provider parameter or that a fixed subscription
has a precise per-call dollar invoice. The compatibility matrix must preserve these differences.

## Company templates

| Template | Initial scope | Review behavior | What still needs real qualification |
| --- | --- | --- | --- |
| Learning / demo | Disposable source and local preview; synthetic fixtures | Manual, with hybrid demonstrations | Local runtime and claim labels |
| Small product team | Allowlisted repo and preview; one worker | Hybrid for proven low-risk paths | GitHub App, checks, data policy, budget |
| Enterprise controlled | Private repo, company IdP, approved providers and targets | Owner-defined gates; step-up for sensitive changes | Identity, private GitHub features, isolated infrastructure |
| High-impact business logic | Explicit critical components, strong acceptance evidence | Human/step-up by default | Domain-specific verifier and delivery horizon |

These are product presets, not regulatory classifications. Never derive “enterprise approved”
from a selected template or an imported standards checklist. A company can prohibit external
models entirely; that is a valid configuration even if it leaves no eligible coding profile.

## Publication, exceptions and rollback

Keep policy source in a protected control repository or protected service outside worker writes.
Compile and validate it, execute decision fixtures, show an impact diff, obtain the required owner
approval, then publish an immutable digest. Store who approved, scope, expiry and predecessor.
Use an established signing/identity mechanism when signatures cross boundaries; do not invent
cryptography for a JSON file.

Run policy changes in shadow against recent **sanitized** decision snapshots. Report actions
that would become allowed, denied or human-gated. Do not replay external effects. A policy
owner cannot use an agent-authored PR to disable the required independent owner review of that
same PR. Control-plane changes use a separate release path and administration role.

Exceptions name control, scope, concrete reason, owner, maximum exposure, start and expiry.
They remain visible exceptions, not passing controls. Expiry fails new admission; handling of
already running work follows a frozen revocation policy. Emergency stop is outside the agent
boundary and does not require a healthy model endpoint.

Rollback publishes a known compatible policy version for future admission. It does not erase
effects or restore retired models, expired credentials or incompatible artifacts. Security
revocation can cancel an active run; it must produce durable evidence and preserve uncertain
provider exposure.

## Decisions API compatibility

Factory already defines approved/proposed/rejected decisions. Preserve that contract. Treat
an approved owner decision as one authenticated input to Gate; a text reason is not an action
capability. Map its scope, expiry and policy version before use. Missing, proposed, rejected or
unreachable required decisions fail closed. Agents can propose; owners approve.

Do not convert the Decisions API to an AI scoring endpoint. An optional model score is a different
signal with a rubric, source revision, evaluator version and provenance. It may add a veto or
human-review requirement. It cannot reduce a deterministic critical classification or create
permission to merge/deploy.

## Policy acceptance

Require schema validation, unknown-key rejection, replay equality, deny precedence, scope
attenuation, cumulative budget races, expiry/revocation, unsupported capability refusal and
policy-self-change tests. Include company/repository identity substitutions and malformed path
fixtures. The cockpit must show effective policy and reason codes without exposing credentials.
