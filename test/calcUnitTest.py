import unittest
from src.Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_add(self):
        calc = Calculator(3, 5)
        res = calc.add()
        self.assertEqual(res, 8)  # add assertion here

    def test_sub(self):
        calc = Calculator(8, 4)
        res = calc.sub()
        self.assertEqual(4, 4)

    def test_obj_add(self):
        calc = Calculator(3, 5)
        newCalc = Calculator(6, 7)
        out = calc + newCalc
        self.assertEqual(out.a,9)
        self.assertEqual(out.b,12)


if __name__ == '__main__':
    unittest.main()
