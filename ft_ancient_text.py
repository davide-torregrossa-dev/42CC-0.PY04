"""
Authorized: sys, sys.argv, len(), open(), typing, typing.IO, io.read(),
io.close(), print()
"""
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        archive: typing.IO[str] = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return
    content = archive.read()
    archive.close()
    print("---")
    print()
    print(content, end="")
    print()
    print("---")
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
