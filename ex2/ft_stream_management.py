"""
Authorized: sys, sys.argv, sys.stdin, sys.stdout, sys.stderr, len(),
open(), typing, typing.IO, io.read(), io.readline(), io.write(),
io.flush(), io.close(), print()
"""

import sys
import typing


def print_sep(str) -> None:
    print("---")
    print()
    print(str, end="")
    print()
    print("---")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    try:
        archive: typing.IO[str] = open(filename, "r")
    except OSError as error:
        print(
            f"[STDERR] Error opening file '{filename}': {error}",
            file=sys.stderr,
        )
        return
    content = archive.read()
    print_sep(content)
    archive.close()
    print(f"File '{filename}' closed.")
    print()
    transformed = content.replace("\n", "#\n")
    print("Transform data:")
    print_sep(transformed)
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_name = sys.stdin.readline().rstrip("\n")
    if new_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_name}'")
    try:
        new_archive: typing.IO[str] = open(new_name, "w")
    except OSError as error:
        print(
            f"[STDERR] Error opening file '{new_name}': {error}",
            file=sys.stderr,
        )
        print("Data not saved.")
        return
    new_archive.write(transformed)
    new_archive.close()
    print(f"Data saved in file '{new_name}'.")


if __name__ == "__main__":
    main()
