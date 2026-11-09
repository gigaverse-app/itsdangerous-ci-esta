import sys


def test_gate_probe_fails_on_python_3_11_only():
    # Throwaway probe: must make exactly one Linux CPython entry fail.
    assert sys.version_info[:2] != (3, 11), "gate probe: deliberate failure on 3.11"
