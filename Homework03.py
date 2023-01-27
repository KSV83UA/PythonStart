# 1. Write a Python program to print the number entered by user only if the
# number entered is negative.
num = int(input('input number negative number '))
if num > 0:
    print('you input unnegative number ')
else:
    print('you input number: ',num)
# 2. Write a Python program to check if the value a is less than 20 or not.
num = int(input('input number '))
if num < 20:
    print('less than 20')
else:
    print('more than 20')
# 3. Write a Python program to check if a given number is Zero or Not.
if num:
    print('not Zero')
else:
    print('Zero')
# 4. Write a Python program to check if a given number is Even or Odd.
if num % 2:
    print('Odd')
else:
    print('Even')
# 5. Write a Python program to find largest number among three numbers
num1 = int(input('number 1'))
num2 = int(input('number 2'))
num3 = int(input('number 3'))
if num1 > num2 and num1 > num3:
    print('num1 is largest: ',num1)
elif num2 > num3:
    print('num2 is largest: ', num2)
else:
    print('num3 is largest: ', num3)
# entered by user