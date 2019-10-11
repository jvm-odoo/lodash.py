import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodFindLastIndex(unittest.TestCase):
    def test_find_last_index(self):
        self.assertEqual(
            _.find_last_index([1, 2, 3, 2], lambda x: x == 2),
            3
        )

if __name__ == '__main__':
    unittest.main()
