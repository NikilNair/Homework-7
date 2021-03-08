import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test_not_div_by_4(self):
        self.assertEqual(leapyear.program(2011), "This is not a leap year")
        self.assertEqual(leapyear.program(2013), "This is not a leap year")
        self.assertEqual(leapyear.program(2009), "This is not a leap year")
        self.assertEqual(leapyear.program(2007), "This is not a leap year")

    def test_div_by_4_and_not_100(self):
        self.assertEqual(leapyear.program(2008), "This is a leap year")
        self.assertEqual(leapyear.program(2012), "This is a leap year")
        self.assertEqual(leapyear.program(2016), "This is a leap year")
        self.assertEqual(leapyear.program(2020), "This is a leap year")

    def test_div_by_4_100_and_400(self):
        self.assertEqual(leapyear.program(2000), "This is a leap year")
        self.assertEqual(leapyear.program(1600), "This is a leap year")
        self.assertEqual(leapyear.program(2400), "This is a leap year")
        self.assertEqual(leapyear.program(2800), "This is a leap year")

    def test_div_by_4_100_and_not_400(self):
        self.assertEqual(leapyear.program(1800), "This is not a leap year")
        self.assertEqual(leapyear.program(1700), "This is not a leap year")
        self.assertEqual(leapyear.program(1400), "This is not a leap year")
        self.assertEqual(leapyear.program(2100), "This is not a leap year")

if __name__ == '__main__':
    unittest.main()
