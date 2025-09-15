class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b

# ✅ Fixing missing parentheses and indentation
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

m = Math(a, b)

print("Add:", m.addition())
print("Sub:", m.subtraction())
print("Mul:", m.multiplication())
print("Div:", m.division())