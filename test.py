import unittest
from main import count_zero
class TestCounter(unittest.TestCase):
    def test(self):
        self.assertEqual(count_zero(100001000), 3)