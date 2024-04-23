import itertools
import sys
import tomllib
from pathlib import Path
from typing import Sequence


def get_version(version: str | dict) -> str | None:
    return version if isinstance(version, str) else version.get("version")


def get_invalid_package_versions(pyproject_toml_file_text: str) -> Sequence[tuple[str, str]]:
    toml_file_text = "\n".join(
        tuple(line for line in pyproject_toml_file_text.splitlines() if "@mm-version-check-ignore" not in line),
    )
    pyproject_data = tomllib.loads(toml_file_text)
    poetry_data = pyproject_data["tool"]["poetry"]

    return tuple(
        (package, version_str)
        for package, version in (
            *poetry_data["dependencies"].items(),
            *poetry_data["dev-dependencies"].items(),
            *itertools.chain.from_iterable(
                (group["dependencies"].items() for _, group in poetry_data.get("group", {}).items()),
            ),
        )
        if (version_str := get_version(version)) not in ("*", None) and not version_str.startswith("~")
    )


def main():
    pyproject_path = Path(sys.argv[1] if len(sys.argv) > 1 else "pyproject.toml")
    if invalid_versions := get_invalid_package_versions(pyproject_path.read_text()):
        print(f"Invalid package versions found in pyproject.toml: {invalid_versions}")
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main())
