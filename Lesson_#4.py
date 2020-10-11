try:
    print(1/0)
except ZeroDivisionError:
    print("Иди учись! На ноль нельзя делить!")

# ФУНКЦИИ

# def имя_функции(аргумент_1, ..., аргумент_n):
#     <Тело функции>
#     return <Возвращаемое значение>
    
# def func():
#     print("Работа функции")

# func()

def func(arg_1, arg_2):
    return arg_1 * arg_2

print(func(2, 4))

# Проверка пароля
def password(nums):
    string = input("На мне кодовый замок, какой же пароль?:") 
    if nums == string: 
        print("Пароль верный!")
    else:
        print("Пароль неверный!")

password("Енот666")

# КулькулАтор
def calc(num_1, num_2, oper):
    if oper == '+':
        print(num_1 + num_2)
    elif oper == '-':
        print(num_1 - num_2)
    elif oper == '*':
        print(num_1 * num_2)
        if num_2 == 0:
            print("Сквад не может быть 0.")
        else:
            print(num_1 / num_2)
    elif oper == '/':
        print(num_1 / num_2)
    else:
        print("Ти дурачек?")
        
num_1 = int(input('1'))
num_2 = int(input('2'))


calc(num_1 / num_2)