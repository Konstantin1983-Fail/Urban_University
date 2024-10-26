import calk
import unittest


class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calk.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calk.sub(5, 3), 2)

if __name__ == "__main__":
    unittest.main()

