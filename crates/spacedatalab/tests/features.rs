//! Every feature adds the module it is named after. Compiling this file under `full` is the check.

#![cfg(feature = "full")]

#[allow(unused_imports)]
use spacedatalab::{
    astro, astrometry, autodiff, constellation, control, coverage, earthvision, elements,
    ephemeris, estimation, geomagnetism, geometry, gnss, grid, ionosphere, ndm, propagation,
    sensors, signal, slr, vision,
};
