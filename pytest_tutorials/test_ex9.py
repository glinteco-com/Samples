# Write a test that checks if a function raises a warning.

import pytest
import warnings


def test_warning():
    with pytest.warns(UserWarning):
        # code to test
        warnings.warn("test warning", UserWarning)
