import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodDiff(unittest.TestCase):
    def test_diff(self):
        self.assertEqual(
            _.diff([1, 2, 3], [2, 3]),
            [1]
        )

if __name__ == '__main__':
    unittest.main()
