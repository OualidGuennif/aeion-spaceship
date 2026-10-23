---
type: Component
title: "Independent module catalog and website content contract"
description: "Canonical five-repository positioning, maturity, quickstarts and bilingual website content with deterministic drift checks."
status: draft
sources:
  - id: catalog
    resource: ../../ecosystem.json
    title: "Canonical public module metadata"
  - id: tool
    resource: ../../tools/ecosystem.py
    title: "Offline validation and guide generation"
  - id: tests
    resource: ../../tests/test_ecosystem.py
    title: "Catalog regression checks"
---

# Ecosystem catalog

## Intent

Make the five repositories understandable and independently adoptable. Keep a single source
for repository URLs, maturity, English/French summaries, prerequisites and safe quickstarts.
Prepare content for a future website without creating another source of product truth.

## Data sources

`ecosystem.json` is maintained by the owner. Each module's source, README, tests and licence
establish its actual capabilities. Metadata does not establish runtime qualification. The
third-party research lock is a separate provenance record, not an installation manifest.

## Inputs

The version-1 catalog contains five ordered modules, canonical repositories, localized summaries
and maturity labels, standalone status, empty mandatory Æion-module dependencies, prerequisites,
available/planned scope, licence notes and examples. Commands are text, never executed by this tool.

## Outputs

`python3 tools/ecosystem.py render` emits `docs/modules.md`. `check` validates the catalog,
generated guide, local Markdown targets, strict JSON and inactive orchestration fixtures.
The website may consume the JSON directly. No network, model or external writer is involved.

## Invariants

- Every repository is independently useful; conceptual relationships are not package dependencies.
- Actual tools and planned runtime capabilities remain separate.
- Quickstarts make no paid model call or external mutation.
- Generated content cannot silently drift from the catalog.
- Canonical links, complete translations and duplicate-free JSON are required.
- Runtime availability stays false until a separately qualified release changes the contract.

## Determinism

Rendering uses catalog order and fixed templates. Validation reads local bytes only. This is
a publication consistency check, not an execution governor, security certificate or remote-link probe.

## Acceptance checks

Run `python3 tools/ecosystem.py check` and `python3 -m unittest discover -s tests -v`.
Test missing modules/translations, repository substitution, introduced module dependencies,
paid quickstarts, duplicate keys and stale output. Separately exercise every advertised example.

## Out of scope

Installing modules, model routing, runtime authorization, a running cockpit, website hosting
and automatically claiming planned features implemented.
