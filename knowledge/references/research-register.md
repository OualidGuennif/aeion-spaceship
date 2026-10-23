---
type: Research
title: "Source register and evidence limits"
description: "Primary repositories, exact source revisions, official control-plane documentation and local Æion inspection scope."
status: draft
---

# Research register

Checked **2026-10-23**. Use [upstreams.lock.json](upstreams.lock.json) for full commits and hashes.
The ten repository default branches were resolved through GitHub metadata, their trees inspected,
and selected files downloaded at immutable commits. **82 retrieved source files** were checked
against Git blob identities and fingerprinted with SHA-256. Semantic inspection was selective;
this is neither a complete code audit nor a proof that a published binary matches those bytes.

## Requested repositories

| ID | Primary source / pin | Checked capability and important limit |
| --- | --- | --- |
| R01 | [Hindsight](https://github.com/vectorize-io/hindsight/tree/80591c20b43473baf1647fd9ed8c5992d9803ea1) | Retain/recall/reflect, LLM extraction, banks, deployment model; isolation remains to be qualified |
| R02 | [Paperclip](https://github.com/paperclipai/paperclip/tree/412914cfa78d5abefcc34d3eb8d4bb86e461caac) | Work platform, adapters, governance; selected accounting and reservation source inspected |
| R03 | [ECC](https://github.com/affaan-m/ECC/tree/90606c8315ee09cafc303515c5f33024db6b9882) | Skills/hooks/memory; selected research and verification guidance, not a security boundary |
| R04 | [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell/tree/9a85667d0d87e8131b64351ec1fc4eb26e7bb865) | Supervisor/runtime source and backend protocol; default branch differs from stable release |
| R05 | [Knowledge-work plugins](https://github.com/anthropics/knowledge-work-plugins/tree/33d3dea41a341b341d4f5da2e8801ae0c89be2b8) | Cowork/Claude Code role packs; per-plugin connectors/licences need review |
| R06 | [Official Claude plugins](https://github.com/anthropics/claude-plugins-official/tree/465f09344424225c25d438f2e052732c3d688d2f) | Curated first/external plugin directory; per-plugin licence and privilege scope |
| R07 | [Graphify](https://github.com/Graphify-Labs/graphify/tree/c588b72d936927790a87ad009955078ed40562a3) | AST-only/local versus semantic/model paths; graph completeness not established |
| R08 | [Archify](https://github.com/tt-a1i/archify/tree/25cf37080fc8b1dbe758a4efc3935b55f3327083) | Typed source-backed diagrams/deltas; no inferred merge-safety authority |
| R09 | [Orca](https://github.com/stablyai/orca/tree/f9e883a4bfa666635f28e72d37d5f249e3703d41) | Worktrees/desktop/remote/mobile; worktree is not OS isolation; SpaceShip API seam unknown |
| R10 | [Cloudflare security-audit-skill](https://github.com/cloudflare/security-audit-skill/tree/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8) | Complete 22-file snapshot in OPS; skill, schema, validators and tests preserved |

Repository metadata reported MIT for R01/02/03/08/09/10 and Apache-2.0 for R04/05/06/07.
This is **not a blanket licence statement for every nested component or linked service**. Root
licence bytes were retrieved; selected plugin licences were checked. Review exact component terms
before redistribution/installation. Upstream authors retain their licences and trademarks.

### Paperclip source supporting reuse

- [Architecture documentation](https://github.com/paperclipai/paperclip/blob/412914cfa78d5abefcc34d3eb8d4bb86e461caac/docs/start/architecture.md): stack and adapter model.
- [Accounting transaction](https://github.com/paperclipai/paperclip/blob/412914cfa78d5abefcc34d3eb8d4bb86e461caac/server/src/services/accounting-transaction.ts): company-scoped serialization and read snapshots.
- [Budget service](https://github.com/paperclipai/paperclip/blob/412914cfa78d5abefcc34d3eb8d4bb86e461caac/server/src/services/budgets.ts): pending/unpriced exposure and admission logic.
- [Reservations](https://github.com/paperclipai/paperclip/blob/412914cfa78d5abefcc34d3eb8d4bb86e461caac/server/src/services/budget-reservations.ts): pre-dispatch checks, cancellation/ownership and retained holds.
- [Connection threat model](https://github.com/paperclipai/paperclip/blob/412914cfa78d5abefcc34d3eb8d4bb86e461caac/doc/connections/SECURITY-THREAT-MODEL.md): additional review input; no deployed assurance inferred.

Some high-level docs summarize accounting as reported spend/pauses, while current source contains
more detailed reservation mechanisms. The plan uses source evidence rather than concluding from
the summary that Paperclip has no reservations. End-to-end integration still needs runtime tests.

## Official controls and protocols

| ID | Source | What it supports |
| --- | --- | --- |
| R11 | [GitHub issue REST API](https://docs.github.com/en/rest/issues/issues#create-an-issue) | Issue creation/permissions; no assumed create idempotency key |
| R12 | [GitHub webhook validation](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries) | Raw-body signature verification before processing |
| R13 | [GitHub App installation tokens](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app) | Short-lived installation authentication and narrowed repository/permission scope |
| R14 | [GitHub PR REST API](https://docs.github.com/en/rest/pulls/pulls) | Expected-head SHA on merge, conflicts and observed results |
| R15 | [Required checks troubleshooting](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks) | Current SHA, check source and merge-group trigger concerns |
| R16 | [Protected branches](https://docs.github.com/en/enterprise-cloud%40latest/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | Review/check/update/merge protection; installation availability must be checked |
| R17 | [Ruleset rules](https://docs.github.com/en/enterprise-cloud%40latest/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets) | Stale reviews, code owners and merge queue configuration |
| R18 | [Deployment environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) | Reviewers, self-review setting, branch rules and plan/visibility restrictions |
| R19 | [GitHub OIDC](https://docs.github.com/en/actions/concepts/security/openid-connect) | Workload identity and restricted cloud trust relationships |
| R20 | [Secure use of pull_request_target](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target) | Privileged workflow dangers when executing untrusted PR code |
| R21 | [OPA introduction](https://www.openpolicyagent.org/docs) | Separation of policy decisions and enforcement; optional future engine |
| R22 | [Temporal workflows](https://docs.temporal.io/workflows) | History/replay model and deterministic workflow requirements |
| R23 | [Temporal activities](https://docs.temporal.io/activities) | External effects and idempotency needs despite workflow replay |
| R24 | [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html) | Identity claims and authentication context/freshness mechanisms; IdP mapping must be qualified |
| R25 | [WebAuthn Level 3](https://www.w3.org/TR/webauthn-3/) | Standard public-key authentication; no new custom cryptographic protocol proposed |
| R26 | [OpenShell support matrix](https://docs.nvidia.com/openshell/v0.1.5/about/support-matrix) | Stable release/platform/kernel qualification surface |
| R27 | [OpenShell security controls](https://docs.nvidia.com/openshell/v0.1.5/security/best-practices) | Enforcement layers, audit/enforce distinction and credential/network controls |
| R28 | [OpenRouter provider routing](https://openrouter.ai/docs/guides/routing/provider-selection) | Provider preferences and parameter/route constraints; no task budget guarantee |
| R29 | [DeepInfra reasoning](https://docs.deepinfra.com/chat/reasoning) | Model-dependent reasoning controls; exact protocol/profile qualification required |

Versioned OpenShell paths above replace floating documentation where appropriate. During research,
current extensionless docs identified v0.1.5; an older `.html` search result carried an alpha warning.
Do not mix that stale presentation with the current stable support statement. Before implementing,
re-resolve the selected release and review its own source/evidence rather than rely on a search cache.

## The four Æion projects inspected locally

| Project | Concrete material inspected | Consequence for SpaceShip |
| --- | --- | --- |
| Factory | AGENTS, loop launcher, issue protocol, Decisions API README, loop operations; local HEAD `805b7955ec408fcdec6d07b0267bf8a53c0f23c6` | Existing issue labels/loops reused; launcher still invokes model reasoning and is not the enterprise authority layer |
| Agentic OPS | README, 16-control component proposal, research and current work | Runtime remains unimplemented/unqualified; SpaceShip consumes its acceptance contract |
| CROA | Public audit-kit README/credits; local HEAD `bb9fd43d1328bd5714ec9973bb8f7c017a729fba` | Assessment CLI/packets are not a deployed CROA runtime |
| Observability | AGENTS and bounded control-loop contract; existing telemetry/provider/quality specification set | Reuse task outcomes, honest usage and observe/shadow/canary progression |

The [public Factory baseline](https://github.com/OualidGuennif/aeion-factory/tree/00fdbd0757b8ed3e08e71fa335de851234423c74)
differs from the local inspected branch. Do not attribute local source behavior to that public
commit without checking it. The [CROA audit kit](https://github.com/OualidGuennif/aeion-croa)
already pins the upstream v1.0.1 specification and records licensing/credits.

Original CROA references: [project](https://github.com/CROA-Project/CROA),
[requested version](https://github.com/CROA-Project/CROA/tree/v1.0.1),
[website](https://www.croaframework.org/), [DOI](https://doi.org/10.5281/zenodo.22310276).
The upstream pin and attribution were re-read from the local kit; website/release-page retrieval
was unsuccessful in this research session. No fresh whole-specification review is claimed here.

## Open questions that need implementation evidence

1. Which supported Paperclip extension seam permits external OPS execution and authoritative
   per-request accounting without a broad fork or unmediated fallback?
2. Which exact stable OpenShell/harness configuration qualifies both requested authentication
   paths, including secret isolation and revocation? Does the chosen host meet all controls?
3. What check/protection features are available on the user's eventual GitHub account/repositories?
4. Which enterprise IdP supplies sufficient fresh assurance and action/role binding?
5. Which provider profile can support defensible exposure, parameter application and reconciliation?
6. Do Graphify/Hindsight/plugin additions improve representative outcomes enough to justify cost,
   data exposure and operational weight?

These are release gates, not excuses to leave the design ambiguous. The plan specifies how to
resolve each one in a bounded spike before enabling affected behavior. No paid model call,
upstream installer, runtime qualification or enterprise deployment was performed. The runtime
GitHub ticket/PR adapters were not exercised; documentation PRs and module publication are
separate maintenance work.
