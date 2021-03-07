import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test_return(self):
        self.assertEqual(fizzbuzz.program(2), 2)
        self.assertEqual(fizzbuzz.program(4), 4)
        self.assertEqual(fizzbuzz.program(7), 7)
        self.assertEqual(fizzbuzz.program(8), 8)

if __name__ == '__main__':
    unittest.main()
