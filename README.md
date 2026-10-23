# spacedatalab

[![PyPI](https://img.shields.io/pypi/v/spacedatalab)](https://pypi.org/project/spacedatalab/)
[![crates.io](https://img.shields.io/crates/v/spacedatalab)](https://crates.io/crates/spacedatalab)
[![docs.rs](https://img.shields.io/docsrs/spacedatalab)](https://docs.rs/spacedatalab)
[![ci](https://github.com/SpaceDataLab/spacedatalab/actions/workflows/ci.yml/badge.svg)](https://github.com/SpaceDataLab/spacedatalab/actions/workflows/ci.yml)
[![wheels](https://github.com/SpaceDataLab/spacedatalab/actions/workflows/wheels.yml/badge.svg)](https://github.com/SpaceDataLab/spacedatalab/actions/workflows/wheels.yml)
[![License: MIT OR Apache-2.0](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue)](#licence)

[Website](https://spacedatalab.org) · [spacelab](https://github.com/SpaceDataLab/spacelab) ·
[Verification ledger](https://github.com/SpaceDataLab/spacelab/blob/main/docs/verification.md)

> **SpaceDataLab's entry points, one per language.** Each product keeps its own name and repository;
> this one puts them behind a single dependency. Today that is
> [spacelab](https://github.com/SpaceDataLab/spacelab), astrodynamics in Rust organised around
> independent verification.

```sh
pip install spacedatalab        # then: import spacedatalab
cargo add spacedatalab          # or: cargo add spacedatalab --features full
```

| Crate | Ships as | What it is |
|---|---|---|
| [`spacedatalab`](crates/spacedatalab) | crate on crates.io | the spacelab core re-exported, and every other spacelab crate behind a feature named after its module |
| [`spacedatalab-python`](crates/spacedatalab-python) | the `spacedatalab` wheel on PyPI | the Python module: each product's bindings, added by the `register` function of its own bridge crate |

A product's bindings live next to its code and are tested there: spacelab's are
[`spacelab-python`](https://github.com/SpaceDataLab/spacelab/tree/main/crates/spacelab-python). The
release workflow runs those tests again, at the tag the wheel links, against every wheel before it is
uploaded. A later product arrives as `spacedatalab.<product>` in Python and as a feature in Rust.

`just check` runs fmt, clippy, tests and docs against the crates on crates.io; `just local ../spacelab
check` runs them against a local spacelab checkout, for a change that spans both repositories.

## Licence

Licensed under either of [Apache-2.0](LICENSE-APACHE) or [MIT](LICENSE-MIT) at your option.
