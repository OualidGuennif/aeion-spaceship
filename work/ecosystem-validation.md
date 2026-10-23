# Independent-module publication checks — 2026-10-23

Scope: five public module entry points, central metadata, offline examples and website content.
This does not qualify a sandbox, provider adapter, cockpit, merge service or deployer.

## Executed local checks

- Factory and CROA: knowledge/link/repository-health gates passed; each ran 10 doc-link tests
  and 137 hook tests. CROA additionally passed its 18 audit CLI tests.
- OPS: all 22 pinned Cloudflare files verified; 13 maintenance-checker tests passed. The
  integrity-only quickstart makes no freshness/network claim and does not renew the weekly check.
- Observability: eight regression tests passed. The offline example includes failed/assisted
  costs, rejects malformed/nonfinite costs and preserves unknown quality/undefined ratios.
- SpaceShip: seven catalog tests passed, including independent adoption, localization,
  canonical repositories, malformed metadata, duplicate JSON and generated documentation.
- Factory knowledge/link checks passed against OPS, Observability and SpaceShip as well.
- Credential-pattern and personal-absolute-path checks found no matches in the publication files;
  this limited check is not a security audit.

## CI and content contract

The three new/updated lightweight workflows use read-only permissions and a verified pinned
checkout action. OPS runs the unchanged Cloudflare validator tests in a bounded network-disabled
container, with no home directory, credentials or host socket attached. Its pinned Node digest
was verified as a multi-architecture OCI index including Linux AMD64 and ARM64.

`ecosystem.json` is the English/French product catalog. `docs/modules.md` is generated from it;
the website content kit consumes the same metadata. Public READMEs explain independent use and
distinguish available tools from planned runtime services. Research source pins remain separate.

Remote publication, final CI and fresh-clone quickstarts are verified at delivery time rather
than inferred from these local checks. Original licences/credits remain with their modules;
CROA's content-specific licensing is preserved.
