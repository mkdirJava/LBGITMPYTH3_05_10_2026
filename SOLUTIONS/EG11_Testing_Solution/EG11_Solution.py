import timeit
from typing import Iterable

import pytest
from EG11_Solution_CUT import is_valid_account_name_v1, is_valid_account_name_v2

# --- Helper assertions (pytest style) ---

def assert_both_true(value: str) -> None:
    assert is_valid_account_name_v1(value), f"fast failed for: {value}"
    assert is_valid_account_name_v2(value), f"slow failed for: {value}"


def assert_both_false(value) -> None:
    assert not is_valid_account_name_v1(value), f"fast passed for: {value}"
    assert not is_valid_account_name_v2(value), f"slow passed for: {value}"


# --- Tests ---

@pytest.mark.parametrize("name", [
    "Mr John Smith",
    "Mrs Jane Brown",
    "Miss Emily Jones",
    "Dr Sarah Connor",
    "Prof Alan Turing",
    "Ms Rachel Green",
])
def test_valid_simple_names(name):
    assert_both_true(name)


@pytest.mark.parametrize("name", [
    "Mr John Smith-Jones",
    "Mrs Sarah Brown-Wilson",
    "Dr Peter Taylor-Reed",
])
def test_valid_hyphenated_last_names(name):
    assert_both_true(name)


@pytest.mark.parametrize("name", [
    "Mr John Van Dyke",
    "Mrs Anna De Vries",
    "Dr Peter Le Roth",
])
def test_valid_spaced_last_names(name):
    assert_both_true(name)


@pytest.mark.parametrize("name", [
    "Sir John Smith",
    "Lord Peter Jones",
    "Mx Alex Brown",
])
def test_invalid_honorific(name):
    assert_both_false(name)


@pytest.mark.parametrize("name", [
    "Mr J Smith",
    "Dr A Brown",
])
def test_invalid_first_name(name):
    assert_both_false(name)


@pytest.mark.parametrize("name", [
    "Mr John S",
    "Mrs Anna B",
    "Dr Peter A-B",
])
def test_invalid_last_name_too_short(name):
    assert_both_false(name)


@pytest.mark.parametrize("name", [
    "Mr John Sm1th",
    "Mrs Jane Br@wn",
    "Dr Sarah O'Neil",
    "Miss Emma Smith_Lee",
])
def test_invalid_characters(name):
    assert_both_false(name)


@pytest.mark.parametrize("name", [
    "",
    "Mr",
    "Mr John",
    "John Smith",
    "Mr John Smith Jones Brown",
])
def test_invalid_structure(name):
    assert_both_false(name)


@pytest.mark.parametrize("name", [
    "Mr John Smith--Jones",
    "Mr John Smith - Jones",
    "Mr John -Smith",
    "Mr John Smith-",
    "Mr John Smith-J",
])
def test_invalid_last_name_separator_usage(name):
    assert_both_false(name)


@pytest.mark.parametrize("value", [
    None,
    123,
    12.5,
    ["Mr", "John", "Smith"],
])
def test_non_string_input(value):
    assert not is_valid_account_name_v1(value)
    assert not is_valid_account_name_v2(value)


def build_test_dataset() -> list[str]:
    base_values = [
        "Mr John Smith",
        "Mrs Jane Brown",
        "Miss Emily Jones",
        "Dr Sarah Connor",
        "Prof Alan Turing",
        "Ms Rachel Green",
        "Mr John Smith-Jones",
        "Mr John Van Dyke",
        "Sir John Smith",
        "Mr J Smith",
        "Mr John S",
        "Mr John Sm1th",
        "John Smith",
        "Mr John Smith--Jones",
        "Mr John Smith Jones Brown",
    ]
    return base_values * 2000


def profile_validator(func, dataset: Iterable[str], loops: int = 100) -> float:
    data = list(dataset)
    return timeit.timeit(lambda: [func(item) for item in data], number=loops)


def run_tests() -> bool:
    # suite = pytest.defaultTestLoader.loadTestsFromTestCase(TestAccountNameValidation)
    # result = pytest.TextTestRunner(verbosity=2).run(suite)
    # return result.wasSuccessful()

    """
    Runs all pytest tests in the current module.
    Returns True if all tests pass, otherwise False.
    """
    # Run pytest programmatically
    result_code = pytest.main(["-v", __file__])

    # pytest returns 0 if all tests passed
    return result_code == 0



def run_profiling() -> None:
    dataset = build_test_dataset()

    fast_time = profile_validator(is_valid_account_name_v1, dataset)
    slow_time = profile_validator(is_valid_account_name_v2, dataset)

    print("\nProfiling results")
    print("-----------------")
    print(f"Fast version: {fast_time:.6f} seconds")
    print(f"Slow version: {slow_time:.6f} seconds")

    if fast_time < slow_time:
        print(f"Faster function: is_valid_account_name_v1 ({slow_time / fast_time:.2f}x faster)")
    elif slow_time < fast_time:
        print(f"Faster function: is_valid_account_name_v2 ({fast_time / slow_time:.2f}x faster)")
    else:
        print("Both functions took the same time")


if __name__ == "__main__": #<< run this from the terminal as python EG11_Solution.py
    ok = run_tests()
    if ok:
        run_profiling()