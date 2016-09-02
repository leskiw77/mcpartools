import unittest

from mcpartools import generatemc


class TestFunMethod(unittest.TestCase):
    def test_help(self):
        self.assertRaises(SystemExit, generatemc.main, ["--help"])

    def test_version(self):
        self.assertRaises(SystemExit, generatemc.main, ["--version"])

    def test_input_exit_code(self):
        exit_code = generatemc.main(["-j", "2", "-p", "100", "tests/res/sample_fluka.inp"])
        self.assertEqual(exit_code, 0)

    def test_input_bad(self):
        self.assertRaises(SystemExit, generatemc.main, ["-j", "2"])


if __name__ == '__main__':
    unittest.main()