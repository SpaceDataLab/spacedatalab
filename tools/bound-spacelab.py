#!/usr/bin/env python3
"""Print `tag=vX.Y.Z`, the spacelab tag of the `spacelab-python` that `Cargo.lock` resolves.

The workflows append it to `$GITHUB_OUTPUT` and check spacelab out at that tag, so the Python suites
they run against a wheel are the ones written for the bridge the wheel links.
"""

import sys
import tomllib
from pathlib import Path

lock = tomllib.loads(
    (Path(__file__).resolve().parent.parent / "Cargo.lock").read_text("utf-8")
)
versions = {p["version"] for p in lock["package"] if p["name"] == "spacelab-python"}
if len(versions) != 1:
    sys.exit(f"Cargo.lock: expected one spacelab-python, found {sorted(versions)}")
print(f"tag=v{versions.pop()}")
