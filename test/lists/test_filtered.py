import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodFiltered(unittest.TestCase):
    def test_filtered_found(self):
        self.assertEqual(
            _.filtered([1, 2, 2], lambda x: x == 1),
            [1]
        )

    def test_filtered_not_found(self):
        self.assertEqual(
            _.filtered([2, 2, 2], lambda x: x == 1),
            []
        )

if __name__ == '__main__':
    unittest.main()
