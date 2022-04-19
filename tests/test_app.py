import os
import unittest

from octue import Runner
from octue.log_handlers import apply_log_handler

REPOSITORY_ROOT = os.path.dirname(os.path.dirname(__file__))
TWINE_PATH = os.path.join(REPOSITORY_ROOT, "twine.json")


apply_log_handler()


class TestApp(unittest.TestCase):
    def test_app(self):
        """Test that the app takes in input in the correct format and returns an analysis with the correct output
        values.
        """
        runner = Runner(app_src=REPOSITORY_ROOT, twine=TWINE_PATH)
        analysis = runner.run(input_values={"n_iterations": 3})
        self.assertEqual(analysis.output_values, [1, 2, 3, 4, 5])
