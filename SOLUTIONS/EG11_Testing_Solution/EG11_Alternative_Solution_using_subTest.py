import re
import timeit
import unittest
from typing import Iterable


VALID_HONORIFICS = {"mr", "mrs", "miss", "ms", "dr", "prof"}

HONORIFIC_PART = r"(mr|mrs|miss|ms|dr|prof)"
NAME_PART = r"[A-Za-z]{2,}"
LAST_NAME_PART = r"[A-Za-z]{2,}(?:[ -][A-Za-z]{2,})?"
ACCOUNT_NAME_RE = re.compile(
    rf"^\s*{HONORIFIC_PART}\s+({NAME_PART})\s+({LAST_NAME_PART})\s*$",
    re.IGNORECASE,
)


def is_valid_account_name_v1(value: str) -> bool:
    if not isinstance(value, str):
        return False
    return ACCOUNT_NAME_RE.fullmatch(value) is not None


def is_valid_account_name_v2(value: str) -> bool:
    if not isinstance(value, str):
        return False

    value = value.strip()
    if value == "":
        return False

    pieces = value.split()
    if len(pieces) < 3:
        return False

    honorific = pieces[0].strip().lower()
    if honorific not in VALID_HONORIFICS:
        return False

    first_name = pieces[1].strip()
    if len(first_name) < 2:
        return False

    if not re.fullmatch(r"[A-Za-z]+", first_name):
        return False

    last_name = " ".join(pieces[2:]).strip()
    if len(last_name) < 2:
        return False

    for ch in last_name:
        if not (ch.isalpha() or ch == " " or ch == "-"):
            return False

    if "--" in last_name or "  " in last_name or "- " in last_name or " -" in last_name:
        return False
    if last_name.startswith("-") or last_name.endswith("-"):
        return False

    if "-" in last_name and " " in last_name:
        return False

    if "-" in last_name:
        subparts = last_name.split("-")
    elif " " in last_name:
        subparts = last_name.split(" ")
    else:
        subparts = [last_name]

    if len(subparts) == 0 or len(subparts) > 2:
        return False

    for part in subparts:
        part = part.strip()
        if len(part) < 2:
            return False
        if not re.fullmatch(r"[A-Za-z]+", part):
            return False

    return True


class TestAccountNameValidation(unittest.TestCase):
    def assert_both_true(self, value: str) -> None:
        self.assertTrue(is_valid_account_name_v1(value), f"fast failed for: {value}")
        self.assertTrue(is_valid_account_name_v2(value), f"slow failed for: {value}")

    def assert_both_false(self, value: str) -> None:
        self.assertFalse(is_valid_account_name_v1(value), f"fast passed for: {value}")
        self.assertFalse(is_valid_account_name_v2(value), f"slow passed for: {value}")

    def test_valid_simple_names(self) -> None:
        for name in [
            "Mr John Smith",
            "Mrs Jane Brown",
            "Miss Emily Jones",
            "Dr Sarah Connor",
            "Prof Alan Turing",
            "Ms Rachel Green",
        ]:
            with self.subTest(name=name):
                self.assert_both_true(name)

    def test_valid_hyphenated_last_names(self) -> None:
        for name in [
            "Mr John Smith-Jones",
            "Mrs Sarah Brown-Wilson",
            "Dr Peter Taylor-Reed",
        ]:
            with self.subTest(name=name):
                self.assert_both_true(name)

    def test_valid_spaced_last_names(self) -> None:
        for name in [
            "Mr John Van Dyke",
            "Mrs Anna De Vries",
            "Dr Peter Le Roth",
        ]:
            with self.subTest(name=name):
                self.assert_both_true(name)

    def test_invalid_honorific(self) -> None:
        for name in [
            "Sir John Smith",
            "Lord Peter Jones",
            "Mx Alex Brown",
        ]:
            with self.subTest(name=name):
                self.assert_both_false(name)

    def test_invalid_first_name_too_short(self) -> None:
        for name in [
            "Mr J Smith",
            "Dr A Brown",
        ]:
            with self.subTest(name=name):
                self.assert_both_false(name)

    def test_invalid_last_name_too_short(self) -> None:
        for name in [
            "Mr John S",
            "Mrs Anna B",
            "Dr Peter A-B",
        ]:
            with self.subTest(name=name):
                self.assert_both_false(name)

    def test_invalid_characters(self) -> None:
        for name in [
            "Mr John Sm1th",
            "Mrs Jane Br@wn",
            "Dr Sarah O'Neil",
            "Miss Emma Smith_Lee",
        ]:
            with self.subTest(name=name):
                self.assert_both_false(name)

    def test_invalid_structure(self) -> None:
        for name in [
            "",
            "Mr",
            "Mr John",
            "John Smith",
            "Mr John Smith Jones Brown",
        ]:
            with self.subTest(name=name):
                self.assert_both_false(name)

    def test_invalid_last_name_separator_usage(self) -> None:
        for name in [
            "Mr John Smith--Jones",
            "Mr John Smith - Jones",
            "Mr John -Smith",
            "Mr John Smith-",
            "Mr John Smith-J",
        ]:
            with self.subTest(name=name):
                self.assert_both_false(name)

    def test_non_string_input(self) -> None:
        #for value in [None, 123, 12.5, ["Mr", "John", "Smith"]]:
        value = [None, 123, 12.5, ["Mr", "John", "Smith"]]
        with self.subTest(value=value):
            self.assertFalse(is_valid_account_name_v1(value))  # type: ignore[arg-type]
            self.assertFalse(is_valid_account_name_v2(value))  # type: ignore[arg-type]


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
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAccountNameValidation)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return result.wasSuccessful()


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


if __name__ == "__main__":
    ok = run_tests()
    if ok:
        run_profiling()