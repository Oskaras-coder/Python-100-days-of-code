def generate_fibonacci_sequence(num_terms):
    sequence = [0, 1]  # Initialize the sequence with the first two terms

    # Generate the Fibonacci sequence
    for _ in range(2, num_terms):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

# Main program
print("Welcome to the Fibonacci Sequence Generator!")

num_terms = int(input("How many terms of the Fibonacci sequence would you like to generate? "))

fibonacci_sequence = generate_fibonacci_sequence(num_terms)

print("The Fibonacci sequence is:")
for term in fibonacci_sequence:
    print(term)
