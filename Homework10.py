# Домашнє завдання:
#  Необхідно підготувати звіт про витрати членів родини на новорічні свята.
# Звіт повинен включати наступне:
# 1. Яка загальна сума витрат по кожній категорії товарів?
# 2. Скільки грошей витратив кожен член родини?
# 2. Яку кількість покупок та на яку загальну суму зробив введений користувачем через input член родини?
from decimal import *
def get_all_payment(in_l = list, index_c = 3):
    g_list = {}
    for index in in_l:
        if not g_list.get(index[index_c]):
            g_list[index[index_c]] = Decimal(index[2])
        else:
            g_list[index[index_c]] += Decimal(index[2])
    return g_list

def get_user_info(in_name, in_l):
    # допускаю, что мы не считали до этого загальну килькисть грошей ним потраченых
    x = {"name":"","pokupok":0,"summa":Decimal(0)}
    x["name"] = in_name
    flag = 0
    for i in in_l:
        if i[1].lower() == in_name.lower():
            x['pokupok'] += 1
            x['summa'] += Decimal(i[2])
    return x
f = open("test.txt", "r")
x = []
index = 0
for line in f:
    t = list(line.split())
    if len(t) > 4:
        x.append([t[0],t[1]+" "+t[2],t[3][:-1],t[4]])
    else:
        x.append([t[0],t[1],t[2][:-1],t[3]])
print(get_all_payment(x))
print(get_all_payment(x,1))
user = input("input name user: ")
print(get_user_info(user, x))
f.close()