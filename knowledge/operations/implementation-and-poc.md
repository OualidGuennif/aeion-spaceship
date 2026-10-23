---
type: Plan
title: "Implementation sequence, ParcelDesk POC and release gates"
description: "Concrete work packages, stack choices, vertical demonstration and 64 planned acceptance scenarios for progressive qualification."
status: draft
---

# Build plan and acceptance gates

This is an implementation backlog, **not completed product code**. The owner requested a large
plan. No runtime acceptance result below is claimed executed. Start with the smallest vertical
mission and expand only when the preceding gate's evidence supports it.

## Implementation baseline

Prefer TypeScript/Node and the selected Paperclip UI/backend conventions for a thin integration;
reuse React and PostgreSQL where that stack is actually selected. Freeze source/dependency
versions during G1. Do not add a second frontend framework, general workflow engine, message
broker or new identity server for the first mission. A pure typed evaluator, explicit database
transitions and outbox are sufficient until demonstrated otherwise.

Keep action authorization behind receiving interfaces, independent of agent adapters. A unit
test can exercise the pure decision function with no network or LLM. Integration tests exercise
actual transaction/receiver behavior. Runtime negative checks use disposable isolated fixtures.
The first offline demonstration can use deterministic fake adapters; their receipts are typed as
simulation and must never be accepted by the live effect path.

## Work packages and dependencies

| ID | Work package | Concrete output | Depends on / stop condition |
| --- | --- | --- | --- |
| WP01 | Freeze owner scope and threat model | Company boundaries, roles, first host, retained auth paths | This plan; unresolved high-impact scope stops live work |
| WP02 | Compile typed contracts | Schemas, reason-code registry, version/unknown-field rules | WP01; examples must validate and stay inactive |
| WP03 | Paperclip extension spike | Trace and test actual supported integration seam | WP02; no assumed internal/public API equivalence |
| WP04 | Accounting/dispatch spike | One authoritative reservation/settlement/recovery path | WP03; no competing ledgers or unmediated provider calls |
| WP05 | Runtime qualification harness | Versioned OpenShell/Docker profile + OPS evidence | WP01; required unsupported control refuses launch |
| WP06 | Pure policy evaluator | Replayable manual/hybrid/autonomous decisions | WP02; deny precedence and critical-code tests |
| WP07 | Protected state and outbox | Transitions, journal, idempotency and reconciliation | WP03/04/06; crash/race evidence |
| WP08 | ParcelDesk source fixture | Small website, reproducible functional defects, external checks | WP02; no real data or credentials |
| WP09 | Offline mission runner | Finding → local ticket → candidate → checks → preview intent | WP06–08; simulation identities cannot unlock live effects |
| WP10 | Mission Control vertical UI | Onboarding, mission timeline, reason, budget and stop | WP09; nonexpert journey review |
| WP11 | Subscription auth qualification | Operator enrollment + bounded isolated Claude task | WP05; unsupported mediation explicitly labelled |
| WP12 | API auth qualification | OpenRouter and selected DeepInfra profile tests | WP05; exact model/protocol/parameter support required |
| WP13 | Real coding worker | One Factory-guided issue, bounded patch export and checks | WP07/11 or12; paid test envelope explicitly set |
| WP14 | GitHub App intake/outbox | Scoped demo repo, HMAC/dedup, issue create/reconcile | WP07/09; no writes to arbitrary repositories |
| WP15 | PR/check connector | Exact head/base facts, trusted CI identity and review evidence | WP14; stale or incomplete facts block eligibility |
| WP16 | Identity and approval | Existing IdP step-up, action binding and replay rejection | WP15; missing required assurance blocks action |
| WP17 | Merge service | Scoped expected-head merge and final-state observation | WP15/16; no bypass role |
| WP18 | Trusted build and local target | Digest-bound build/release/health receipt and recovery | WP05/17; no untrusted host execution |
| WP19 | Observability joins | Native telemetry, ledger projection, interventions/outcomes | WP13/18; coverage and unknowns visible |
| WP20 | Profile experiments | Fixed baseline, shadow evaluation, bounded canary | WP19; mature representative quality/cost/time evidence |
| WP21 | Optional context tools | Qualified Graphify, then Hindsight if useful | Core mission accepted; measured benefit exceeds overhead |
| WP22 | Optional plugin/diagram/client packs | ECC/Anthropic selections, Archify, later Orca seam | Per-tool qualification and rollback; no blanket install |
| WP23 | Audit and maintenance | CROA export, Cloudflare intake, weekly upstream routine | WP07/19; explicit partial coverage and scheduler evidence |
| WP24 | Company distribution | Install/upgrade/backup/incident/support matrix | Prior applicable gates; no unsupported production badge |

