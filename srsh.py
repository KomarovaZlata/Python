import random
# подключили модуль рандом
print("Привет, как тебя зовут?")
myname = input
#Поздоровались, спросили имя, ответ записать в переменную 

while True:
    s = random.randint(1,100)
    print("Я загадала число от 1 до 100.")
    #Программа загадала (сгенерировала) число от 1 до 100 и рассказала об этом игроку
    for i in range(10):
        #даём игроку 10  попыток отгадать число:
        print("Введи число от 1 до 100")
        y=input()
        # программа просит ввести число и записать введенное в переменную y
        while True:
            if y.isdigit():
                break
            else:
                print("Введи число.")
                y = input()
        y = int(y)
        #переводи число в строку
        if s > y:
            print("Твоё число меньше загаданого")
        if s < y:
            print("Твоё число больше загаданого")
        if  s == y:
            break 
    if s == y:
        print("Поздравляем! Ты выйграл.")
    if s != y:
        print("Увы! Загаданное число"+str(s))

    pr = True  
    print('Хочешь попробoвать ещё раз?')
    otvet = input()
    if (otvet == "да") or (otvet == "д") or (otvet == "yes") or (otvet == "y"):
        pr = False

    if pr:
        #игра прекращается
        break
