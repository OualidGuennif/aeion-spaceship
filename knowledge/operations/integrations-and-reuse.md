---
type: Research
title: "All requested tools: reuse decisions and qualification contracts"
description: "Source-checked roles for Paperclip, OpenShell, Hindsight, ECC, both Anthropic collections, Graphify, Archify and Orca."
status: draft
---

# Integration and reuse decisions

Checked on **2026-10-23** using repository metadata, pinned README/licence bytes and selected
source files. Exact commits and inspected-file hashes are in
[upstreams.lock.json](../references/upstreams.lock.json). A source check is not a local integration
test or a security endorsement. No upstream installer, hook or agent fleet was started.

## Selection method

Evaluate added capability, overlap with Factory, deterministic enforcement surface, documented
extension stability, privilege/secret exposure, data exits, licence, operational weight and
measurable user benefit. Keep one accountable owner per function. Repository popularity and
marketing claims are not compatibility evidence. “Selected” means first to qualify, not production
approved. The minimum stack must work while optional tools are absent.

| Tool | Proposed use | First inclusion | Authority limit |
| --- | --- | --- | --- |
| Paperclip | Work/cockpit foundation, tasks, routines, adapters, accounting reuse | G1 integration spike | Agent task writes cannot authorize protected effects |
| OpenShell | OPS execution and credential mediation candidate | G1/G3 | Only controls demonstrated on the chosen release/platform |
| Hindsight | Scoped project memory | After core mission | Retrieved/generated facts cannot change policy |
| ECC | Selected development/research skills | Per-task qualification | No replacement of Factory or blanket hook install |
| Knowledge-work plugins | Company-specific business task packs | After coding path | Connectors require separate company capabilities |
| Official Claude plugins | Reviewed development/review/LSP capabilities | Selective | Curated listing is not a blanket trust or licence grant |
| Graphify | Local AST impact/context evidence | After trusted baseline | Incomplete graph cannot lower deterministic risk |
| Archify | Source-backed interactive architecture views | Cockpit documentation slice | Diagram receipt does not prove merge safety |
| Orca | Optional developer desktop/remote interface | Later optional client | No second policy authority or automatic host executor |
| Cloudflare audit skill | Structured source-audit workload, vendored in OPS | Intake design now; execution after OPS qualification | Finding schema/LLM verdict is not runtime proof |

## Paperclip: first foundation to qualify

**Observed:** a Node/React/PostgreSQL-oriented work platform with tasks, adapters, schedules and
governance. Selected source includes company-scoped accounting transactions, budget reservations
and admission checks. `accounting-transaction.ts` locks a company before accounting mutation.
The budget service rechecks held reservations and treats some unpriced/pending exposure as blocking.
The architecture docs describe adapters that can spawn local agent processes. These observations
do not prove every provider request is intercepted or expose a stable public admission API.

**Æion decision:** build a narrow SpaceShip policy/evidence layer around a qualified Paperclip
extension rather than recreate a task manager. Reuse task checkout, routines and accounting where
their actual path satisfies the contract. The cockpit may be an extension/projection of Paperclip
instead of a separate competing work UI. The exact extension seam is a G1 deliverable.

**Gate:** trace a real task from authenticated intake to worker dispatch, reservation, provider
call, settlement, cancellation and recovery. Verify which routes an agent can write; ensure it
cannot set verified release state, modify company policy or call a protected connector directly.
Review current private/remote deployment authentication and company scoping. Disable direct
host-local/process adapters on paths that require OPS isolation.

**API discipline:** do not import undocumented internal TypeScript functions as a product contract.
Prefer a supported external adapter/plugin seam; otherwise make a small reviewed upstream change
or maintain a narrowly pinned patch with upgrade tests. If financial admission cannot sit on the
actual dispatch path, do not claim a hard request cap. Select one canonical ledger; never charge
or reserve the same request independently in two systems.

**Fallback:** if the spike cannot preserve authority without a broad fork, keep Paperclip as an
optional work projection and implement the smallest Gate/work ledger needed for the proven local
mission. Record the failed reuse criterion and costs. Do not build both full products in parallel.

## NVIDIA OpenShell: runtime candidate

**Observed:** runtime policy enforcement, supervisor mediation and versioned backend contracts.
Current docs identify stable v0.1.5 and a platform support matrix. Source on the inspected default
branch is newer development material. The backend document distinguishes boundary opening,
confirmation and explicit start, and notes optional suspend/resume limitations. SDK and runtime
versions matter; default-branch features cannot be attributed to the stable binary automatically.

