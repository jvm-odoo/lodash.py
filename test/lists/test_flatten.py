import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodFlatten(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(
            _.flatten([1, [[[2]]], [[[[[3]]]], 4]]),
            [1, 2, 3, 4]
        )

if __name__ == '__main__':
    unittest.main()
