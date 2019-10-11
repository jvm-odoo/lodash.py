import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodDropWhileRight(unittest.TestCase):
    def test_drop_while_right(self):
        self.assertEqual(
            _.drop_while_right([1, 2, 3], lambda x: x != 1),
            [1]
        )

if __name__ == '__main__':
    unittest.main()