**Æion decision:** qualify the stable release named by OPS first. Keep runtime details in OPS,
with SpaceShip consuming a capability/evidence contract. Supply trusted manifests, image digests,
resource limits and endpoint grants; receive actual lifecycle/enforcement events. Never expose
the gateway's administrative credentials or host Docker socket to the workload.

**Gate:** execute OPS negative tests for filesystem, egress bypass, wrong API destination,
credential substitution/revocation, stale generation, process/resource limits, artifact promotion
and cleanup. Test the exact Apple Silicon/Linux host, Docker and harness versions. The previously
documented Claude API-key and OpenRouter/OpenCode profiles do not prove the requested Claude
subscription-token plus Claude/OpenRouter combination is already compatible.

**Failure:** unsupported required enforcement refuses launch. Audit-only networking is not an
enforcing profile. Avoid floating `main`/`dev` packages, implicit TUI approvals and automatic
policy suggestions. Maintain a stable-versus-development feature matrix and requalify upgrades.

## Hindsight: optional memory, outside authority

**Observed:** retain/recall/reflect operations and project memory banks. Retain uses an LLM for
extraction; reflect can generate reasoning-based responses. The repository supports self-hosting
and multiple model backends. Its README's isolation claims are not independent tenant tests.

**Æion decision:** use a company/project-scoped memory service only if measured task savings beat
plain Factory knowledge and bounded source retrieval. Start with approved summaries and provenance,
not automatic retention of every conversation. Store source revision, evidence identity, age and
confidence. Treat a recalled statement as a hypothesis until current source or trusted facts confirm it.

**Gate:** authenticate every bank access; test company separation, deletion/export, backup access,
secret/PII exclusion, stale memory and prompt injection. A bank name is not authorization. Include
retention/extraction/reflection model calls and infrastructure in total task cost. Verify whether
the selected self-hosted identity model meets the company's needs before enabling it.

**Failure:** memory outage falls back to approved source context when that is safe. Required audit,
policy and budget state never depend on memory recall. Automatic retention and learned policy
editing remain disabled. Expired or contradictory memories cannot override the source revision.

## ECC: selective capability library

**Observed:** a broad harness skills/rules/hooks/memory toolkit. The inspected tree contains
`skills/search-first`, `skills/verification-loop` and `skills/continuous-learning-v2`. Its guidance
warns against stacking installation methods. The verification skill includes generic commands,
grep examples and a sample coverage threshold; these are not repository-specific acceptance proof.

**Æion decision:** shortlist search/research and targeted verification guidance where it adds
information beyond Factory. Keep Factory as the fixed method. Configure actual project checks
from trusted project policy; do not copy a universal 80% line-coverage threshold or grep-based
“security pass” into merge authorization. Prefer native LSPs where they already work.

**Gate:** review one exact skill's instructions, hooks, commands, network effects and licence;
measure task quality/time/token benefit. Check collisions with existing Factory hooks and skills.
One project-local installation path, explicit activation, reproducible rollback. No global
installer or automatic “install everything” step.

**Failure:** optional guidance absence does not change permissions. Continuous learning and
instincts remain advisory proposals with provenance; they cannot rewrite deterministic policy,
verifier definitions or accepted knowledge without review. Keep learned content scoped and bounded.

## Anthropic knowledge-work plugins: business packs

**Observed:** file-based role plugins intended for Cowork and also described as Claude Code
compatible. They bundle skills, commands and connectors. The inspected collection includes
engineering and product-management; per-plugin licence files vary in presence. MCP connectors
can access external business systems and need their own trust analysis.

**Æion decision:** after the coding path works, let a company choose a task pack such as product
requirements or support triage. Bind inputs/outputs, data class, acceptance and capabilities to a
versioned task family. A business plugin can propose a software ticket; it cannot make its own
external messages, customer-data export or production change automatically authorized.

**Gate:** select the exact plugin/version, confirm licence and harness feature support, enumerate
connector actions and data destinations, and run benign/malicious task fixtures. Reconcile plugin
commands with company-specific systems rather than assume Cowork UI behavior exists headlessly.

**Failure:** connector or identity absence shows an unsupported capability. Do not silently use a
different app, shared user token or unapproved data exit. No role pack is mandatory for ParcelDesk.

## Anthropic official plugin directory: curated inputs

