def febonachi_sequence(num_terms):
    sequence = [0,1]

    for _ in range(2, num_terms):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

print('Sveiki atvyke i Fabonachio sekos moduliacija')

num_terms = int(input('Iveskite norimu sekos skaiciu kieki '))

seka = febonachi_sequence(num_terms)

for term in febonachi_sequence(num_terms):
    print(term)