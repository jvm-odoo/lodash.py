import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodPull(unittest.TestCase):
    def test_pull(self):
        self.assertEqual(
            _.pull([1, 2, 2], 2),
            [1]
        )

if __name__ == '__main__':
    unittest.main()