WP11 and WP12 preserve both requested authentication options. One may be qualified before the
other, but the release must state the support status of each. Do not call the unsupported path
implemented. A company requiring credential isolation cannot accept a restricted exposed-token
profile as equivalent. DeepInfra is an additional API qualification, not a silent replacement.

## G0 — design ready for implementation review

Inputs: this researched plan, pinned source register, inactive examples and OPS Cloudflare copy.
Outputs: accepted authority boundaries, contracts, first demo and explicit unresolved integration
questions. Required review focuses on product scope and risk, not permission to execute arbitrary
production actions. Local/read-only design work requires no provider budget or external account.

## G1 — reuse and boundary feasibility

Prove the Paperclip extension with a disposable installation. Inspect actual requests and state
ownership. Show that an agent can submit work but cannot approve a release, change Gate policy
or bypass financial admission. Verify the chosen database/extension/migration path. Record any
narrow patch and its upgrade burden.

Qualify the selected OpenShell stable release on the declared local Docker host. Confirm which
controls are native and which need a trusted outer component. Report unsupported requirements.
If core reuse fails, make one explicit fallback decision; do not accumulate a half-integrated
Paperclip stack plus a second full homegrown platform.

## G2 — ParcelDesk offline demonstration

**Product:** a shipping-price website with a weight input and a quote. Currency is integer EUR
cents; inputs use integer grams. The contract is €5 for the first kilogram and €3 for every
additional started kilogram, from 1g through 30,000g. Invalid input is rejected. No payments,
customer records, shared production database or external delivery service is involved.

| Fixture | Defect / action | Expected policy result |
| --- | --- | --- |
| PD01 | Rounding uses completed rather than started extra kilograms; 1,200g returns €5 instead of €8 | Reproduced bug; pricing is critical business code, so hybrid requires the configured owner/step-up |
| PD02 | Ordinary help/label text violates an explicit UI acceptance check | Low-risk bounded change can become eligible under hybrid after trusted checks |
| PD03 | A proposed repair also edits permission policy or privileged CI | Separate authority required regardless of size/AI score |
| PD04 | A forged success log refers to another candidate | Deny stale/untrusted evidence |
| PD05 | Same defect observed by two overlapping loops | One canonical local ticket, two observations |
| PD06 | Provider fixture returns no final usage after cancellation | Retain uncertain exposure and block new unadmittable work |

Use independently maintained boundary tests: 1, 1,000, 1,001, 1,200, 2,000, 2,001 and 30,000g;
zero/negative/too-large/noninteger values; malformed requests. The agent cannot rewrite this
external acceptance contract to make the bug disappear.

The first offline run may use a prewritten correction and synthetic profile/usage records. Label
them explicitly. PD02 proves the automatic local preview path; PD01 proves a critical change stays
blocked until the later qualified approval path. Simulation of an MFA receipt is permitted only
in tests and cannot authorize a real merge/deploy. Do not report this as model autonomy or real
provider optimization.

## G3 — bounded real coding

Use one disposable source repo, one worker, one task and an owner-set paid exposure envelope.
The harness uses Factory instructions inside OPS. Capture real source/artifact/check identities,
resource/cleanup and provider usage. Test both retained auth paths and document limitations.
The coding worker has no GitHub merge/deploy credential. Source patches still go through trusted
verification. Do not widen concurrency just to produce a busier dashboard.

