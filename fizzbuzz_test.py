import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test_return(self):
        self.assertEqual(fizzbuzz.program(2), 2)
        self.assertEqual(fizzbuzz.program(4), 4)
        self.assertEqual(fizzbuzz.program(7), 7)
        self.assertEqual(fizzbuzz.program(8), 8)

    def test_fizz(self):
        self.assertEqual(fizzbuzz.program(3), "Fizz")
        self.assertEqual(fizzbuzz.program(6), "Fizz")
        self.assertEqual(fizzbuzz.program(9), "Fizz")
        self.assertEqual(fizzbuzz.program(12), "Fizz")

if __name__ == '__main__':
    unittest.main()
