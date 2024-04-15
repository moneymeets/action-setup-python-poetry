import itertools
import sys
import tomllib
from pathlib import Path
from typing import Sequence

IGNORE_PACKAGES = ("boto3",)


def get_version(version: str | dict) -> str | None:
    return version if isinstance(version, str) else version.get("version")


def get_invalid_package_versions(pyproject_data: dict) -> Sequence[tuple[str, str]]:
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
        if package not in IGNORE_PACKAGES
        and (version_str := get_version(version)) not in ("*", None)
        and not version_str.startswith("~")
    )


def run():
    if invalid_versions := get_invalid_package_versions(
        pyproject_data=tomllib.loads(Path("pyproject.toml").read_text()),
    ):
        print(f"Invalid package versions found in pyproject.toml: {invalid_versions}")
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(run())