## G4 — real GitHub demo

Create a dedicated repository such as `aeion-spaceship-demo` under an explicitly selected owner;
never test against the nine upstream projects. Install the App only there. Enable issue/PR
features and required checks supported by the account. A plan-tier limitation is visible and
must not be bypassed through an administrator token.

Demonstrate repeated findings creating one issue, a real branch/PR, correct `Fixes #N` linkage,
delivery reconciliation, a rejected stale head and a denied untrusted check. Confirm actual
remote state before declaring the effect delivered. No production repository participates.

## G5 — approval, merge and delivery

Demonstrate all three PR modes on the same deterministic fixtures. Configure a real identity
step-up for actions requiring it. Prove approval replay, changed source, wrong environment and
role revocation fail. Merge through the receiving scope and observe the resulting commit.

Build the exact approved source in a trusted isolated path, deploy a digest to local preview,
verify version and behavior, then exercise lost-response recovery and a health failure. Prove a
stale worker cannot overwrite a newer target. No irreversible migration is included in v0.

## G6 — performance evidence

Use the Observability contract with complete attempts/cost/interventions and mature acceptance
outcomes. Run a representative corpus under a fixed baseline, then shadow candidates. Publish
uncertainty and comparable cohorts. Only an explicitly approved bounded canary can alter real
assignments. A synthetic chart or model self-score cannot pass this gate.

## G7 — company installation

Package supported combinations, protected identity/policy, credential setup, backup/restore,
upgrade ordering, diagnostics and incidents. Validate a clean install and a restore with external
writes initially disabled. Test the nonexpert journey. Document operational owners and support
limits. An enterprise pilot remains scoped; it is not a universal security/compliance claim.

## Planned acceptance matrix — 64 scenarios

These IDs are requirements for future tests. **None is claimed run in this planning release.**

