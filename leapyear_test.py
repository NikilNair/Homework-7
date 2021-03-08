import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test_not_div_by_4(self):
        self.assertEqual(leapyear.program(2011), "This is not a leap year")
        self.assertEqual(leapyear.program(2013), "This is not a leap year")
        self.assertEqual(leapyear.program(2009), "This is not a leap year")
        self.assertEqual(leapyear.program(2007), "This is not a leap year")

if __name__ == '__main__':
    unittest.main()
