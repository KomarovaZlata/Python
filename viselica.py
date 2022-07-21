#***
#РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
#***
import random
#***
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
#***
def GenVis():
    HANGMAN_PICT = ['''
  +---+
      |
      |
      |
     ===''',''' 
  +---+
  0   |
      |
      |
     ===''','''
  +---+
  0   |
  |   |
      |
     ===''','''
  +---+
  0   |
 /|   |
      |
     ===''','''
  +---+
  0   |
 /|\  |
      |
     ===''','''
  +---+
  0   |
 /|\  |
 /    |
     ===''','''
  +---+
  0   |
 /|\  |
 / \  |
     ===''']

    return HANGMAN_PICT

def GenSlov():
    words = {'животные':'акула аист белка бобр бегемот верблюд волк выдра голубь гусь дрозд дятел дикобраз еж енот жираф журавль заяц зебра зубр индюк иволга кабан косатка кот коршун кролик лама лев лиса ленивец медведь мышь носорог норка орел обезяна олень осёл петух паук панда пингвин рысь рак синица слон сова суслик тигр тюлень уж улитка филин хорек хомяк цапля чайка черепаха'.split(),
    'цвета':'красный оранжевый желтый зеленый голубой синий фиолетовый розовый черный белый коричневый'.split(),
    'фрукты':'яблоко груша апельсин персик слива ананас дыня киви'.split()}



    return words

def VyborSlova (spisok,uS):
    if uS == 'Л':
        for i in range(len(list(spisok.keys()))):
            print('Для выбора категории'+list(spisok.keys())[i]+' введите '+str(i))

        while True:
            katSlov = input()
            if not katSlov.isdigit():
                print('Вводить можно только цифры.')
            else:
                katSlov = int(katSlov)
                if katSlov > len(list(spisok.keys())):
                    print('Вы ввели неверное число.')
                else:
                    break

        kategorya = list(spisok.keys())[katSlov]
    else:
        kategorya = random.choice(list(spisok.keys()))

    indexSlova = random.randint(0,len(spisok[kategorya])-1)

    return [spisok[kategorya][indexSlova],kategorya]

def vyborUS():
    while True:
        print('Выберите уровень сложности')
        print('Введите "Л" для лёгкого уровня')
        print('Введите "С" для среднего уровня')
        print('Введите "Т" для трудного уровня')
        uroven = input()
        uroven = uroven.upper()
        if len(uroven) != 1:
            print('Надо вводить только один символ.')
        elif uroven not in 'ЛСТ':
            print('Вы ввели неправильную букву.')
        else:
            return uroven

    game = random.randint(0,len(spisok)-1)
    slovo = spisok[game]
    return slovo

def proverka(strbukv):
    while True:
        print('Введите букву')
        buk = input()
        buk = buk.lower()
        if len(buk) !=1:
            print('Ввести можно только одну букву')
        elif buk not in ('абвгдежзийклмнопрстуфхцчшщьыъэюя'):
            print('Вводить можно только буквы русского алфавита')
        elif buk in strbukv:
            print('Вы уже вводили эту букву')  
        else:
            return buk  

def displayboard(NasVis,errorBuk,yesBuk,SicretSl,urS,kS):
    if urS in 'ЛС':
        print(kS)
    print(NasVis[len(errorBuk)])
    print()
    print('Ошибочные буквы:' +errorBuk)
    print()

    shablon = '_'*len(SicretSl)
    
    for i in range(len(SicretSl)):
        if SicretSl[i] in yesBuk:
            shablon = shablon[:i]+SicretSl[i]+shablon[i+1:]
    
    for s in shablon:
        print(s,end=' ')
    print()

def PlayAgain():
     # Создаём бесконечный цикл
    while True:
        #Задаём вопрос и получаем ответ
        print('Хотите ли Вы продолжить игру?') 
        ot = input()
        ot = ot.lower()
        #Проверяем ответ игрока на совпадение со следующими фразами
        #'Да' 'ДА' 'да' 'д' 'Yes' 'YES' 'yes' 'y'
        if (ot == 'Да') or (ot == 'да') or (ot == 'ДА') or (ot == 'д') or (ot == 'Yes') or (ot == 'yes') or (ot == 'YES') or (ot == 'y'):
            return True
        #Если в ответе есть совпадение, то переменной присваиваем значение True
        #Прерываем цикл командой return 
        #Проверяем ответ игрока на совпадение со следующими фразами
        #'Нет' 'НЕТ' 'нет' 'н' 'No' 'NO' 'no' 'n' 
        #Если в ответе есть совпадение, то переменной присваиваем значение True
        elif (ot == 'Нет') or (ot == 'НЕТ') or (ot == 'нет') or (ot == 'н') or (ot == 'No') or (ot == 'NO') or (ot == 'no') or (ot == 'n'):
            return False
        #Если ответ игрока не совпадает с фразами
        #Сообщаем игроку о том, что не поняли ответ
        else:
            print('Мы не поняли Ваш ответ')
            print('Дайте Ваш ответ ещё раз')


#***
#ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
#***
vis = GenVis()
wordsS = GenSlov()

strokaErrorB = ''
strokaYesB = ''
GameOver = False

urovenSl = vyborUS()
SicretSlovo,katSlov = VyborSlova(wordsS,urovenSl)






while True:
    displayboard(vis,strokaErrorB,strokaYesB,SicretSlovo,urovenSl,katSlov)
    vvedenyaB = proverka(strokaErrorB + strokaYesB)

    if vvedenyaB in SicretSlovo:
        strokaYesB = strokaYesB + vvedenyaB

        endGame = True
        for i in range (len(SicretSlovo)):
            if SicretSlovo[i] not in strokaYesB:
                endGame = False
                break
        if endGame:
            print('ДА! Секретное слово - "'+SicretSlovo+'". Поздравляем,Вы угадали!')   
            GameOver = True
    else:
        strokaErrorB = strokaErrorB + vvedenyaB

        if len(strokaErrorB) ==len(vis) -1:
            displayboard(vis,strokaErrorB,strokaYesB,SicretSlovo,urovenSl,katSlov)
            print('''             У Вас закончились все попытки!
            Названо ошибочных букв: "'''+str(len(strokaErrorB))+'''"       
            Угадано букв:    "'''+str(len(strokaYesB))+'''"      
            Было загадано слово: "'''+SicretSlovo+'''" ''' )
            GameOver = True

    if GameOver:
        if PlayAgain():
            urovenSl = vyborUS()
            SicretSlovo,katSlov = VyborSlova(wordsS,urovenSl)

            strokaErrorB = ''
            strokaYesB = ''
            GameOver = False
        else:
            break


           