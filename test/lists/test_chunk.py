import sys; sys.path.append('../')
import src as _
import unittest

class TestListsMethodChunk(unittest.TestCase):
    def test_chunk(self):
        self.assertEqual(
            _.chunk([1, 2, 3, 4], 3),
            [[1, 2, 3], [4]]
        )

if __name__ == '__main__':
    unittest.main()
