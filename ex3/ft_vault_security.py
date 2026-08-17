"""
Authorized: open(), read(), write(), print()
"""


def secure_archive(
    filename: str,
    action: "int | str" = 0,
    content: str = "",
) -> "tuple[bool, str]":
    is_write = action in (1, "write", "w")
    mode = "w" if is_write else "r"
    try:
        with open(filename, mode) as archive:
            if is_write:
                archive.write(content)
                return True, "Content successfully written to file"
            return True, archive.read()
    except OSError as error:
        return False, str(error)


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print()

    print(
        "Using 'secure_archive' to write previous content to a new file:"
    )
    if result[0]:
        print(secure_archive("new_fragment.txt", "write", result[1]))


if __name__ == "__main__":
    main()