**Observed:** a curated directory including first-party and external plugins. The README directs
users to each plugin's relevant licence. The inspected PR review toolkit offers specialized
review roles; its outputs are model-assisted analysis, not deterministic acceptance evidence.

**Æion decision:** prefer a few useful capabilities: native language tooling when available,
targeted review and selected code assistance. Do not install every review role on every PR.
Choose review based on changed areas and independently measured detection value. Keep review
comments separate from Gate's check identity and human approval.

**Gate:** pin plugin and referenced remote components, review hooks/MCP endpoints, inspect
permissions and per-plugin licences, verify the harness actually loads/enables the capability,
and record its input/output/cost. Marketplace inclusion is not a transitive approval for future code.

**Failure:** a broken optional reviewer cannot fabricate success or weaken a mandatory check.
If required by policy, missing review blocks the action. Automatic marketplace sync must not
execute newly changed code inside an existing authorized run.

## Graphify: source graph with explicit provenance

**Observed:** local tree-sitter AST extraction for code; optional semantic extraction for docs/
media may call a model. The project distinguishes these modes and includes source graph tooling.
Static parsing does not imply complete behavior for dynamic calls, generated code or runtime wiring.

**Æion decision:** use an explicitly local AST-only profile to reduce repeated source exploration
and identify candidate impact relationships. Bind graph to repository revision, file inventory,
parser/tool version and extraction mode. Tag edges as syntactic/resolved versus inferred.
Sensitive-path rules remain authoritative even when no graph edge is found.

**Gate:** test language coverage, parser failures, stale/incomplete graph handling, symlinks,
dependency/config boundaries, bounded cache/artifacts and absence of unintended backend calls.
Measure time/tokens and missed dependencies on representative tasks. Optional document semantic
processing needs separate data/budget authorization.

**Failure:** stale or partial results increase uncertainty and review requirements. They never
prove that a tiny PR cannot affect a critical component. Context retrieval is optional to Gate.

## Archify: explain the system, preserve facts

**Observed:** typed diagram authoring and interactive HTML views, including repository-backed
source evidence and architecture delta views. Its README explicitly distinguishes authored delta
comparison from inferred impact/risk/merge safety. Repository evidence binds source identity.

**Æion decision:** expose architecture, authority boundaries and release-flow diagrams in Mission
Control using reviewed source-backed facts. Show revision, generation time, evidence and unknowns.
Use the tool to help a nonexpert understand a blocked action or proposed change, not classify it safe.

**Gate:** validate typed input and receipts, verify cited ranges at the exact commit, review
generated HTML/script behavior, and sanitize names/links. Serve interactive artifacts in an
isolated origin/sandbox rather than granting arbitrary generated HTML the cockpit's session origin.
Check that diagrams do not disclose private source paths or sensitive topology when exported.

**Failure:** an absent diagram does not block an otherwise qualified action unless the company's
review contract explicitly requires it. Diagram freshness is visible; no invented runtime edge.

## Orca: optional developer client

**Observed:** developer desktop features include parallel worktrees, terminals, GitHub/Linear
views, remote worktrees and mobile companion features. A Git worktree separates source state;
it does not establish an OS sandbox. No supported SpaceShip control API was established here.

**Æion decision:** offer Orca as an optional developer experience for inspecting branches, PRs
and runs after a safe integration seam is identified. Keep Mission Control as the company's
authoritative approval surface. Prefer links/read-only projection first. Do not run Paperclip
and Orca as two independent schedulers with overlapping write credentials.

**Gate:** trace actual process launch, credential inheritance, remote/mobile identity and exposed
ports; prove all protected effects still traverse Gate. Validate an extension rather than assume
an API from a README. Default remote/mobile connectivity remains off in the first local release.

**Failure:** the client may be unavailable without affecting task authority or durable state.
An action performed manually outside SpaceShip is recorded as external activity, not retroactively
claimed as governed autonomous delivery.

## Minimum deployable composition

For the first qualified local path, aim for the selected Paperclip app/store, Gate module/service,
trusted runtime controller and one disposable worker. Add a collector only as needed for the
required evidence/telemetry contract. Reuse an existing observability backend; do not require
Langfuse, Hindsight, a graph store, Temporal and a queue cluster just to run one mission.

Optional integrations ship as versioned profiles with prerequisites, scopes, data exits, failure
behavior, tests and uninstall/rollback instructions. The default installation must not activate
external connectors, provider calls or auto-merge merely because their software is present.
