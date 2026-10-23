# Working on Æion SpaceShip

- Read [PLAN.md](PLAN.md), [knowledge/index.md](knowledge/index.md) and
  [work/current.md](work/current.md) before meaningful work.
- This repository currently contains a plan. Do not describe proposed adapters or controls as
  implemented. The owner explicitly requested a substantial plan before product implementation.
- Keep code, docs, comments and logs in English. Explain findings to the owner in French.
- Preserve Factory's method. Reuse the four sibling contracts; do not silently change them.
- Trusted code owns authorization, budgets, state transitions and protected effects. Agents
  produce untrusted proposals and artifacts. Never let a score or retrieved text grant authority.
- Inspect source and exact upstream versions before asserting compatibility. Do not execute
  installers, target code, plugin hooks or repository setup on the host to explore an integration.
- Scope credentials to a company and receiving service; never read or print secret stores.
- No external writes, paid calls, merge, deployment or production access are enabled by examples.
- Keep one authority per state domain and one financial admission ledger per execution path.
- Prefer small, testable slices; preserve deny/unknown states and evidence of incomplete work.
- Review security implications before adopting dependencies; preserve upstream licenses/credits.
- Documentation checks prove document consistency, not a runtime boundary or CROA conformance.
