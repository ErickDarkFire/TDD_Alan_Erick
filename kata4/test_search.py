from exercise4 import(
    search,
    load_csv_data
)

import pytest
import csv

@pytest.mark.parametrize("text ,expected_result", load_csv_data(1))
def test_ShouldReturnNoResult_WhenInputIsLesThanTwo(text, expected_result):
    assert search(text) == expected_result

@pytest.mark.parametrize("text ,expected_result", load_csv_data(2))
def test_Should(text, expected_result):
    assert search(text) == expected_result

@pytest.mark.parametrize("text ,expected_result", load_csv_data(3))
def test_Should(text, expected_result):
    assert search(text) == expected_result

@pytest.mark.parametrize("text ,expected_result", load_csv_data(4))
def test_Should(text, expected_result):
    assert search(text) == expected_result

@pytest.mark.parametrize("text ,expected_result", load_csv_data(5))
def test_Should(text, expected_result):
    assert search(text) == expected_result

    