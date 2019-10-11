import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodSome(unittest.TestCase):
    def test_some_true(self):
        self.assertEqual(
            _.some([1, 1, 2], lambda x: x == 1),
            True
        )

    def test_some_false(self):
        self.assertEqual(
            _.some([2, 2, 2], lambda x: x == 1),
            False
        )

if __name__ == '__main__':
    unittest.main()
