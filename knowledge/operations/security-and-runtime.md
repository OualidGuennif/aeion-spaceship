---
type: Design
title: "Zero-trust agent execution and protected control plane"
description: "Threat model, trusted computing base, credential and network boundaries, supply chain and concrete enforcement gates."
status: draft
---

# Security and runtime

## Threat model and limits

Treat repository source, dependencies, install scripts, issue/PR text, model outputs, tools,
plugins, retrieved memories and exported artifacts as potentially malicious. A coding agent can
be induced to run attacker instructions or can simply make a mistake. The runtime must remain
safe even if the model entirely disregards the prompt.

Protect the host, other company projects, credentials, source/data, policy and audit state,
financial budget and delivery targets. Also consider compromised operator accounts, controller
bugs, malicious plugins, mistaken company policy, dependency compromise and a stale worker after
lease loss. Deterministic code is part of the trusted computing base and needs security review.

No claim of perfect security is made. Ordinary Docker shares a kernel boundary; a worktree is
only source-state isolation. For hostile code or unrelated users, require the stronger boundary
qualified by OPS for that threat model. A local one-user POC is not proof of multi-tenant safety.

## Trusted computing base

Keep the policy/effect service, identity integration, accounting path, runtime supervisor,
artifact promotion, trusted verifier definitions and release receiver outside workload writes.
Inventory their versions and privileges. Limit component count: each new service/plugin expands
the review surface and creates update/recovery work.

The cockpit is not a security boundary by itself. Every receiver authenticates scope and action
server-side. A hidden UI button or a model told “do not deploy” cannot replace a missing permission
check. Agent-facing APIs expose proposal/submission operations, not generic SQL/status setters or
arbitrary authenticated proxy calls.

## Local-first installation

Bind administrative UI/API to loopback for the POC. Do not enable remote/mobile access or create
a public tunnel automatically. Protect browser mutations against cross-origin requests and DNS
rebinding with appropriate host/origin/session controls. A local unauthenticated prototype must
not be advertised as a company authentication solution.

The controller may need Docker administration; the workload must never receive the Docker socket,
host home, SSH agent, cloud configuration, identity session or controller credentials. Stage an
approved source revision into disposable state. Do not run repository setup on the host to make
the sandbox convenient. Dependency downloads occur only in a separately bounded setup phase.

Every company install has its own identity/policy/credential boundary. Sharing a laptop directory
or memory bank prefix is not the planned enterprise tenancy mechanism. A future SaaS would require
a separate threat model, isolation design, abuse controls and acceptance program.

## Runtime admission and capabilities

Preflight required controls before workload start: host/runtime/image/harness identity, filesystem
confinement, process/syscall/resource bounds, network mediation, secret path, evidence sink and
cleanup. A required unsupported capability refuses admission. An audit configuration does not
count as enforcement. Do not silently downgrade to an ordinary container when OpenShell fails.

Apply deny-by-default destinations and receiving API actions, with tests for direct IP, alternate
proxy, DNS/IPv6, redirects, private network and metadata paths. An allowlisted model endpoint is
still an intentional data exit: the source sent to it can leave the machine. A network allowlist
does not prove the model request contains no sensitive data.

Capabilities specify principal, run/generation, destination, operation, resource, expiry and
limits. A child run cannot combine grants into wider authority. A plugin or MCP server uses the
same capability path; local stdio is not inherently trusted and must not inherit unrestricted
host process authority.

## Credentials and both authentication paths

| Path | Required treatment | Unsupported condition |
| --- | --- | --- |
| Claude subscription token | Supported operator enrollment, user-bound reference, recreation/expiry/revocation tests | No shared enterprise token, copied home directory or invented noninteractive compatibility |
| OpenRouter / DeepInfra API | External secret resolution and endpoint-bound mediation where qualified | Wrong endpoint substitution, unsupported protocol or missing requested controls |
| GitHub App | Scoped receiver-side installation token, short-lived, distinct action services | General token mounted into coding worker |
| Deployment | Target-scoped workload identity/short-lived credentials | Agent has production admin credentials |

If a supported local subscription path necessarily exposes a token to the workload, label that
restricted profile honestly; it cannot satisfy OPS credential-isolation requirements. A company
requiring isolation cannot enable it until compatible mediation is demonstrated. Do not silently
force all users onto API billing, but do not claim both paths have identical security guarantees.

Credentials never appear in manifests, logs, issue bodies, exported evidence or example files.
Test with synthetic canaries. Expiry/detach/revocation must affect future and established traffic
according to documented runtime behavior; a UI toggle without enforcement is not sufficient.

## Artifact boundary

Stop the workload before promoting outputs. Trusted promotion accepts only declared regular
files, bounded count/size and approved relative paths. Reject traversal, symlink/hardlink/device/
FIFO/socket entries, changing files and unsupported archive behavior. Verify types and bounds
through safe APIs rather than checking a path and reopening it later.

Do not recursively copy a sandbox into the host or run its hooks on import. Review executable
bits and hidden CI/plugin/config changes. Retained artifacts are protected from worker writes.
The Cloudflare skill in OPS specifies a stricter descriptor-based promotion procedure for its
audit evidence; preserve that contract when running the skill.

## Supply chain and plugin trust

Pin runtime images, plugins, skills, workflows and referenced remote components. Review licence,
notices, execution hooks, data exits and upgrade diffs. A trusted publisher can still ship a
breaking or compromised release. Re-run the applicable qualification matrix after relevant changes.
No global `curl | sh`, floating plugin sync or automatic skill update in an authorized live run.

The complete Cloudflare source snapshot is maintained in OPS. Its validators establish structure
and internal consistency; they do not prove findings or qualify isolation. Its full audit workflow
requires independent verification and bounded sandboxed target execution. SpaceShip must preserve
coverage gaps and confidential reporting rather than convert every model suspicion into a public
GitHub vulnerability ticket.

## Evidence, privacy and storage

Separate protected transition records from optional traces. Authenticate ingestion, bound event
size/rate, label producer trust and detect dropped/gapped telemetry. A workload cannot impersonate
the runtime or rewrite historical decisions. Required journal unavailability blocks protected
transitions; optional analytics may degrade visibly under policy.

Collect metadata by default: identity, timing, decisions, usage, artifact/check lineage and outcome.
Content capture needs explicit company data/retention approval. Encrypt/authenticate storage and
transport as appropriate to the deployment. A local hash chain is useful for integrity checking
but does not establish tamper-proof storage against an administrator controlling the host.

Company authorization applies to traces, artifacts, memory, backups, exports and support bundles,
not only task APIs. Test direct-object access and deletion/export pathways. Redaction is a
defense, not a reason to ingest every secret-bearing payload first.

## Security acceptance and incident response

Before a runtime profile can launch real coding work, demonstrate OPS controls on the declared
host and both selected auth configurations. Before protected GitHub/deployment effects, test
identity substitution, stale approvals/checks, policy self-change, replay, orphan workers and lost
responses. Publish pass/fail/unknown per supported combination; exceptions remain exceptions.

On suspected boundary failure: stop new work, revoke mediated capabilities, terminate/quarantine
affected generations, preserve sanitized external evidence, identify exposed scopes and rebuild
from known inputs. Do not trust the compromised worker to certify its cleanup. Restore normal
operation only after the owner accepts the concrete recovery evidence.
