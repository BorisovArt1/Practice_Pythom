import math

def second_number():
    second_number1 = float(input("Введите второе число>>  "))
    return second_number1

prod = 'y'
while prod == 'y':
    f_num = float(input("Введите первое число>>  "))
    oper = input("Введите операцию>>  ")
    if oper == '+':
        s_num = second_number()
        print(f_num + s_num)
    elif oper == '-':
        s_num = second_number()
        print(f_num - s_num)
    elif oper == '*':
        s_num = second_number()
        print(f_num * s_num)
    elif oper == '/':
        s_num = second_number()
        if s_num == 0:
            print("На ноль делить нельзя!")
        else:
            print(f_num / s_num)
    elif oper == '%':
        s_num = second_number()
        print(f_num % s_num)
    elif oper == '**':
        s_num = second_number()
        print(f_num ** s_num)
    elif oper == 'sqrt':
        print(math.sqrt(f_num))
    else:
        print('Ошибка')
    prod = input("Введите 'у', чтобы продолжить или любую клавишу, чтобы завершить процесс>>  ")

