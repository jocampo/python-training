import os
import unittest


def analyze_text(filename):
    with open(filename, 'r') as f:
        return sum(len(line.split()) for line in f)


class TextAnalysisTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self._filename = 'text_analysis_test_file.txt'
        with open(self._filename, 'w') as f:
            f.write('Pablito clavo un clavito lol.')

    def tearDown(self):
        """Cleanup! deletes the file if it exists"""
        try:
            os.remove(self._filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test"""
        self.assertEqual(analyze_text(self._filename), 5)

    def test_function_throws_exception(self):
        with self.assertRaises(IOError):
            analyze_text('haha')

