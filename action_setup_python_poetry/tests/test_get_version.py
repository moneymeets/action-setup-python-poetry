from unittest import TestCase

from action_setup_python_poetry.invalid_package_versions import get_version


class GetVersionTest(TestCase):
    def test_get_version_success(self):
        self.assertEqual("*", get_version("*"))
        self.assertEqual("*", get_version({"version": "*"}))

    def test_get_version_failed(self):
        self.assertEqual(None, get_version({}))
