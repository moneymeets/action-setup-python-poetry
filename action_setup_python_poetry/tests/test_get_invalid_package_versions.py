from pathlib import Path
from unittest import TestCase

from action_setup_python_poetry.invalid_package_versions import get_invalid_package_versions

TEST_DATA_DIR = Path(__file__).parent / "data"


class GetInvalidPackageVersionsTest(TestCase):
    valid_pyproject_toml = (TEST_DATA_DIR / "pyproject_mock_valid.toml").read_text()
    invalid_pyproject_toml = (TEST_DATA_DIR / "pyproject_mock_invalid.toml").read_text()

    def test_get_invalid_package_versions_success(self):
        self.assertEqual((), get_invalid_package_versions(self.valid_pyproject_toml))

    def test_get_invalid_package_versions_failed(self):
        self.assertEqual(
            (
                ("python", ">=3.12"),
                ("pytest", ">=8"),
                ("test-package-1", ">=1"),
                ("test-package-2", ">=1"),
            ),
            get_invalid_package_versions(self.invalid_pyproject_toml),
        )
