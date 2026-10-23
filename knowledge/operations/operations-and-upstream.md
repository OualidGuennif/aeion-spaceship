---
type: Runbook
title: "Operating and maintaining a company installation"
description: "Ownership, weekly upstream checks, compatibility promotion, backups, incidents and support lifecycle."
status: draft
---

# Operations and upstream maintenance

## Ownership and service boundaries

Each installation names a policy owner, security/runtime maintainer, repository owner, release
owner and incident contact. One person may hold multiple roles in a local demo; that does not
demonstrate separation of duties. Protected production policies can require independent roles.

Maintain an inventory of controller, runtime, harness, database, plugins, model/provider profiles,
identity and targets with versions, scopes, owner and last qualification. Distinguish the product's
supported baseline from optional integrations the company enabled. Default external effects remain
off until the installation completes its applicable gates.

## Mandatory upstream watch

Check the designated upstreams **at least once every seven days**. Cloudflare's complete snapshot
and executable read-only checker live in OPS; its runbook is the authoritative procedure for that
copy. Check the other selected tools on the same cadence, with immediate review of relevant
security notices. A weekly routine is proposed here; no background scheduler has been installed.

| Check | Evidence | Result handling |
| --- | --- | --- |
| Default branch and release/tag state | Observed commit/tag, retrieval time and identity | New version becomes a proposal, never automatic execution |
| Licence/notices | Exact changed files and component scope | Block promotion when redistribution/use terms are unresolved |
| Execution surface | Install hooks, MCP/connectors, network and credential changes | Re-run affected threat/qualification tests |
| Data/parameter contract | Schema, SDK/API and telemetry changes | Replay versioned fixtures; no silent field dropping |
| Security advisories | Available official notice and affected scope | Triage urgency and containment; absence is not proof of safety |
| Compatibility | Pinned source and release/runtime/harness matrix | Promote only the concrete qualified combination |

An owner records successful check time and next deadline in protected maintenance state. Failed
requests, offline file verification and a cached dashboard do not renew freshness. Missed checks
raise one maintenance ticket and block promotion of newly changed profiles; avoid an automatic
production outage solely because a research document is old.

## Update workflow

Resolve an immutable candidate, stage it in quarantine, compare the complete tree and notices,
review code/instructions, test the affected controls, publish an owner-approved profile and keep
a compatible rollback pin. A new README claim does not prove the deployed binary supports it.
For OpenShell, keep stable release documentation separate from default-branch development features.
For plugins, pin referenced external components too rather than only the marketplace directory.

Use a deduplicated maintenance ticket keyed by upstream and candidate revision. Group harmless
documentation changes only when it reduces review cost without hiding execution changes. Record
rejected updates and reasons. Do not silently advance a pin because a release is newer.

## Startup, health and shutdown

Startup preflights identity, policy validity, DB migrations, required journal, runtime support,
credential mediator and receiver scope. Read-only inspection may remain available while work is
blocked. Do not start new provider dispatch or protected effects with missing required controls.

Health checks separate liveness from readiness and specific capability readiness. The cockpit can
be alive while GitHub writes are unavailable. Expose queue depth, oldest pending/unknown effect,
lease recovery, budget reconciliation, audit gaps, worker cleanup and profile expiry.

Graceful shutdown stops admission, drains or cancels under policy, persists outstanding intents,
revokes applicable access and records unresolved effects/charges. Restart reconciles before
reissuing mutations. A process restart is not a fresh authorization or an empty budget window.

## Backups and restore

Back up policy, protected journal, accounting/outbox state and required artifacts through a
documented encrypted access path. Do not include live secrets in a support bundle. A database
backup alone may not include external artifacts or identity configuration; inventory the full
restore dependency set.

Define company-specific recovery point/time objectives rather than invent universal values.
Test restore into an isolated environment with external writes disabled. Reconcile outstanding
effects against live receivers before re-enabling them. Prevent restored old leases, consumed
approvals or outbox items from reauthorizing past actions. Revalidate policy expiry, credentials
and current target generations after restore.

## Incident procedures

| Incident | Immediate response | Evidence needed before resume |
| --- | --- | --- |
| Suspected workload escape/exfiltration | Stop admission/egress, revoke affected access, quarantine | Boundary/root cause and clean rebuild evidence |
| Unknown merge/deployment outcome | Freeze conflicting effects, observe/reconcile receiver | Confirmed source/target state and next authorized action |
| Unpriced/unreconciled spend | Stop affected paid dispatch; retain holds | Provider/ledger reconciliation or owner-scoped exception |
| Identity/policy compromise | Revoke affected authority, stop protected actions | Restored trust root, independent policy review and audit |
| Journal failure | Block protected transitions | Durable service recovered and gaps understood |
| Optional analytics failure | Stop learning; fixed allowed baseline if eligible | Telemetry integrity/coverage restored before promotion |
| Contaminated workspace/cleanup failure | Quarantine; no state reuse | Independent lifecycle cleanup verification |

Do not let the suspected compromised workload gather its own secrets or declare the incident
resolved. Preserve source identities and uncertain states. Security-sensitive findings stay out
of public issue bodies unless the owner explicitly approves a sanitized disclosure.

## Support and product lifecycle

Publish support per OS/runtime/harness/auth/provider/target combination. Experimental profiles
remain labelled and cannot inherit the stable profile's badge. Document upgrade ordering and
rollback compatibility; controller/runtime protocol mismatches should fail admission explicitly.

Provide a support export containing sanitized versions, policy digests, reason codes and bounded
event IDs, with user preview. Exclude prompt/source content and credentials by default. Removal
instructions stop workers, revoke App/target access and explain retained audit/data obligations.
Do not delete evidence simply to make uninstall look complete.
