extern crate pyo3;

use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;

use regex::Regex;

#[pyfunction]
fn get_page_layout_from_djs(djs: &str) -> PyResult<String> {
    let re = Regex::new(r#"(?m)DDG\.pageLayout\.load\('d',(\[\{.+\}),\{"n"#)
        .expect("Failed to compile regex for page layout retrieval.");

    match re.find(djs) {
        Some(m) => Ok(m.as_str().to_string()),
        None => Err(PyRuntimeError::new_err(
            "Failed to get parse page layout (crucial element)",
        )),
    }
}

#[pyfunction]
fn get_djs(response_text: &str) -> PyResult<String> {
    let re =
        Regex::new(r#"'(/d\.js\?.+)'"#).expect("Failed to compile regex for `d.js` retrieval.");

    match re.find(response_text) {
        Some(m) => Ok(m.as_str().to_string().trim_matches('\'').to_string()),
        None => Err(PyRuntimeError::new_err(
            "Failed to get d.js (crucial script element from response.text)",
        )),
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn search(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_djs, m)?)?;
    m.add_function(wrap_pyfunction!(get_page_layout_from_djs, m)?)?;
    Ok(())
}
