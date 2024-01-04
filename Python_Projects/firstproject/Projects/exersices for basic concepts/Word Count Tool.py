def count(text):
    words = text.split()
    return len(words)


text = str(input('Iveskite paragrafa ar sakinius kuriuose norite suskaiciuoti zodzius '))
a = text.split()
print(a)
word_count = count(text)
print("\nWord count: ", word_count)