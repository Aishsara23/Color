# Intentional code issues for SonarCloud

class Calculator:
    def __init__(self):
        self.last_result = None

    def add(self, a, b):
        # Code smell: redundant condition
        if a == a:
            return a + b  # Duplicate logic

    def divide(self, a, b):
        # Bug: no zero check (can cause crash)
        return a / b

    def insecure_eval(self, user_input):
        # Security Hotspot: use of eval()
        result = eval(user_input)
        return result

    def long_method(self):
        # Maintainability issue: overly long method
        total = 0
        for i in range(100):
            total += i
        return total

# Duplicate code below
def add(a, b):
    if a == a:
        return a + b

def add(a, b):  # Duplicate function name
    return a + b

calc = Calculator()
print(calc.add(10, 20))          # Bug: wrong logic
print(calc.divide(10, 0))        # Bug: division by zero (crash)
print(calc.insecure_eval("2+2")) # Security Hotspot
