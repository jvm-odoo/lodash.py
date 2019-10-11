import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodHeadFirst(unittest.TestCase):
    def test_head_first(self):
        self.assertEqual(
            _.head([1, 2, 3, 2]),
            1
        )

if __name__ == '__main__':
    unittest.main()
