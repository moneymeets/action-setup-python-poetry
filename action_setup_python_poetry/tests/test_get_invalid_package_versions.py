from pathlib import Path
from unittest import TestCase

from action_setup_python_poetry.invalid_package_versions import get_invalid_package_versions

TEST_DATA_DIR = Path(__file__).parent / "data"


class GetInvalidPackageVersionsTest(TestCase):
    def test_get_invalid_package_versions_success(self):
        valid_pyproject_toml = (TEST_DATA_DIR / "pyproject_mock_valid.toml").read_text()
        self.assertEqual((), get_invalid_package_versions(valid_pyproject_toml))

    def test_get_invalid_package_versions_failed(self):
        invalid_pyproject_toml = (TEST_DATA_DIR / "pyproject_mock_invalid.toml").read_text()
        self.assertEqual(
            (
                ("django", ">=4.2"),
                ("pytest", ">=8"),
                ("test-package-1", ">=1"),
                ("test-package-2", ">=1"),
            ),
            get_invalid_package_versions(invalid_pyproject_toml),
        )

    def test_no_dev_dependencies(self):
        no_dev_dependencies_pyproject_toml = (TEST_DATA_DIR / "pyproject_mock_no_dev_dependencies.toml").read_text()
        self.assertEqual((), get_invalid_package_versions(no_dev_dependencies_pyproject_toml))
