#Спрашиваем пользователя какое игровое имя он хотел бы взять.
nickname = input("Введите ваше игровое имя:") 
print (nickname, "сколько тебе лет?")

#Спрашиваем сколько лет пользователю.
age = int(input("Введите сколько вам лет:"))

#Проводим контроль возраста.
if  age >= 12:
    print("Доступ разрешен!")
elif age < 12: 
    print("УХАДИ! ОТОШОЛ! ОТОШОЛ Я СКОЗАЛ!")
else: 
    print("ТИ ШЁ БИЗГРАМОТЬНИЙ? ЛИБО ВВОДИ ПРАВИЛЬНОЕ ЧИСЛО ЛИБО УХАДИ!")

#Незнаю что это. А это же ГДЗ по математике)
print("Калькулятор для", nickname)
a = int(input("Первое число:"))
b = int(input("Второе число:"))
c = input("Введите действие:")

if c == "*":
    print(a * b)
   
elif c == "/":
    if b == 0:
        print("Уфф. Я я думал ты умнее...")
    else:
        print(a / b)
    
elif c == "+":
    print(a + b)

elif c == "-":
    print(a - b)

else:
    print("Ти дурачек?")

# 