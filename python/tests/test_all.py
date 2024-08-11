import pytest
import search


def test_sum_as_string():
    assert search.sum_as_string(1, 1) == "2"
