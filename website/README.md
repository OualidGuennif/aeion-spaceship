# Website content kit

This prepares the presentation of Æion SpaceShip. No site is implemented or deployed here.

## Canonical content

Use [ecosystem.json](../ecosystem.json) for module cards, repository URLs, English/French
summaries, maturity, prerequisites and quickstarts. The locale-specific `website` fields supply
the hero/status note. The [module guide](../docs/modules.md) is generated from the same JSON.
Do not maintain another independently edited set of product cards.

```python
import json
from pathlib import Path

catalog = json.loads(Path("ecosystem.json").read_text())
print(catalog["website"]["headline"]["fr"])
for module in catalog["modules"]:
    print(module["name"], module["summary"]["fr"], module["repository"])
```

Run from the SpaceShip checkout. This reads metadata only. A future website should consume a
reviewed content revision, escape text and preserve canonical links. Rendering the explanation
needs no live GitHub/model request.

## Presentation sequence

1. Hero: modular software-factory framework and explicit current status.
2. Five cards: purpose, available capability, planned scope and repository link.
3. Adoption paths: minimum setup, security, audit, measurement or full assembly roadmap.
4. One small example and expected result per module.
5. Integrated vision: deterministic authority, bounded agents, cost/time/quality.
6. Evidence, implementation gates, limitations, licences and upstream credits.

Use “Choose a module”, “Try an offline example” and “Read the integration plan”. Do not use
“Launch the factory” or “Connect production” until those paths are implemented and qualified.

## Claims and publication

Say **open-source framework** and **independent modules**. Name the actual scaffold/audit/checker/
example tools. Label synthetic metrics. Keep the integrated cockpit, automatic ticketing/MFA/
deployment and qualified optimization visibly planned. Do not claim perfect security,
certification, measured savings or universal autonomy. Preserve CROA and upstream attribution.

Before publishing, run `python3 tools/ecosystem.py check`; regenerate the module guide with
`python3 tools/ecosystem.py render > docs/modules.md` when the catalog changes. Exercise the
examples, review both languages and visible maturity, and pin the site's consumed revision.
Hosting, analytics, domain and deployment choices are separate work.
