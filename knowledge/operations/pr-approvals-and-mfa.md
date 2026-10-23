---
type: Design
title: "Deterministic PR decisions and action-bound human approval"
description: "Manual, hybrid and autonomous modes; critical code classification, trusted checks, stale approval rejection and MFA."
status: draft
---

# PR approval and MFA

## Core rule

Small change size, green tests and a strong API/model score do not establish safe authority.
A one-line change can disable authentication, alter a payment formula or bypass policy. Risk
classification and required human authority take precedence over convenience signals.

Keep three modes available. The company publishes the mode and scope; a task cannot select a
more permissive policy for itself. Merge authority and deployment authority are separate even
when both are automated.

| Mode | Automatic PR eligibility | Human requirement |
| --- | --- | --- |
| Manual | Prepare evidence and recommendation | Every PR needs the declared reviewer role |
| Hybrid — recommended initial mode | Complete low-risk facts, allowed paths, bounded change, trusted checks, all other gates | Sensitive/unknown/large changes or vetoed evidence |
| Autonomous | Unattended within explicit company-preauthorized code/risk scope, including separately approved business-critical scope if chosen | Outside that scope; governance/security administration retains separate authority |

Autonomous is an intentionally higher-risk profile. It removes per-PR human approval only for its
published scope; it never ignores failed checks, missing evidence, revoked authority or forge
protection. “Accept everything including changes to the agent's own permissions” is incompatible
with a zero-trust boundary and is not a supported shortcut. Owners can change root policy only
through the separate administration path.

## Trusted risk inventory

The company maintains critical components and owners: authorization, deterministic business
rules, money calculations, data deletion/migrations, public contracts, infrastructure, release
workflows, secrets, policy/evaluator code, dependency lockfiles and executable plugin configuration.
Explicit paths are the first reliable signal. Add qualified dependency/AST impact analysis only
as supplementary evidence; a stale or incomplete graph cannot prove low impact.

Evaluate old and new paths for renames, deletions and moves. Check file modes, symlinks,
submodules, binary/generated content, archive paths and normalization. Unrecognized content and
unknown classification route to review. A generated file can be a production input and therefore
cannot be exempted automatically. Changed-line thresholds apply only after risk and scope gates.

An LLM may identify a missed risk and request stricter review. It cannot move a protected path
into the low-risk class. Policy owners review changes to the inventory itself independently.

## Decision sequence

1. Authenticate installation/repository/company and identify the expected PR head and base.
2. Collect complete file/diff metadata using trusted APIs, handling pagination and truncation.
   Missing files, unknown mergeability or an incomplete diff prevent automatic eligibility.
3. Freeze policy/evaluator/risk-inventory versions and classify the full change deterministically.
4. Require current trusted checks for the exact head and, where used, tested merge/base identity.
   Bind check producer App/workflow definition and runner profile, not just a familiar check name.
5. Evaluate security, dependency, artifact, data, budget and policy-integrity obligations.
6. Apply the published mode. Size and advisory scores can impose additional review after hard
   rules; they cannot cancel a hard rule.
7. Produce reason codes and either deny, request human/step-up, or issue a narrowly bound
   expiring merge intent. Record the decision before its protected transition.
8. The merge connector revalidates current head/base/policy/revocation and receiving scope.
   Use GitHub's documented expected-head SHA on merge and handle mismatch as invalidation.

The REST expected-head comparison does not alone protect against changes to the base branch.
Use an appropriate strict-update/merge-queue workflow or serialize and revalidate the tested
integration state. A queue entry means queued, not merged. Checks for merge groups need their
own supported trigger and identity. Always observe the final merge result before progressing.

## What qualifies as a trusted check?

A green test result is meaningful only with a protected check definition, exact tested inputs,
trusted runner identity and a policy for flaky/skipped/neutral results. SpaceShip may demand
explicit success even where GitHub accepts other conclusions. If a PR changes the tests or
workflow that supposedly proves it safe, require the corresponding independent review and/or
unchanged external acceptance suite.

