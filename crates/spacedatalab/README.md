# spacedatalab

[![crates.io](https://img.shields.io/crates/v/spacedatalab)](https://crates.io/crates/spacedatalab)
[![docs.rs](https://img.shields.io/docsrs/spacedatalab)](https://docs.rs/spacedatalab)
[![License: MIT OR Apache-2.0](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue)](https://github.com/SpaceDataLab/spacedatalab#licence)

[Website](https://spacedatalab.org) · [API reference](https://docs.rs/spacedatalab) ·
[spacelab](https://github.com/SpaceDataLab/spacelab)

> **SpaceDataLab in one dependency.** The organisation's Rust entry point, as
> [`spacedatalab`](https://pypi.org/project/spacedatalab/) on PyPI is its Python one. It re-exports
> [spacelab](https://github.com/SpaceDataLab/spacelab), the core: time scales, Earth orientation,
> reference frames and SGP4. Every other spacelab crate is behind a feature named after the module it
> adds.

```toml
[dependencies]
spacedatalab = { version = "0.2", features = ["gnss", "estimation"] }   # or "full"
```

```rust
let iss = spacedatalab::sgp4::Satellite::from_tle(line1, line2)?;
let state = iss.propagate_minutes(90.0)?;
```

The features are `astro`, `astrometry`, `autodiff`, `constellation`, `control`, `coverage`,
`earthvision`, `elements`, `ephemeris`, `estimation`, `geomagnetism`, `geometry`, `gnss`, `grid`,
`ionosphere`, `ndm`, `propagation`, `sensors`, `signal`, `slr` and `vision`; `full` turns on all of
them, and `onnx` adds ONNX inference to `earthvision`. Feature `gnss` adds the module `gnss`, which is
the crate [`spacelab-gnss`](https://docs.rs/spacelab-gnss), and so on. Each crate is verified in the
[spacelab verification ledger](https://github.com/SpaceDataLab/spacelab/blob/main/docs/verification.md).

## Licence

Licensed under either of
[Apache-2.0](https://github.com/SpaceDataLab/spacedatalab/blob/main/LICENSE-APACHE) or
[MIT](https://github.com/SpaceDataLab/spacedatalab/blob/main/LICENSE-MIT) at your option.
