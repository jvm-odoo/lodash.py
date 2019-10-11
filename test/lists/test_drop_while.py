import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodDropWhile(unittest.TestCase):
    def test_drop_while(self):
        self.assertEqual(
            _.drop_while([1, 2, 3], lambda x: x != 3),
            [3]
        )

if __name__ == '__main__':
    unittest.main()
