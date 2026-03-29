class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


if __name__ == "__main__":
    calc = Calculator()
    print("Addition: 5 + 3 =", calc.add(5, 3))
    print("Subtraction: 10 - 4 =", calc.subtract(10, 4))
    print("Multiplication: 6 * 7 =", calc.multiply(6, 7))
    print("Division: 20 / 5 =", calc.divide(20, 5))