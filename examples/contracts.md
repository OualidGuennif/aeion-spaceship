# Proposed integration contracts

These are interface requirements for G1, **not implemented SDKs or endpoints**. JSON schemas and
supported transport versions must be compiled and tested before a live adapter is accepted.
Unknown authority-bearing keys fail validation. Simulation identities are rejected on live paths.

## Shared envelope

Every message carries schema/type/version, company/installation identity, producer identity and
trust class, event/request ID, observed/created time, causal task/run/attempt identity where
applicable, source/policy/artifact references and bounded payload. Authenticate transport before
trusting producer fields. Validate sizes/depth/counts, enums, money units and timestamp bounds.

Messages are at-least-once unless the selected receiver explicitly guarantees otherwise.
Consumers deduplicate on the documented identity and record conflicting reuse as an error.
Ordering is per authoritative entity/generation, not inferred from timestamps alone.

## Factory → SpaceShip: work proposal

Input: repository revision, task family, acceptance contract, finding/issue identity, proposed
scope, required owner decisions and bounded artifacts. Output: accepted task or reason-coded
request for missing authority/evidence. Factory's `agent-ready` label is a routing hint; the
receiving service still verifies current policy and scope.

## SpaceShip → OPS: run admission

Input: frozen task/policy/profile, runtime/harness/image identity, approved mounts and network/API
capabilities, credential references, resource/deadline/exposure envelope, evidence requirements
and generation. Output: qualified admission receipt or explicit unsupported/failed control.
Required lifecycle events include start, cancellation request/acknowledgement, limits, cleanup
and uncertain effects. Do not return a passing control from a workload-authored assertion.

## Worker → verifier: artifact proposal

Input: bounded inventory, safe artifact handles, source lineage and intended acceptance contract.
Output: trusted promotion/quarantine result and checks bound to immutable bytes and protected
definitions. Worker-provided stdout is evidence to inspect, never an authoritative check result.

## SpaceShip → CROA: assessment export

Input: scoped architecture/authority map, applicable control evidence references, exact deployed
versions, gaps and unsupported boundaries. Use the existing CROA audit-kit CLI/packet format where
it fits rather than invent a certification endpoint. Output: assessment/report with limitations.
No audit score grants runtime authority; no runtime conformance level is inferred automatically.

## Runtime / ledger / verifier → Observability

Input: native events and canonical task/run/attempt/provider/check/effect joins, usage units,
trust/completeness, interventions and outcome horizon. The financial ledger remains authoritative
for admission; analytics are a projection. Output: measured cohorts and profile recommendations,
never writable policy grants. Preserve native token/cost semantics and incomplete usage.

## Gate → protected receiver

Input: exact company/resource/action, expected prior state/generation, source/artifact identity,
policy/check/approval binding, expiry and one-use effect identity. Output: accepted/denied/conflict/
unknown status plus observed receiver receipt. The receiver revalidates authority and implements
its own idempotency/fencing semantics. A generic authenticated HTTP proxy does not satisfy this.

## Adapter acceptance packet

Each adapter release supplies exact upstream/dependency versions, required privileges, exposed
interfaces, data exits, supported scopes, request/cancel/retry/reconcile behavior, capability
matrix, positive/negative fixtures, unknowns, upgrade compatibility and rollback/removal procedure.
These contracts are the stable Æion surface; the upstream implementation can change only through
reviewed mapping and requalification.
