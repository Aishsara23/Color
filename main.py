class Calculator:
    def __init__(self):
        self.last_result = None

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def secure_eval(self, user_input):
        # Replace eval with a safe alternative (e.g., limited math parser)
        try:
            allowed_chars = "0123456789+-*/(). "
            if all(c in allowed_chars for c in user_input):
                return eval(user_input)
            else:
                return "Error: Unsafe expression"
        except Exception:
            return "Error: Invalid expression"

    def long_method(self):
        return sum(range(100))


if __name__ == "__main__":
    calc = Calculator()
    print("Add:", calc.add(10, 20))
    print("Divide:", calc.divide(10, 0))
    print("Eval:", calc.secure_eval("2+2"))
