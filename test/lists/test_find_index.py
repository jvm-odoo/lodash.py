import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodFindIndex(unittest.TestCase):
    def test_find_index(self):
        self.assertEqual(
            _.find_index([1, 2, 3], lambda x: x == 2),
            1
        )

if __name__ == '__main__':
    unittest.main()
