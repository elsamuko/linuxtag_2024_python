import unittest
import subprocess
import sys


class TestIntegration(unittest.TestCase):

    def test_run(self):
        rv = subprocess.run(
            [sys.executable, "-m", "linuxtag", "--test"], capture_output=True
        )
        out = rv.stdout.decode()
        self.assertEqual("ok\n", out)
