class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def __add__(self, other):
        return Calculator(self.a + other.a, self.b + other.b)

    def sub(self):
        return self.a - self.b


if __name__ == "__main__":
    calc = Calculator(3, 5)
    print(calc.add())
    print(calc.sub())
    newCalc=Calculator(6,7)
    out=calc+newCalc
    print(out.a,out.b)
