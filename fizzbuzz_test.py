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

    def test_buzz(self):
        self.assertEqual(fizzbuzz.program(5), "Buzz")
        self.assertEqual(fizzbuzz.program(10), "Buzz")
        self.assertEqual(fizzbuzz.program(20), "Buzz")
        self.assertEqual(fizzbuzz.program(25), "Buzz")

    def test_fizz_buzz(self):
        self.assertEqual(fizzbuzz.program(15), "FizzBuzz")
        self.assertEqual(fizzbuzz.program(30), "FizzBuzz")
        self.assertEqual(fizzbuzz.program(45), "FizzBuzz")
        self.assertEqual(fizzbuzz.program(60), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()
