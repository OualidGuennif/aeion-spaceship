#!/usr/bin/env python3
"""Check the public module catalog or render its adoption guide; no network or runtime launch.

Spec: knowledge/components/ecosystem-catalog.md
"""

import argparse
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
MODULE_IDS = ("factory", "ops", "croa", "observability", "spaceship")


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("Duplicate JSON key: " + key)
        value[key] = item
    return value


def read_json(path):
    def reject_constant(value):
        raise ValueError("Nonfinite JSON number: " + value)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object,
                      parse_constant=reject_constant)


def validate(catalog):
    if type(catalog["schema_version"]) is not int or catalog["schema_version"] != 1 or catalog["locales"] != ["en", "fr"]:
        raise ValueError("Unsupported catalog version or locales")
    if catalog["project"]["integrated_runtime_available"] is not False:
        raise ValueError("Runtime status must remain false until its release is qualified")
    if tuple(m["id"] for m in catalog["modules"]) != MODULE_IDS:
        raise ValueError("Expected exactly the five canonical modules in adoption order")
    for field in ("headline", "introduction", "status_note"):
        if (set(catalog["website"][field]) != {"en", "fr"}
                or not all(isinstance(v, str) and v for v in catalog["website"][field].values())):
            raise ValueError("Incomplete website localization")
    for module in catalog["modules"]:
        if module["repository"] != "https://github.com/OualidGuennif/aeion-" + module["id"]:
            raise ValueError("Unexpected canonical repository")
        if module["standalone"] is not True or module["requires_aeion_modules"] != []:
            raise ValueError("Modules must remain independently adoptable")
        for field in ("summary", "maturity_label"):
            if (set(module[field]) != {"en", "fr"}
                    or not all(isinstance(v, str) and v for v in module[field].values())):
                raise ValueError("Incomplete module localization")
        if not module["maturity"] or not module["available"] or not module["planned_or_not_provided"]:
            raise ValueError("Missing maturity or scope distinction")
        quickstart = module["quickstart"]
        if quickstart["external_writes"] is not False or quickstart["paid_calls"] is not False:
            raise ValueError("Quickstarts must not write remotely or spend provider quota")
        if (not isinstance(quickstart["commands"], list) or not quickstart["commands"]
                or not all(isinstance(c, str) and c for c in quickstart["commands"])):
            raise ValueError("Quickstart commands must be nonempty strings")
    return catalog


def render(catalog):
    lines = ["# Choose your Æion modules", "", "<!-- Generated from ecosystem.json by tools/ecosystem.py render. -->", "",
             "Every repository can be used independently. There is no mandatory suite installation,",
             "Git submodule tree or dependency on a running SpaceShip service. Factory is the shared",
             "method; adopting that method does not require cloning another repository.", "",
             "| Module | Use it for | Available today |", "| --- | --- | --- |"]
    for module in catalog["modules"]:
        lines.append("| [{name}]({repository}) | {summary} | {status} |".format(
            name=module["name"], repository=module["repository"],
            summary=module["summary"]["en"], status=module["maturity_label"]["en"]))
    lines += ["", "Start with one module. Combine only the contracts you need. SpaceShip documents",
              "their integration; the integrated cockpit and execution path are not available yet.", ""]
    for module in catalog["modules"]:
        lines += ["## " + module["name"], "", module["summary"]["en"], "",
                  "Prerequisites: " + ", ".join(module["requirements"]) + ".", "", "```sh",
                  *module["quickstart"]["commands"], "```", "", module["quickstart"]["expected"], "",
                  "Available: " + "; ".join(module["available"]) + ".", "",
                  "Planned or outside this module: " + "; ".join(module["planned_or_not_provided"]) + ".", "",
                  "License: " + module["license"] + ".", ""]
    return "\n".join(lines)


def check(root, catalog):
    expected = render(catalog)
    if (root / "docs/modules.md").read_text(encoding="utf-8") != expected:
        raise ValueError("docs/modules.md is stale; regenerate with tools/ecosystem.py render")
    for path in root.rglob("*.json"):
        if ".git" not in path.parts:
            read_json(path)
    policy = read_json(root / "examples/company-policy.json")
    if policy["execution"]["enabled"] or policy["github"]["external_writes"]:
        raise ValueError("Design fixtures must remain inactive")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            target = target.split("#")[0]
            if target and "://" not in target and not target.startswith("mailto:"):
                if not (path.parent / target).exists():
                    raise ValueError("Broken local link in " + str(path.relative_to(root)) + ": " + target)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", choices=("check", "render"))
    args = parser.parse_args()
    try:
        catalog = validate(read_json(ROOT / "ecosystem.json"))
        if args.command == "render":
            print(render(catalog), end="")
        else:
            check(ROOT, catalog)
            print("PASS: 5 independent modules; catalog, generated guide, local links and inactive examples checked")
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("FAIL: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
