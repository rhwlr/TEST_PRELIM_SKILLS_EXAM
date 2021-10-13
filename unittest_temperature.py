from temperature import Temperature
import unittest

class Test_Kelvin(unittest.TestCase):
    
    def test_celsiustokelvin(self):
        self.assertEqual(Temperature(celsius=36).kelvin, 309.15)

    def test_fahrenheittokelvin(self):
        self.assertEqual(Temperature(fahrenheit=33).kelvin, 273.7055555555555)

    def test_kelvintokelvin(self):
        self.assertEqual(Temperature(kelvin=310).kelvin, 310)

    def test_negative_kelvintokelvin(self):
        self.assertEqual(Temperature(kelvin=-285).kelvin, -285)

if __name__ == '__main__':
    unittest.main()