Untrusted PR code runs without merge/deploy secrets or a write-capable forge token. Never fetch
and execute fork-controlled code in a privileged `pull_request_target` job. Artifact downloads
and `workflow_run` do not sanitize untrusted contents. Scan/export steps have bounded inputs and
safe extraction. Pin release-critical actions and reusable workflow definitions to reviewed
identities. Do not assume a plan tier provides every desired GitHub protection.

## AI review / Decisions API scoring

Preserve Factory's approved owner decisions separately from optional AI scoring. Store an AI
review's model/provider/version, rubric, input source digest, prompt policy, output schema, cost
and uncertainty. It can create review comments, flag a suspected defect or veto automatic flow.
It does not sign a trusted check or approve another agent's authority.

Do not multiply reviewers by default. Same-model reviewers with shared context can fail together.
Use deterministic checks first and targeted independent review only when it adds information.
Evaluate false negatives and actual regressions, not average score or review verbosity. Missing,
malformed or stale advisory output cannot satisfy a required advisory gate.

## Human decision and fresh step-up

GitHub login 2FA verifies a login; it does not prove that a person freshly approved this exact
PR/artifact/environment. Required reviewers on an environment are useful native controls, but
must be evaluated against the company's assurance requirement. Their availability varies by
repository visibility and plan. Inspect the actual installation rather than assume support.

Prefer the enterprise's existing OIDC identity and an established WebAuthn/passkey step-up
mechanism. Do not build a new authentication protocol or email a fixed bypass code. If fresh MFA
is required but the integration cannot establish it, keep the action waiting; a local “Approve”
button is not an acceptable substitute.

The approval challenge/receipt binds:

- Company and installation, authenticated user and required role, separation-of-duty requirement.
- Action (`merge` or `deploy`), repository numeric ID and PR number where applicable.
- Exact head and tested base/integration identity; artifact digest and destination environment.
- Policy/evaluator/required-check-set digests and current target generation for deployment.
- Issuer, audience, nonce, issued time, freshness/expiry and assurance evidence.

Validate issuer/audience, role, current eligibility and required assurance server-side through
the chosen identity integration. Store one-use consumption transactionally with the action intent.
Reject replay, expiry, wrong action/environment/company, role loss and any changed bound input.
The challenge must show the concrete artifact and consequences clearly enough for a person to
review. Mobile approval uses the same identity and binding rules, not a second weaker channel.

For four-eyes policies, initiator and approver must be distinct and authorized. An autonomous
coding agent is not the second person. Recovery codes and break-glass actions belong to the IdP
and company policy, with explicit audit and expiry; the workload cannot access them.

## Representative decision table

| Situation | Hybrid | Autonomous with ordinary product scope |
| --- | --- | --- |
| Tiny allowlisted UI change, exact trusted success, complete evidence | Eligible | Eligible |
| One-line deterministic pricing/risk-core change | Step-up / owner | Only eligible if that critical business scope was separately preauthorized |
| Policy, authentication or privileged release workflow change | Separate owner authority / step-up | Separate owner authority / step-up |
| High score, failed or forged test result | Deny | Deny |
| Green checks from a previous head | Deny / invalidate | Deny / invalidate |
| Large ordinary change with complete facts | Human by size rule | Evaluate explicit autonomous scope and limits |
| Unknown file mode, incomplete diff or dependency impact | Review / no automatic action | Review / no automatic action |
| Human approved head A, branch now head B | Invalidate | Invalidate |
| Native GitHub protection blocks merge | Block; show reason | Block; never request bypass privileges |

## Audit and user experience

Every decision shows the failing or satisfied rule, source facts, policy version and required next
action. Distinguish refusal from a missing integration. A denial is a successful safety outcome,
not an agent failure to be retried indefinitely. Store approval and merge receipts separately;
approval does not imply a merge occurred. Never close a deployment ticket from a merge-intent log.
