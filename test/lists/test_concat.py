import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodConcat(unittest.TestCase):
    def test_concat(self):
        self.assertEqual(
            _.concat([1], [2], [[3], [[4]]]),
            [1, 2, 3, 4]
        )

if __name__ == '__main__':
    unittest.main()
