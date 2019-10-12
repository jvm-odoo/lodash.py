import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodWithout(unittest.TestCase):
    def test_without(self):
        self.assertEqual(
            _.without([1, 2, 3], 2, 3),
            [1]
        )

if __name__ == '__main__':
    unittest.main()
