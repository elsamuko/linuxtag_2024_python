import unittest
from linuxtag import functions, worker
from unittest.mock import patch


class DummyResponse:
    def __init__(self, content) -> None:
        print("DummyResponse")
        self.content = content


class TestFunctions(unittest.TestCase):

    def test_add_five(self):
        self.assertEqual(12, functions.add_five(7))
        # self.assertEqual(13, functions.add_five(7))

    @patch(f"requests.get")
    def test_get_ip(self, mock):
        mock.return_value = DummyResponse(b"Blubb")
        rv = functions.get_ip()
        self.assertEqual(rv, "Blubb")

    def test_blubb(self):
        pass
        # self.assertTrue(functions.blubb(True))
        # self.assertFalse(functions.blubb(False))
