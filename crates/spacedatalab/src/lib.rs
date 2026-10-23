//! SpaceDataLab in one dependency.
//!
//! [SpaceDataLab](https://spacedatalab.org) builds space-data software and gives each product its own
//! name. This crate is the organisation's Rust entry point, as `spacedatalab` on PyPI is its Python
//! one. It re-exports [spacelab](https://docs.rs/spacelab), the core: time scales, Earth orientation,
//! reference frames and SGP4. Every other spacelab crate is behind a feature named after the module it
//! adds, so feature `gnss` adds the module `gnss`, which is the crate `spacelab-gnss`:
//!
//! ```toml
//! [dependencies]
//! spacedatalab = { version = "0.2", features = ["gnss", "estimation"] }
//! ```
//!
//! The features are `astro`, `astrometry`, `autodiff`, `constellation`, `control`, `coverage`,
//! `earthvision`, `elements`, `ephemeris`, `estimation`, `geomagnetism`, `geometry`, `gnss`, `grid`,
//! `ionosphere`, `ndm`, `propagation`, `sensors`, `signal`, `slr` and `vision`; `full` turns on all
//! of them, and `onnx` adds ONNX inference to `earthvision`. A module compiles exactly the code its
//! crate does: depending on `spacelab-gnss` directly is the same build, with one more version to keep
//! in step.
//!
//! ```
//! let iss = spacedatalab::sgp4::Satellite::from_tle(
//!     "1 25544U 98067A   08264.51782528 -.00002182  00000-0 -11606-4 0  2927",
//!     "2 25544  51.6416 247.4627 0006703 130.5360 325.0288 15.72125391563537",
//! )?;
//! let state = iss.propagate_minutes(0.0)?;
//! let radius = state.position.vector.norm(); // metres, TEME
//! assert!((6.6e6..7.0e6).contains(&radius));
//! # Ok::<(), Box<dyn std::error::Error>>(())
//! ```

pub use spacelab::*;

#[cfg(feature = "astro")]
pub use spacelab_astro as astro;
#[cfg(feature = "astrometry")]
pub use spacelab_astrometry as astrometry;
#[cfg(feature = "autodiff")]
pub use spacelab_autodiff as autodiff;
#[cfg(feature = "constellation")]
pub use spacelab_constellation as constellation;
#[cfg(feature = "control")]
pub use spacelab_control as control;
#[cfg(feature = "coverage")]
pub use spacelab_coverage as coverage;
#[cfg(feature = "earthvision")]
pub use spacelab_earthvision as earthvision;
#[cfg(feature = "elements")]
pub use spacelab_elements as elements;
#[cfg(feature = "ephemeris")]
pub use spacelab_ephemeris as ephemeris;
#[cfg(feature = "estimation")]
pub use spacelab_estimation as estimation;
#[cfg(feature = "geomagnetism")]
pub use spacelab_geomagnetism as geomagnetism;
#[cfg(feature = "geometry")]
pub use spacelab_geometry as geometry;
#[cfg(feature = "gnss")]
pub use spacelab_gnss as gnss;
#[cfg(feature = "grid")]
pub use spacelab_grid as grid;
#[cfg(feature = "ionosphere")]
pub use spacelab_ionosphere as ionosphere;
#[cfg(feature = "ndm")]
pub use spacelab_ndm as ndm;
#[cfg(feature = "propagation")]
pub use spacelab_propagation as propagation;
#[cfg(feature = "sensors")]
pub use spacelab_sensors as sensors;
#[cfg(feature = "signal")]
pub use spacelab_signal as signal;
#[cfg(feature = "slr")]
pub use spacelab_slr as slr;
#[cfg(feature = "vision")]
pub use spacelab_vision as vision;
