#***
#РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
#***
import random
#***
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
#***

#функции настроек
def nastroyki():
    print("ИГРА'НАПЁРСТКИ'")
    print()
    print('АВТОР:"Комарова Злата"')
    print()
    print('Версия 1.0')
    print()
    print("Введите сколько денег у игрока")
    dengi = input()
    while True:
        if dengi.isdigit():
            dengi = int(dengi)
            break
        else:
            print('Надо вводить только цифры')
            dengi = input()

    print("Введите сумму минимальной ставки")
    minStavka = input()
    while True:
        if minStavka.isdigit():
            minStavka = int(minStavka)
            break
        else:
            print("Надо вводить только цифры")
            minStavka = input()

    return[dengi,minStavka]

def intro():
    print("Однажды человек гулял по огромной городской площади,ему было скучно.")
    print()
    print("Часы тянулись необычайно долго,пока он не увидел небольшой шатёр.")
    print()
    print("Человек зашёл в шатёр и увидел там маленький стол,на котором лежало три напёрстка.")
    print()
    print("За столом сидела пожилая женщина,сразу предложившая сыграть")
    print()
    print("Человек согласился,решившись попытать удачу и развеить скуку")
    print()
    print("Сможет ли он выйграть?Помоги ему!")

def proverka(dengi,minStavka):
    print("Сделайте вашу ставку")
    stavka = input()
    while True:
        if stavka.isdigit():
            # переведи строку в число
            stavka = int(stavka)
            # проверяем, что ставка больше минимальной
            if stavka > minStavka:
                # проверяем, что ставка меньше количества денег у игрока
                if stavka > dengi:
                    print("Ставка не может быть больше суммы денег игрока")
                    stavka = input()
                else:
                    break
            else:
                print("Ставка не может быть меньше минимальной")
                stavka = input()
        else:
            print("Надо вводить только цифры")
            stavka = input()
    return stavka



#***
#ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
#***

many,minBig = nastroyki()

intro()