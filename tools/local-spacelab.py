#!/usr/bin/env python3
"""Stage this workspace against a local spacelab checkout instead of the crates on crates.io.

    python3 tools/local-spacelab.py ../spacelab target/local

copies the workspace to DEST, without `target/` and `.git/`, and writes `DEST/.cargo/config.toml`
with a `[patch.crates-io]` entry for every publishable package of the checkout, so cargo and maturin
run in DEST build against it. A change that spans both repositories, or a spacelab release not yet
on crates.io, is tested that way. The copy takes the patched `Cargo.lock`; this tree's stays the
registry's. `just local SPACELAB RECIPE` runs a recipe there.

Standard library only, plus `cargo metadata`.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def packages(spacelab: Path) -> list[tuple[str, Path]]:
    """`(name, directory)` of every package the checkout would publish."""
    out = subprocess.run(
        ["cargo", "metadata", "--format-version", "1", "--no-deps"],
        cwd=spacelab,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    found = [
        (p["name"], Path(p["manifest_path"]).parent)
        for p in json.loads(out)["packages"]
        if p["publish"] != []
    ]
    if not any(name == "spacelab-python" for name, _ in found):
        raise SystemExit(
            f"{spacelab}: no publishable spacelab-python, so not a spacelab checkout"
        )
    return sorted(found)


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    spacelab = Path(sys.argv[1]).resolve()
    dest = Path(sys.argv[2]).resolve()
    patched = packages(spacelab)
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(
        ROOT,
        dest,
        ignore=shutil.ignore_patterns("target", ".git", "dist", "__pycache__"),
    )
    lines = ["[patch.crates-io]"]
    lines += [f'{name} = {{ path = "{path}" }}' for name, path in patched]
    (dest / ".cargo").mkdir()
    (dest / ".cargo" / "config.toml").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print(f"{dest}: {len(patched)} crates patched to {spacelab}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
