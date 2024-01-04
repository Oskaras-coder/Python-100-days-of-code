def add(s1, s2):
    skaicius = s1 + s2
    return skaicius

def subtract(s1, s2):
    skaicius = s1 - s2
    return skaicius

def multiply(s1, s2):
    skaicius = s1 * s2
    return skaicius

def divide(s1, s2):
    if(s2 != 0):
        skaicius = s1 / s2
        return skaicius
    else:
        return print('Negalima dalinti is 0')

op = str(input("Pasirinkite operacija (+,-,*,/): "))

s1 = float(input('Pirmas skaicius: '))
s2 = float(input('Antras skaicius: '))

if(op == '+'):
    atsakymas = add(s1, s2)

elif(op == '-'):
    atsakymas = subtract(s1, s2)

elif(op == '*'):
    atsakymas = multiply(s1, s2)

elif(op == '/'):
    atsakymas = divide(s1, s2)

print('Atsakymas ', atsakymas)