# Домашнє завдання:
# 1. Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.
import shlex

def conv1(line=str, number1=float, number2=float):
    return line + str(number1+number2)
print(conv1("line",7,8))
# 2. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*».
# Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.
def f_draw(w=int, h=int):
    print(f'{"*" * w}')
    for _ in range(h-2):
        print(f'*{" "* (w-2)}*')
    print(f'{"*" * w}')
f_draw(4,5)
# 3. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел.
# Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».
def f_search(item=int, s_list=list):
    for i in range(len(s_list)):
        print(s_list[i])
        if s_list[i] == item:
            return i
    return -1
print("number index: ", f_search(9,[5,7,6]))
# 4. Напишіть функцію, яка поверне кількість слів у текстовому рядку.
def f_split(in_str=str):
    a = []
    a = in_str.split()
    return len(a)
print("count string: ", f_split("sdfs sdfsdf sdfsddf dfg dfgs ddsf"))

# 5. Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents
def f_chang(dol):
    # словарь не переносил специально во вложенную функцию
    n_list_0 = {
         0: "",
         1:"one",
         2:"two",
         3:"three",
         4:"four",
         5:"five",
         6:"six",
         7:"seven",
         8:"eigth",
         9:"nine",
        10:"ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40:	"forty",
        50:	"fifty",
        60:	"sixty",
        70:	"seventy",
        80:	"eighty",
        90:	"ninety",
        100:"hundred",
        1000:"thohousand",
        1000000: "million",
        1000000000: "billion"
    }

    dec = ["dollars", "thohousand", "million","billion"]

    def get_str(dol_cen, n_list_0=list, name_p=str):
        str_l = ""
        if dol_cen == 0:
            return ""
        if not n_list_0.get(dol_cen):
            if(n_list_0[dol_cen // 100] != ''):
                str_l = n_list_0[dol_cen // 100] + " hundred"
            t = dol_cen % 100
            if n_list_0.get(t):
                str_l += " " + n_list_0[t] + " " + name_p
                return str_l
            else:
                str_l += " " + n_list_0[t//10 * 10] + " "+ n_list_0[t % 10] + " " + name_p
                return str_l
        else:
            return n_list_0[dol_cen] + " " + name_p

    dol_centos = round(dol % 1*100)
    centos_str = get_str(dol_centos, n_list_0, "centos")
    dol = int(dol // 1)
    str_out = ""
    for item in dec:
        tmp = dol % 1000
        dol = dol // 1000
        if tmp == 0:
            break;
        str_out = get_str(tmp,n_list_0,str(item)) + str_out

    return str_out + " " + centos_str

print(f_chang(1158112.21))
# 6. Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
# Наприклад: XXII -> 22


def f_rim(number:str):
    r = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV': 4,'IX':9,'XL':40,'XC':90,'CD':400, 'CM':900}
    sum = 0
    l = list(number)
    print(l)
    index = 0
    while 1:
        if index > len(l)-1:
            break

        if index+1 <= len(l)-1:
            if r.get(l[index] + l[index+1]):
                sum += r.get(l[index] + l[index+1])
                index += 2
            else:
                sum += r.get(l[index])
                index += 1
        else:
            sum += r.get(l[index])
            break
    return sum

print("RIM: ",f_rim('MXCXXVII'))
# if __name__ ==