| ID | Scenario | Required observation |
| --- | --- | --- |
| A01 | Identical normalized facts/policy replay | Identical decision/reason digest |
| A02 | Unknown field / malformed schema | Refusal before effect |
| A03 | Agent proposes wider path/network grant | Effective authority unchanged |
| A04 | Child grants individually fit but union exceeds parent | Shared admission refuses excess |
| A05 | Wrong company/repo identity | No data or receiver access |
| A06 | Expired/revoked policy | New action refused |
| A07 | Control-policy PR attempts self-approval | Separate authority required |
| A08 | Clock/random/network changes during replay | Recorded inputs used; no hidden nondeterminism |
| W01 | Crash before transition commit | No authority/effect exists |
| W02 | Crash after commit before send | Outbox recovers with revalidation |
| W03 | Lost response after external mutation | Unknown then reconciled; no blind duplicate |
| W04 | Two workers claim one task | One valid lease/generation |
| W05 | Old worker acts after lease expiry | Receiver rejects stale generation |
| W06 | Journal unavailable | Protected transition blocked |
| W07 | Out-of-order/duplicate event delivery | State converges without backward transition |
| W08 | Restore old database snapshot | Past approvals/effects cannot replay automatically |
| T01 | Same finding from concurrent loops | One canonical ticket and multiple observations |
| T02 | Similar symptoms, distinct root causes | No silent false deduplication |
| T03 | Issue-create response lost | Marker/receiver reconciliation before retry |
| T04 | Bad webhook HMAC or wrong installation | Rejected before processing |
| T05 | Loop flood/rate limit | Bounded queue, backpressure, visible deferred work |
| T06 | Confidential security finding | Private intake; no public secret/exploit body |
| T07 | Unresolved hypothesis / partial audit | No confirmed severity or complete-coverage badge |
| T08 | Closed defect recurs on changed source | Explicit revalidation/reopen evidence |
| P01 | Tiny low-risk change, trusted current checks | Hybrid eligible within scope |
| P02 | One-line critical business rule | Required owner/step-up in hybrid |
| P03 | High AI score plus failed/forged checks | Refused |
| P04 | Rename from protected to ordinary path | Protected old path still governs |
| P05 | Truncated diff / unknown file mode | No automatic eligibility |
| P06 | Head/base/policy changes after approval | Approval invalidated |
| P07 | Replayed/wrong-action/expired MFA receipt | Refused transactionally |
| P08 | Autonomous profile but native GitHub gate blocks | No bypass; reason visible |
| R01 | Host socket/home/SSH access attempt | Denied outside declared scope |
| R02 | Direct-IP/DNS/IPv6/metadata/redirect egress | Denied by actual outer boundary |
| R03 | Wrong-endpoint credential request | No credential substitution/leak |
| R04 | Expiry/revocation with existing stream | Qualified stop/reconciliation behavior |
| R05 | CPU/RAM/PID/disk/output/deadline exhaustion | Bounded termination and evidence |
| R06 | Cross-run workspace/memory/cache read | No unintended access |
| R07 | Symlink/hardlink/traversal artifact export | Trusted promotion rejects |
| R08 | Failed cleanup / unsupported enforcement | Quarantine/refuse; no silent downgrade |
| D01 | Mutable tag changes after approval | Digest binding prevents substitution |
| D02 | Untrusted build script seeks release secrets | No privileged credential access |
| D03 | Wrong OIDC repository/workflow/environment | Target refuses credential/action |
| D04 | Concurrent target updates | Generation conflict prevents stale overwrite |
| D05 | Deployment accepted but old version serves | Outcome remains unverified |
| D06 | Lost apply/rollback response | Observe/reconcile target before new effect |
| D07 | Health fails and rollback supported | Approved rollback observed and verified |
| D08 | Irreversible migration proposed | Explicit gate; no fake code-only rollback |
| O01 | Concurrent requests approach remaining cap | Atomic exposure admission |
| O02 | Duplicate usage frame versus billable retry | One charge per actual attempt, no lost retry cost |
| O03 | Interrupted stream / unknown spend | Uncertain hold retained |
| O04 | Cache/reasoning token category overlap | No double counting |
| O05 | Required human approval versus code repair | Governance wait and corrective help separated |
| O06 | Missing intervention/outcome coverage | Quality unknown; no fabricated success |
| O07 | Unsupported provider parameter/fallback | Profile refused; no silent downgrade |
| O08 | Candidate quality/privacy regression | Stop promotion/canary; bounded compatible recovery |
| U01 | Nonexpert launches offline demo | Understandable contract/status, no hidden paid call |
| U02 | Local demo receipt reaches live connector | Rejected by trust class |
| U03 | Hindsight/graph suggests weaker policy | No authority change |
| U04 | Stale graph/diagram or optional tool outage | Explicit unknown/fallback; no safety inference |
| U05 | Weekly upstream check overdue or network failed | Maintenance ticket; no false timestamp refresh |
| U06 | Upstream adds executable file/schema change | Full inventory/diff and requalification before promotion |
| U07 | Operator stops run | Request/acknowledgement/cleanup and uncertain cost visible |
| U08 | Evidence/support export | Scoped sanitized data; no credentials/default content leak |

SS-01/08/11 map primarily to A/P/U; SS-02/07/12 to A/W/R/D; SS-03/04/06/10 to W/P/D;
SS-05/09/13 to O/P; SS-14 to U and the release support matrix. These groupings do not replace
the detailed per-test source/control mapping required when implementation starts.

## Definition of a releasable slice

Each slice has source/version identity, one coherent user behavior, positive/negative evidence,
documented limits, recovery and an owner-reviewed result. Runtime tests run in the qualified
boundary; tests that require an absent account/credential remain unverified. No integration is
“done” because its logo appears in the cockpit. Stop expansion when the vertical mission is not
reliable; fix root causes before adding more models, agents or UI screens.
