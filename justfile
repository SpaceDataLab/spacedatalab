# SpaceDataLab's entry points: the crate `spacedatalab` and the `spacedatalab` wheel.

# A spacelab checkout, for the recipes that read one: `just spacelab=../spacelab test-python`.
spacelab := ""

# fmt, clippy, tests and docs, cheapest first, against the spacelab crates on crates.io.
check: fmt lint test doc

fmt:
    cargo fmt --all -- --check

lint:
    cargo clippy --workspace --all-targets --all-features -- -D warnings

test:
    cargo test --workspace --all-features

# The crate's docs with its default features and with all of them: an intra-doc link to a module
# behind a feature breaks only the first.
doc:
    RUSTDOCFLAGS="-D warnings" cargo doc --no-deps -p spacedatalab
    RUSTDOCFLAGS="-D warnings" cargo doc --no-deps -p spacedatalab --features full

# The PyPI README's figure block, copied from spacelab's README at the tag `Cargo.lock` binds.
# `just figures --check` exits 1 if it is stale; `--from DIR` reads a local checkout instead.
figures *ARGS:
    python3 tools/sync-figures.py {{ARGS}}

# spacelab's smoke and bindings tests, read from the checkout, against the wheel built here: what
# `wheels.yml` runs on every platform before an upload.
test-python PY="3.11":
    test -n "{{spacelab}}" || { echo 'name the checkout: just spacelab=DIR test-python'; exit 2; }
    rm -rf target/wheels
    cd crates/spacedatalab-python && uvx maturin build --release -i python{{PY}} -o ../../target/wheels
    uv run --no-project -p {{PY}} --with target/wheels/*.whl python "{{spacelab}}/crates/spacelab-python/tests/smoke.py"
    uv run --no-project -p {{PY}} --with target/wheels/*.whl python "{{spacelab}}/crates/spacelab-python/tests/bindings.py"

# Any recipe above against a local spacelab checkout instead of crates.io, in a copy of this tree at
# target/local: for a change that spans both repositories, or a spacelab release not yet published.
local SPACELAB *RECIPE:
    python3 tools/local-spacelab.py "{{SPACELAB}}" target/local
    abs="$(realpath '{{SPACELAB}}')" && cd target/local && just spacelab="$abs" {{RECIPE}}
