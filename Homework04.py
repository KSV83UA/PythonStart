# 1. Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці. На одному поверсі - 4
# квартири. Напишіть програму, яка від користувача отримує номер квартири та виводить для заданої квартири номер
# 'їзду, поверху та номер на поверсі. Якщо такої квартира немає в цьому будинку, то необхідно повідомити користувача про це.

import math
all_flat = 4*9*4
#flat = int(input('input number flat'))
flat = 73
if 0 < flat <= all_flat:
    entrance = math.ceil(flat / 36)
    floor = math.ceil(flat / 4) - (entrance-1) * 9
    number_flat = (flat % 4) or 4
    print('entrance', entrance)
    print('floor', floor)
    print('number flat',number_flat)
else:
    print('incorrect number of flat')


# 2. Написати програму, яка буде повертати для заданого року кількість днів. Рік є високосним, якщо він кратний 4,
# але не кратний 100, а також якщо він кратний 400
#year_date = int(input('date: '))
year_date = 2100
if (not (year_date % 4) or not (year_date % 400)) and year_date % 100:
    print('days 366')
else:
    print('days 365')

# 3. Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої. Дано: A, B, C - сторони трикутника.
# Напишіть програму, яка вказує чи існує такий трикутник.
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a+b >c or a+c > b or b+c > a:
    print('good')
else:
    print('bad')