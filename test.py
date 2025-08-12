import unittest
from main import add, subtract, multiply, divide, check, remainder
'''
# assertEqual
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)

# assertNotEqual
class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertNotEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertNotEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertNotEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertNotEqual(divide(4, 2), 3)
        self.assertNotEqual(divide(20, 5), 4)

class TestCheckTrueCases(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(63))
        self.assertTrue(check(220))


class TestCheckFalseCases(unittest.TestCase):
    def test_check(self):
        self.assertFalse(check(1))
        self.assertFalse(check(2))
        self.assertFalse(check(57))

class TestDivide(unittest.TestCase):
   def test_divide_success(self):
       self.assertEqual(divide(10, 2), 5)
       self.assertEqual(divide(6, 3), 2)
       self.assertEqual(divide(70, 2), 35)

   def test_divide_by_zero(self):
       self.assertRaises(ValueError, divide, 6, 0)
'''


class TestRemainder(unittest.TestCase):
    def test_remainder_normal_cases(self):
        # Проверка обычных случаев
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(15, 4), 3)
        self.assertEqual(remainder(20, 7), 6)
        self.assertEqual(remainder(0, 5), 0)  # 0 делится на любое число

    def test_remainder_negative_numbers(self):
        # Проверка отрицательных чисел
        self.assertEqual(remainder(-10, 3), 2)  # -10 = (-4)*3 + 2
        self.assertEqual(remainder(10, -3), -2)  # 10 = (-4)*(-3) - 2
        self.assertEqual(remainder(-10, -3), -1)  # -10 = (3)*(-3) - 1

    def test_remainder_by_zero(self):
        # Проверка деления на ноль с помощью assertRaises
        with self.assertRaises(ValueError):
            remainder(10, 0)
        with self.assertRaises(ValueError):
            remainder(0, 0)

    def test_remainder_edge_cases(self):
        # Проверка крайних случаев
        self.assertEqual(remainder(1, 1), 0)
        self.assertEqual(remainder(1, 2), 1)
        self.assertEqual(remainder(2, 1), 0)


if __name__ == '__main__':
    unittest.main()