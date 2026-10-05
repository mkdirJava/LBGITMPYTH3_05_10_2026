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
