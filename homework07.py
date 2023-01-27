# 1. Напишіть програму, яка порахує скільки літер «b» у введеному рядку тексту.
#in_str = str(input('input line: '))
import math

in_str = "bgbfgbbgfb"
counter = 0
index = 0
while index != -1:
    index = in_str.find('b', index)
    print(index)
    if index != -1:
        counter += 1
        index += 1
print('input b: ', counter)
# 2. Користувач вводить з клавіатури ім'я людини. Написати програму для перевірки введеного ім'я на
# валідність (мається на увазі, що, наприклад, в імені людини не може бути цифр, воно повинно починатися з
# великої літери, за якою повинні йти маленькі).
#name = str(input('input name: '))
name = "Serhii"
#name = name.strip()
if name.isalpha() and name[0].isupper() and name[1:].islower():
    print('correct name')
else:
    print('incorrect name')
# 3. Напишіть програму, яка обчислить суму всіх кодів символів рядка.
#in_str = str(input('input string: '))
in_str = "sdfsdf"
print(sum(map(ord, in_str)))
# 4. Виведіть на екран 10 рядків із значенням числа Pi. У першому рядку має бути 2 знаки після коми, у другому 3 і так далі.
print(str(math.pi))
for i in range(11):
    print(str(math.pi)[:i+4])
# 5. Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та вивести його на екран.
in_str = "sdfjdkjf fg dkfjhgdsflgkd hflsdjfhg dsfgkdfgdfg dfg dfg dfg"
out_str = list(in_str.split(" "))
print(max(out_str, key=len))

# 1. Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери).
# Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту. Напишіть програму, яка
# визначить найкоротше слово з написаних Вовочкою. Наприклад:
# aaaaaaa - Вовочка писав слово - "a"
# ititititit - Вовочка писав слово - "it"
# catcatcatcat - Вовочка писав слово - "cat"
in_str = "catcatcat aaaaa ititititi fsdd fgf"
out_str = in_str.split(" ")
out_list = []
for i_str in out_str:
    tmp_string = ' '
    index = 0
    #  как написать условие while после прохода блока, немогу найти.
    # Можно было бы убрать обьявление пустой временно строки
    while len(tmp_string):
        tmp_string = i_str.replace(i_str[0:index],'')
        index += 1
    out_list.append(i_str[0:index-1])
print(min(out_list))

# 2. Напишіть програму для очищення тексту від HTML-тегів. Більше про html-теги https://html5book.ru/html-tags/
# Також необхідно врахувати кілька особливостей:
# - крім одинарних тегів є парні теги, наприклад <div> </div>, тобто. перший тег відкриває, а другий закриває.
# - тег у собі може містити купу додаткової інформації. Наприклад <div id="rcnt" style="clear:both;position:relative;zoom:1">


# Я ТАК ПОНИМАЮ РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ
in_html = "<div>Гарантированный анализ:</b> протеин 0,0014%, жиры 0,00029%, зола 5,3%, влага 81%, кальций 5,2%, калий 0,026%, магний 0,000014%, натрий 0,000047%, фосфор 0,0011%</div>"
print(in_html)
res = 0
while res != -1:
    res = in_html.find('<')
    res2 = in_html.find('>')
    if res != -1:
        in_html = in_html[:res] + in_html[res2+1:]
    else:
        break #чтобы не было вывода кореектной строки два раза
    print(in_html)
