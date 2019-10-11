import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodDrop(unittest.TestCase):
    def test_drop(self):
        self.assertEqual(
            _.drop([1, 2, 3], 2),
            [3]
        )

if __name__ == '__main__':
    unittest.main()
