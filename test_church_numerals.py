import unittest
from main import *

class TestChurchNumerals(unittest.TestCase):

    def test_church_to_int(self):
        self.assertEqual(church_to_int(zero), 0)
        self.assertEqual(church_to_int(one), 1)
        self.assertEqual(church_to_int(two), 2)
        self.assertEqual(church_to_int(three), 3)

    def test_int_to_church(self):
        self.assertEqual(church_to_int(int_to_church(0)), 0)
        self.assertEqual(church_to_int(int_to_church(5)), 5)
        self.assertEqual(church_to_int(int_to_church(10)), 10)

    def test_add(self):
        self.assertEqual(church_to_int(add(zero, one)), 1)
        self.assertEqual(church_to_int(add(one, two)), 3)
        self.assertEqual(church_to_int(add(three, two)), 5)

    def test_mul(self):
        self.assertEqual(church_to_int(mul(zero, three)), 0)
        self.assertEqual(church_to_int(mul(one, three)), 3)
        self.assertEqual(church_to_int(mul(two, three)), 6)

    def test_exp(self):
        self.assertEqual(church_to_int(exp(two, zero)), 1)  # 2^0 = 1
        self.assertEqual(church_to_int(exp(two, one)), 2)  # 2^1 = 2
        self.assertEqual(church_to_int(exp(two, three)), 8)  # 2^3 = 8

    def test_get_number_predefined(self):
        self.assertEqual(church_to_int(get_number("zero")), 0)
        self.assertEqual(church_to_int(get_number("one")), 1)
        self.assertEqual(church_to_int(get_number("two")), 2)
        self.assertEqual(church_to_int(get_number("three")), 3)

    def test_get_number_from_int(self):
        self.assertEqual(church_to_int(get_number("4")), 4)
        self.assertEqual(church_to_int(get_number("10")), 10)

    def test_get_number_invalid(self):
        self.assertIsNone(get_number("invalid"))

    def test_full_calculator_operations(self):
        # Проверим основные операции через ввод
        self.assertEqual(church_to_int(add(get_number("two"), get_number("three"))), 5)
        self.assertEqual(church_to_int(mul(get_number("two"), get_number("three"))), 6)
        self.assertEqual(church_to_int(exp(get_number("two"), get_number("three"))), 8)

    # Проверка отрицательных чисел
    def test_negative_numbers(self):
        self.assertIsNone(get_number("-1"))  # Нельзя преобразовать отрицательное число
        self.assertIsNone(get_number("-100"))
        self.assertIsNone(get_number("-1"))

    def test_fractional_numbers(self):
        self.assertIsNone(get_number("2.5"))  # Дробные числа не поддерживаются
        self.assertIsNone(get_number("0.1"))
        with self.assertRaises(TypeError):  # Проверка операции с дробным числом
            add(int_to_church(2.5), one)

    def test_missing_predefined_numbers(self):
        self.assertIsNone(get_number("five"))  # Неопределённое текстовое представление
        self.assertIsNone(get_number("ten"))  # Только целые числа или определённые слова

    def test_large_numbers(self):
        large_church = int_to_church(100)
        self.assertEqual(church_to_int(large_church), 100)
        self.assertEqual(church_to_int(add(large_church, int_to_church(50))), 150)
        self.assertEqual(church_to_int(mul(large_church, int_to_church(2))), 200)
