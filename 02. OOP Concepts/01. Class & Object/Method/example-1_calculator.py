class Calculator:
    brand = 'Casio MS990'

    def add(self, num1, num2):
        result = num1 + num2
        return result
    
    def deduct(self, num1, num2):
        result = num1 - num2
        return result
    
    def multiply(self, num1, num2):
        result = num1 * num2
        return result
    
    def divide(self, num1, num2):
        result = num1 + num2
        return result
    
calculate = Calculator()

add = calculate.add(15, 6)
print(add)

add = calculate.deduct(15, 6)
print(add)

add = calculate.multiply(15, 6)
print(add)

add = calculate.divide(15, 6)
print(add)