"""A script demonstrating access to external data."""
# from __future__ import annotations

import sys
from typing import Any, Dict, Final, Optional

import requests


POSTCODES_API_BASE_URL: Final[str] = "https://api.postcodes.io/postcodes"
REQUEST_TIMEOUT_SECONDS: Final[int] = 5
SEPARATOR_WIDTH: Final[int] = 60

# Custom headers to spoof the User-Agent
# (in case of API restriction)
REQUEST_HEADERS: Final[Dict[str, str]] = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.1901.183 Safari/537.36 Edg/115.0.1901.183"
    )
}


def build_postcode_url(postcode: str) -> str:
    """
    Build the Postcodes.io URL for a given postcode.

    :param postcode: The postcode to lookup
    :return: Fully qualified API URL
    """
    return f"{POSTCODES_API_BASE_URL}/{postcode}"


def fetch_postcode_response(postcode: str) -> requests.Response:
    """
    Make a GET request for a postcode lookup.

    :param postcode: The postcode to lookup
    :return: The HTTP response object
    :raises requests.exceptions.RequestException:
        If the request fails
    """
    url = build_postcode_url(postcode)

    # Make Get request to endpoint URL, with spoofed
    # user agent string and a suitable timeout
    return requests.get(
        url,
        headers=REQUEST_HEADERS,
        timeout=REQUEST_TIMEOUT_SECONDS,
    )


def extract_postcode_information(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract specific information from the API response payload.

    :param data: Parsed JSON response
    :return: Dictionary containing selected postcode fields
    """
    result: Dict[str, Any] = data.get("result", {})

    extracted_info: Dict[str, Any] = {
        "country": result.get("country"),
        "parliamentary_constituency": result.get("parliamentary_constituency"),
        "longitude": result.get("longitude"),
        "latitude": result.get("latitude"),
        "NUTS_geocode": result.get("codes", {}).get("nuts"),
    }
    return extracted_info


def print_error(message: str) -> None:
    """
    Print an error message to standard error.
    """
    print(message, file=sys.stderr)


def lookup_postcode(postcode: str) -> Optional[Dict[str, Any]]:
    """
    Looks up a single postcode using the Postcodes.io API
    and extract specific information.
    """
    try:
        response = fetch_postcode_response(postcode)

        if response.status_code == requests.codes.ok:  # 200
            data: Dict[str, Any] = response.json()
            return extract_postcode_information(data)

        if response.status_code == requests.codes.not_found:  # 404
            print_error(f"Error: Postcode '{postcode}' was not found.")
            return None

        print_error(
            f"Error: Received unexpected status code {response.status_code}."
        )
        return None

    except requests.exceptions.RequestException as exc:
        print_error(f"Error: Request failed: {exc}")
        return None


def print_separator() -> None:
    """Display a row of separator characters."""
    print("\n" + "-" * SEPARATOR_WIDTH + "\n")


def print_extracted_information(result: Dict[str, Any]) -> None:
    """Print extracted postcode information."""
    print("Extracted Information:")
    for key, value in result.items():
        print(f"  {key}: {value}")


def main() -> None:
    """Entry point for the script."""
    postcode = "EC2R8AH"

    print_separator()
    print(f"Testing with postcode: {postcode}")

    result = lookup_postcode(postcode)

    if result:
        print_extracted_information(result)

    print_separator()


if __name__ == "__main__":
    main()