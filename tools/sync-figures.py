#!/usr/bin/env python3
"""Copy the figure block of spacelab's README into the PyPI README.

spacelab's `tools/gen-figures.py` draws four comparisons against independent references and quotes
their numbers in the captions. The PyPI page shows the same block, and a copy typed by hand would
drift, so this copies it from spacelab's README at the tag of the `spacelab-python` that
`Cargo.lock` binds. Image links are pinned to that tag too: the page PyPI renders for a release
never changes, and neither should the pictures its numbers describe.

    python3 tools/sync-figures.py                       # rewrite the block in place
    python3 tools/sync-figures.py --check               # exit 1 if it is stale (CI runs this)
    python3 tools/sync-figures.py --from ../spacelab    # read a local checkout instead of the tag

Standard library only, so CI needs nothing the runner does not already have.
"""

from __future__ import annotations

import re
import sys
import tomllib
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "crates" / "spacedatalab-python" / "README.md"
BEGIN = "<!-- BEGIN GENERATED FIGURES — tools/gen-figures.py -->"
END = "<!-- END GENERATED FIGURES -->"
BLOCK = re.compile(re.escape(BEGIN) + ".*?" + re.escape(END), flags=re.DOTALL)
FIGURES_AT_MAIN = (
    "https://raw.githubusercontent.com/SpaceDataLab/spacelab/main/docs/figures/"
)


def bound_version() -> str:
    """The `spacelab-python` version `Cargo.lock` resolves: the code this wheel links."""
    lock = tomllib.loads((ROOT / "Cargo.lock").read_text(encoding="utf-8"))
    versions = {p["version"] for p in lock["package"] if p["name"] == "spacelab-python"}
    if len(versions) != 1:
        raise SystemExit(
            f"Cargo.lock: expected one spacelab-python, found {sorted(versions)}"
        )
    return versions.pop()


def source_readme(local: Path | None, tag: str) -> str:
    if local is not None:
        return (local / "README.md").read_text(encoding="utf-8")
    url = f"https://raw.githubusercontent.com/SpaceDataLab/spacelab/{tag}/README.md"
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8")


def block_of(text: str, where: str) -> str:
    found = BLOCK.search(text)
    if found is None:
        raise SystemExit(f"{where}: the generated block's markers are missing")
    return found.group(0)


def main() -> int:
    args = sys.argv[1:]
    check = "--check" in args
    local = None
    if "--from" in args:
        local = Path(args[args.index("--from") + 1]).resolve()
    tag = f"v{bound_version()}"
    source = block_of(source_readme(local, tag), str(local or tag))
    if FIGURES_AT_MAIN not in source:
        raise SystemExit(f"{tag}: the block links no figure at {FIGURES_AT_MAIN}")
    new = source.replace(FIGURES_AT_MAIN, FIGURES_AT_MAIN.replace("/main/", f"/{tag}/"))
    text = TARGET.read_text(encoding="utf-8")
    old = block_of(text, str(TARGET))
    if old == new:
        return 0
    if check:
        print(
            f"{TARGET.relative_to(ROOT)}: the figure block differs from spacelab {tag}"
        )
        return 1
    TARGET.write_text(text.replace(old, new), encoding="utf-8")
    print(f"{TARGET.relative_to(ROOT)}: figure block copied from spacelab {tag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
