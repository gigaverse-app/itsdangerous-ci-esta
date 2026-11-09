import sys


def test_gate_probe_fails_on_cpython_3_11_only():
    # Throwaway probe: must make exactly one Linux CPython entry fail (not PyPy 3.11).
    is_cpython_311 = sys.implementation.name == "cpython" and sys.version_info[:2] == (3, 11)
    assert not is_cpython_311, "gate probe: deliberate failure on CPython 3.11"
