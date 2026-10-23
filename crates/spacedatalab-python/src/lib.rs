//! The `spacedatalab` Python module, the wheel on PyPI.
//!
//! Each SpaceDataLab product keeps its Python bindings next to its code, in a library with a
//! `register` function, and this module calls them. Its top level is the spacelab core,
//! [`spacelab-python`](https://docs.rs/spacelab-python); a later product arrives as a submodule
//! `spacedatalab.<product>`.

use pyo3::prelude::*;

#[pymodule]
fn spacedatalab(m: &Bound<'_, PyModule>) -> PyResult<()> {
    spacelab_python::register(m)
}
