import random

def flip_coin():
    Monetos_puse = random.choice(['H', 'T'])
    return (Monetos_puse)

kartai = int(input('Kiek kartų mesite monetą? '))
i = 0
H = 0
T = 0

while i != kartai:
    p = flip_coin()
    print(p)
    if p == 'H':
        H += 1
    if p == 'T':
        T += 1
    i += 1

print(f'Išmetę monetą {kartai} kartų, heads atsivertė {H} kartų, o tails {T} kartų, ez game.')