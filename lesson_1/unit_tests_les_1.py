import unittest
from unittest.mock import patch

from lesson_1 import product_and_sum, equation, generate, letter_position
from lesson_1 import num_to_letter, triangle, is_leap_year, avg_num


class TestProblem(unittest.TestCase):
    @patch('builtins.input', return_value='234')
    def test_ex_1(self, user_numbers):
        self.assertEqual(product_and_sum(), 'Сумма чисел = 9\nПроизведение чисел =  24')

    @patch('builtins.input', return_value='1 5 -5 6')
    def test_ex_3(self, coords):
        self.assertEqual(equation(), 'y = 2.75x + -7.75')

    @patch('builtins.input', return_value='i 1 999')
    def test_ex_4(self, user_input):
        self.assertGreater(generate(), 1)
        self.assertLess(generate(), 999)

    @patch('builtins.input', return_value='a x')
    def test_ex_5(self, user_input):
        self.assertEqual(letter_position(), 'a - 1 место\nx - 24 место\nБукв между ними - 23')

    @patch('builtins.input', return_value='26')
    def test_ex_6(self, user_input):
        self.assertEqual(num_to_letter(), 'z')

    @patch('builtins.input', return_value='2 3 4')
    def test_ex_7_1(self, user_input):
        self.assertEqual(triangle(), 'Треугольник разносторонний')

    @patch('builtins.input', return_value='1 2 34')
    def test_ex_7_2(self, user_input):
        self.assertEqual(triangle(), 'Такой треугольник не может существовать.')

    @patch('builtins.input', return_value='3 3 5')
    def test_ex_7_3(self, user_input):
        self.assertEqual(triangle(), 'Треугольник равнобедренный')

    @patch('builtins.input', return_value='4 4 4')
    def test_ex_7_4(self, user_input):
        self.assertEqual(triangle(), 'Треугольник равносторонний')

    @patch('builtins.input', return_value='2000')
    def test_ex_8_1(self, user_input):
        self.assertEqual(is_leap_year(), '2000 - Год високосный')

    @patch('builtins.input', return_value='2394')
    def test_ex_8_2(self, user_input):
        self.assertEqual(is_leap_year(), '2394 - Год не високосный')

    @patch('builtins.input', return_value='1 3 5')
    def test_ex_9_1(self, user_input):
        self.assertEqual(avg_num(), '3 - Среднее')

    @patch('builtins.input', return_value='10 3 5')
    def test_ex_9_2(self, user_input):
        self.assertEqual(avg_num(), '5 - Среднее')

    @patch('builtins.input', return_value='4 3 10')
    def test_ex_9_3(self, user_input):
        self.assertEqual(avg_num(), '4 - Среднее')


if __name__ == '__main__':
    unittest.main()
