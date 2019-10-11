import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodIntersection(unittest.TestCase):
    def test_intersection(self):
        self.assertEqual(
            _.intersection([1, 2, 3, 4], [2, 3, 4, 5]),
            [2, 3, 4]
        )

if __name__ == '__main__':
    unittest.main()
