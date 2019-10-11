import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodFill(unittest.TestCase):
    def test_fill(self):
        self.assertEqual(
            _.fill([1, 2, 3, 4], '*', 1, 3),
            [1, '*', '*', 4]
        )

if __name__ == '__main__':
    unittest.main()
