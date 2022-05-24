import random
#print("Привет, как тебя зовут?")
#s = input()
#print(s+', Очень рада тебя видеть')
#st = 'сыр '*5
#print(st)
#ch = (2+10)/2*3+2
#print(ch)
s = random.randint(1,10)
print('сгенерировано число: '+str(s))
for i in range(5):
    x = random.randint(1,10)
    s = s + x
    print('s+x='+str(s))