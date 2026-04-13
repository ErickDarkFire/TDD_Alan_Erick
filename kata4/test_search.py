from exercise4 import(
    search,
    load_csv_data
)

import pytest

all_cases = (
    load_csv_data('v'),
    load_csv_data('va'),
    load_csv_data('VA'),
    load_csv_data('APE'),
    load_csv_data('*'),
    load_csv_data('vALeN')
)
@pytest.mark.parametrize(
    "text,expected_result",
    all_cases,
    ids=[f"case_{i}" for i in range(len(all_cases))]
)
def test_subtest(text,expected_result):
    assert str(search(text)) == expected_result

    