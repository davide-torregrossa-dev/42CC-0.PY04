"""
Authorized: sys, sys.argv, len(), open(), typing, typing.IO, io.read(),
io.write(), io.close(), print(), input()
"""
import sys
import typing


def add_archive_char(content: str) -> str:
    lines = content.splitlines(keepends=True)
    result = ""
    for line in lines:
        if line.endswith("\n"):
            result += line[:-1] + "#\n"
        else:
            result += line + "#"
    return result


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
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
    print()

    transformed = add_archive_char(content)
    print("Transform data:")
    print("---")
    print()
    print(transformed, end="")
    print()
    print("---")

    new_name = input("Enter new file name (or empty): ")
    if new_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_name}'")
    try:
        new_archive: typing.IO[str] = open(new_name, "w")
    except OSError as error:
        print(f"Error opening file '{new_name}': {error}")
        return
    new_archive.write(transformed)
    new_archive.close()
    print(f"Data saved in file '{new_name}'.")


if __name__ == "__main__":
    main()
