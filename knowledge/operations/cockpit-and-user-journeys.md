---
type: Design
title: "Mission Control product and user journeys"
description: "Progressive onboarding, mission queue, explainable gates, approvals and honest performance views for nonexpert users."
status: draft
---

# Mission Control

## Product principle

Make the next useful action understandable. A person should not need to know what OTLP, a lease
or a provider parameter means to launch an approved task. They must still understand which
repository/data/environment they authorize, what it may cost, what will be delivered and what
requires their decision. Expose technical evidence in a details drawer rather than every screen.

The visual direction is a restrained mission-control cockpit: clear hierarchy, readable contrast,
one primary action, visible operating mode and no animated “agents working” decoration used as
proof of progress. Status changes come from durable state and observed evidence. All demo data
and synthetic measurements carry a persistent visible label.

## Main screens

| Screen | Default view | Useful drill-down |
| --- | --- | --- |
| Overview | Running/queued/waiting missions, budget/exposure, integration health | Policy and evidence freshness; company/installation scope |
| Missions | Outcome, repository, stage, next action, elapsed time | Timeline, attempts, acceptance checks, artifacts |
| Tickets | Reproduced defects, validation needs, duplicates grouped | Current evidence, recurrence, external delivery state |
| Approvals | Concrete proposed action and consequence | Exact source/artifact, diff, applicable rule, identity assurance |
| Performance | Verified autonomous outcomes, total cost, time, human repair | Comparable cohorts, unknown coverage, profile/version lineage |
| Connections | Repository, runtime, provider and target readiness | Required capability missing, safe repair instructions |
| Policies | Human-readable effective constraints and publication status | Version diff, replay impact, owner/expiry/exception |
| Architecture | Reviewed source-backed system/boundary map | Graph evidence, revision, unknown/stale relationships |
| Evidence / audit | Required controls and actual evidence coverage | CROA packet export, gaps, scoped assessments |

Do not turn the initial UI into a general organization/HR system if Paperclip already provides
that surface. Expose Æion-specific authorization, verified outcomes and cross-tool evidence.

## Onboarding: one local company

1. **Choose a demo or a repository.** The first run offers ParcelDesk with no external account.
   Importing a real repo requires an explicit scope and source revision; do not execute its setup.
2. **Choose allowed operating bounds.** Show local runtime readiness, data/model permission,
   budget/deadline and review mode. Defaults are preview/manual until qualified.
3. **Connect only what the path needs.** GitHub is optional for the offline demo. Real writing
   uses the scoped App setup. Provider credentials are enrolled through the operator's supported
   flow and kept outside chat/repository data. Keep subscription and API paths available.
4. **Run preflight.** Display “ready”, “needs configuration”, “unsupported” and “unknown” honestly.
   A failed required control cannot be fixed by a more permissive prompt.
5. **Review the mission contract.** Plain description, acceptance examples, maximum envelope,
   artifact/target and expected human gates. Launch only the approved scope.

The wizard explains a consequential missing choice once. It can propose safe defaults for a
demo, but must not infer a company region, data permission or production target from convenience.
An owner can finish onboarding in stages; disconnected integrations remain visibly unavailable.

## Golden journey: a delivery defect

The user selects “check ParcelDesk's shipping calculation”. The acceptance card states €5 for
the first kilogram and €3 for each additional started kilogram. The trusted check observes an
incorrect 1,200g quote, creates one local defect and shows evidence. Repeating the health loop
increments its occurrence count instead of creating ten tickets.

A bounded worker receives one clear correction task. The UI shows its scope and budget; it
does not display a fabricated confidence percentage as progress. Exported artifacts move to
verification. A trusted check suite tests boundary weights and invalid inputs. Hybrid policy
either makes the ordinary correction eligible or requests review if it touches critical pricing
code. The operator can inspect the precise rule and artifact.

After authorized merge/build/release, the preview displays the corrected quote and verified
version. The ticket closes under its resolution rule. The outcome records whether a person
repaired code or merely supplied mandatory approval. Synthetic/offline repairs remain labelled
and are excluded from real model-performance comparisons.

## Journey: sensitive PR

Mission Control shows “Human verification required: this changes a protected permission rule”,
the affected component and concrete diff. The review panel explains why size and AI score do not
remove this requirement. The authorized reviewer authenticates through the configured identity
step-up and approves the exact action. The client cannot submit a new SHA under an old approval.

If the identity integration is absent, the panel says what is missing and preserves the waiting
state. A demo approval control, if implemented, must explicitly say it is a local demonstration
and cannot unlock actions requiring real enterprise MFA.

## Journey: budget or telemetry problem

The user sees “Paused before a new request: remaining budget is reserved by unfinished work”,
with settled, held and uncertain amounts separately. They may wait, cancel eligible work or ask
an authorized owner to adjust the budget. Repeated clicking cannot create unaccounted dispatches.

For a telemetry gap, show “quality unknown” or “usage incomplete” rather than zero cost or a
perfect success rate. Explain whether work can safely continue under an approved fixed profile.
The system never recommends switching to an unapproved cheaper provider merely to clear a block.

## Journey: failed release

Show requested, admitted, applying, observed and health-verified stages. If the receiver response
is lost, show “deployment outcome unknown; reconciling” and disable duplicate apply. If health
fails, present the preapproved rollback path or a human recovery requirement. Keep current
observed version and last verified version distinct.

The operator's stop button requests cancellation across worker/egress/delivery scopes and shows
which components acknowledged. It does not instantly claim cleanup or erase charges. Failed
cleanup quarantines state and offers reviewed recovery instructions.

## Explainable decisions

Every blocked action includes one primary reason, supporting facts and the next permitted action.
Examples: missing repo authorization, stale checks, critical component, incompatible profile,
uncertain spend, unsupported isolation or expired approval. Optional model prose may explain a
reason code but cannot change it or hide the evidence.

Keep granular source/artifact IDs available for audit while presenting meaningful names by
default. Do not ask nonexperts to choose internal queue types, cryptographic algorithms or raw
provider JSON. Advanced operators can edit a proposed typed profile with validation and review.

## Accessibility and control ergonomics

Use text plus color for status, keyboard navigation, clear focus, semantic labels, readable
contrast and reduced-motion support. Confirm consequential scope changes on a concrete diff.
Ordinary inspection and safe reversible preview actions need no repeated confirmation ritual.

Keep “stop work” separate from “delete evidence”. Avoid a universal “approve all” button across
different artifacts/environments. For bulk low-risk work, the policy can preauthorize a bounded
scope; each individual action still has its identity and receipt. Human approval screens must
not expose secrets or encourage clicking through an unexplained score.

## Product acceptance

Test with a person unfamiliar with agentic tooling: can they launch the demo, identify why a
critical change is blocked, distinguish fake from real telemetry, stop a run, find a duplicate
ticket and understand what an approval authorizes? Observe completion/errors; do not invent a
usability percentage. A beautiful cockpit without these behaviors does not satisfy the product.
