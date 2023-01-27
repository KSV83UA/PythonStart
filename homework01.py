#Exercise 1. Write a Python-script that displays the message “Hello world"

print("Hello world")

#Exercise 2. Rewrite the first script to display three any messages.

print("Example 1")
print("Example 2")
print("Example hom01-exe-3.py")

#Exercise 3. Write a Python-script to reads values for the length and width of a
#rectangle and returns the area of the rectangle.

rec_length = float(input('input length > '))
rec_weidth = float(input('input weidth > '))
print( f'area of the rectangle: {rec_length * rec_weidth}')

#Exercise 4. Write a program that requests the user to enter two numbers and
#prints the sum, product, difference and quotient of the two numbers.

number1 = float(input("input number 1 > "))
number2 = float(input("input number 2 > "))
print(f'summa: {number1 + number2}')
print (f'product: {number1 * number2}')
print(f'difference: {number1 - number2}')
print(f'quotient of the two numbers: {number1 // number2}')

#Exercise 5. Write a program that reads in the radius of a circle and prints the
#circle’s diameter, circumference and area. Use the constant value 3.14159 for π.
#Do these calculations in output statements
radius = float(input("input radius circle: "))
print(f'diameter: {2 * radius}')
print(f'circumference :  {2 * 3.14159 * radius}')
print(f'area circly: {3.14159 * radius**2}')