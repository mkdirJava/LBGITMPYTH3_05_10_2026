#from __future__ import annotations
import csv
from pathlib import Path


def reassemble_iban(parts: list[str]) -> str:
    """
    Reassemble an IBAN from 6 CSV fields of lengths 4, 4, 4, 4, 4, 2.
    """
    cleaned = [part.strip().upper() for part in parts]
    if len(cleaned) != 6:
        raise ValueError("Each row must contain exactly 6 fields.")
    expected_lengths = [4, 4, 4, 4, 4, 2]
    if [len(part) for part in cleaned] != expected_lengths:
        raise ValueError("IBAN row parts do not match the expected 4,4,4,4,4,2 layout.")
    iban = "".join(cleaned)
    if not iban.isalnum():
        raise ValueError("IBAN contains invalid characters.")
    return iban


def iban_to_numeric_string(iban: str) -> str:
    """
    Rearrange the IBAN and convert letters to numbers for mod-97 checking.
    """
    rearranged = iban[4:] + iban[:4]
    converted: list[str] = []
    for char in rearranged:
        if char.isdigit():
            converted.append(char)
        else:
            converted.append(str(ord(char) - ord("A") + 10))
    return "".join(converted)


def perform_mod97(number_string: str) -> int:
    """
    Calculate modulo 97 incrementally to avoid large integer issues.
    """
    remainder = 0
    for char in number_string:
        remainder = (remainder * 10 + int(char)) % 97
    return remainder


def is_valid_iban(iban: str) -> bool:
    """
    Return True when an IBAN passes the mod-97 check.
    """
    if len(iban) < 5 or not iban.isalnum():
        return False
    numeric = iban_to_numeric_string(iban)
    return perform_mod97(numeric) == 1


def process_iban_file(
    input_csv: str | Path,
    valid_output: str | Path = "valid.txt",
    invalid_output: str | Path = "invalid.txt",
) -> tuple[list[str], list[str]]:
    """
    Read a CSV of 6-part IBAN rows, validate each IBAN, and write
    valid and invalid entries to separate text files.
    """
    valid_ibans: list[str] = []
    invalid_ibans: list[str] = []

    with Path(input_csv).open("rt", newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        header = next(reader, None)    # Discard for now
        for row in reader:
            try:
                iban = reassemble_iban(row)
                if is_valid_iban(iban):
                    valid_ibans.append(iban)
                else:
                    invalid_ibans.append(iban)
            except ValueError:
                invalid_ibans.append("".join(cell.strip().upper() for cell in row))

    Path(valid_output).write_text("\n".join(valid_ibans) + ("\n" if valid_ibans else ""), encoding="utf-8")
    Path(invalid_output).write_text("\n".join(invalid_ibans) + ("\n" if invalid_ibans else ""), encoding="utf-8")

    return valid_ibans, invalid_ibans


def main() -> None:
    valid_ibans, invalid_ibans = process_iban_file("iban.csv", "valid.txt", "invalid.txt")
    print(f"IBANs Processed {len(valid_ibans) + len(invalid_ibans)} IBANs.")
    print(f"IBANs Valid: {len(valid_ibans)}")
    print(f"IBANs Invalid: {len(invalid_ibans)}")


if __name__ == "__main__":
    main()

