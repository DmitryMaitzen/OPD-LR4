import unittest
from LR3_web_app import solve


class TestSolveFunction(unittest.TestCase):

    def test_integer_quotients_two_different_roots(self):
        roots = solve("5", "2", "-12")[1:]
        self.assertEqual(round(roots[0], 4), -1.7620)
        self.assertEqual(round(roots[1], 4), 1.3620)

    def test_integer_quotients_two_identical_roots(self):
        root = solve("4", "4", "1")[1]
        self.assertEqual(round(root, 4), -0.5)

    def test_integer_quotients_no_real_roots(self):
        result = solve("5", "5", "5")[0]
        self.assertEqual(result, "Действительных корней нет.")

    def test_float_quotients(self):
        roots = solve("2.3", "-5.1", "-3.2")[1:]
        self.assertEqual(round(roots[0], 4), -0.5101)
        self.assertEqual(round(roots[1], 4), 2.7275)

    def test_empty_b_and_c_quotients(self):
        root = solve("11", "", "")[1]
        self.assertEqual(root, 0.0)

    def test_empty_c_quotient(self):
        roots = solve("6", "12", "")[1:]
        self.assertEqual(roots[0], -2.0)
        self.assertEqual(roots[1], 0.0)

    def test_zero_a_quotient(self):
        result = solve("0", "2", "-5")[0]
        self.assertEqual(result, "Введён некорректный коэффициент a. Попробуйте снова.")

    def test_a_quotient_invalid(self):
        result = solve("%", "2", "-3")[0]
        self.assertEqual(result, "Введён некорректный коэффициент a. Попробуйте снова.")

    def test_b_quotient_invalid(self):
        result = solve("5", "?", "-4")[0]
        self.assertEqual(result, "Введён некорректный коэффициент b. Попробуйте снова.")

    def test_c_quotient_invalid(self):
        result = solve("9", "-1", "&")[0]
        self.assertEqual(result, "Введён некорректный коэффициент c. Попробуйте снова.")


if __name__ == "__main__":
    unittest.main()
