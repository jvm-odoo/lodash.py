import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodDropWhileRight(unittest.TestCase):
    def drop_right_while(self):
        self.assertEqual(
            _.drop_right_while([1, 2, 3], lambda x: x != 1),
            [1]
        )

if __name__ == '__main__':
    unittest.main()
