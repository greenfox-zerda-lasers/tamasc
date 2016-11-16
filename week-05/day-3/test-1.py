import unittest
from p1 import divide_numbers
from p2 import number_of_lines
from p3 import Person

class TestWork(unittest.TestCase):
    def setUp(self):
        pass

    def test_divide_2and2_is1(self):
        self.assertEqual(divide_numbers(2,2), 1)

    def test_divide_2and2_is2(self):
        self.assertEqual(divide_numbers(4,2), 2)

    def test_divide_4and0_isNone(self):
        self.assertEqual(divide_numbers(4,0), None)

    def test_lineNumber_is_4(self):
        self.assertEqual(number_of_lines('tr.txt'), 4)

    def test_lineNumber_noFile(self):
        self.assertEqual(number_of_lines('sda.rt'), 0)

    def test_Lajos_has_name(self):
        lajos = Person('Lajos', 1990)
        self.assertEqual(lajos.name, 'Lajos')

    def test_Lajos_has_birthdate(self):
        lajos = Person('Lajos', 1990)
        self.assertEqual(lajos.birth_date, 1990)

    def test_invalid_birthdate(self):
        self.assertRaises(ValueError, Person, 'Lajos', 2200)

if __name__ == '__main__':
    unittest.main()
