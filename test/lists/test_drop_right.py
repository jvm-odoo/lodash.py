import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodDrop(unittest.TestCase):
    def test_drop(self):
        self.assertEqual(
            _.drop_right([1, 2, 3, 4], 2),
            [1, 2]
        )

if __name__ == '__main__':
    unittest.main()
