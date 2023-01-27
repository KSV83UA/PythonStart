#1 Construct an integer from the string "123"
str = "123"
print("Old type",type(str))
str = int(str)
print("New type",type(str))

#2 Construct a float from the integer 123
number = 123
print("Old type",type(number))
number = float(number)
print("New type",type(number))

#3 Construct an integer from the float 12.345
number_float = 12.345
print("Old type",type(number_float))
number_float = int(number_float)
print("New type",type(number_float))

#4 Write a Python-script that detects the last 4 digits of a credit card
per1, per2, per3, per4 = input('input number card (0000-0000-0000-0000): ').split('-')
print('the last 4 digits of credit card: ' + per4)

#5 Write a Python-script that calculates the sum of the digits of a three-digit number
number = int(input('Input three-digit number: '))
print((number//100)+(number//10%10)+(number%10))

#6 Write a program that calculates and displays the area of a triangle if its sides are known
tri1 = int(input('input 1 side'))
tri2 = int(input('input 2 side'))
tri3 = int(input('input 3 side'))
p = (tri1 + tri2 + tri3) / 2
area = (p * (p - int(tri1)) * (p - int(tri2)) * (p - int(tri3)))**0.5
print('area of a triangle: ', area)
#7 Write a Python-script that calculates the sum of the digits of a number
number = int(input('input number: '))
sum = 0
while number != 0:
    sum = sum + number % 10
    number = number // 10
print("Calculates the sum of digits:", sum)

#8 Determine the number of digits in a number
number = int(input('input number: '))
count = 0
while number:
    count += 1
    number = number // 10
print('the number of digits in a number: ', count)

#9 Print the digits in reverse order
number = int(input('input number: '))
revers = 0
while number > 0:
    tmp = number % 10
    number = number // 10
    revers = revers * 10
    revers = revers + tmp
print(revers)



