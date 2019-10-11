import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodCompact(unittest.TestCase):
    def test_compact(self):
        self.assertEqual(
            _.compact([1, 0, False, None, [], {}, ()]),
            [1]
        )

if __name__ == '__main__':
    unittest.main()
