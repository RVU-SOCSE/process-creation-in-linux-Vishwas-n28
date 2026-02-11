#simplecalculator
"""def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y ==0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y
    
while True:
    A=int(input("Enter first number: "))
    B=int(input("Enter second number: "))
    print("select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide") 
    choice = input("Enter choice(1/2/3/4): ")
    if choice == '1':
        print(A, "+", B, "=", add(A, B))
    elif choice == '2':
        print(A, "-", B, "=", subtract(A, B))
    elif choice == '3':
        print(A, "*", B, "=", multiply(A, B))
    elif choice == '4':
        print(A, "/", B, "=", divide(A, B))
    else:
        print("Invalid input")
    break """
    
    #temperature conversion
'''def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
while True:
    print("Temperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter choice(1/2): ")
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid input")
    break '''
    
    #find the largest number among three numbers
def find_largest(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
largest = find_largest(num1, num2, num3)
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")


#find the smallest number amoing three numbers
def find_smallest(a, b, c):
    if (a <= b) and (a <= c):
        return a
    elif (b <= a) and (b <= c):
        return b
    else:
        return c
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
smallest = find_smallest(num1, num2, num3)
print(f"The smallest number among {num1}, {num2}, and {num3} is: {smallest}")
   