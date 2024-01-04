import random

random_number = random.randint(1, 100)
sk = None
sk = int(input('Atspekite skaiciu: '))
k = 1

while(sk != random_number):
    if(random_number > sk):
        print('too low')

    if(random_number < sk):
        print('too high')

    if(sk < 1 or sk > 100):
        print('Ka tu darai nevykeli ')

    sk = int(input('Spekite dar karta: '))
    k = k + 1

print(f'Atspejai iš {k} karto')