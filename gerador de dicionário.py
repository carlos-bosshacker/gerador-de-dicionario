import itertools

def generate_dictionary():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    min_length = 1
    max_length = 8

    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            word = ''.join(combination)
            yield word

# Exemplo de uso
for word in generate_dictionary():
    print(word)