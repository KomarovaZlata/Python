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

def sravnenie(game,igrok):
    if game == igrok:
        sovpadenie = True
    else:
        sovpadenie = False
    return sovpadenie

def intro2():
    print('''  После сделанной вами ставки 
    женщина начала двигать напёрстки с невиданной скоростью

    После придвинула напёртки ближе к Вам
    Вы должны выбрать один из напёрстков,
    под которым по вашему мнению находится шарик''')

def otvet():
    print('Укажите номер выбранного вами напёрстка:')
    nap = input()
    while True:
        if nap.isdigit():
            if (nap in '123') and (len(nap)==1):
                nap = int(nap)
                break
            else:
                print('Нужно ввести только 1,2 или 3')
                nap = input()
        else:
            print('Нужно ввести только цифру')
            nap = input()
    return nap


#***
#ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
#***
many,minBig = nastroyki()
intro()
stavkaIgroka = proverka(many,minBig)
intro2()
napGame = random.randint(1,3)
napIgrok = otvet()
if sravnenie(napGame,napIgrok):
    print('Поздраляем!Вы выйграли!')
    many = many + stavkaIgroka
else:
    print('Очень жаль!Вы проиграли!')
    many = many - stavkaIgroka

print(many)