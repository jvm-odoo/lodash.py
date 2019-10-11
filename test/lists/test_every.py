import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodEvery(unittest.TestCase):
    def test_every_true(self):
        self.assertEqual(
            _.every([1, 1, 1], lambda x: x == 1),
            True
        )

    def test_every_false(self):
        self.assertEqual(
            _.every([1, 1, 2], lambda x: x == 1),
            False
        )

if __name__ == '__main__':
    unittest.main()
