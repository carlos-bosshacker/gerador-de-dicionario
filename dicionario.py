import itertools
import platform  # Módulo para obter informações sobre o sistema operacional

def generate_dictionary():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    min_length = 1
    max_length = 8

    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            word = ''.join(combination)
            yield word

def main():
    if platform.system() != 'Linux':
        print("Este script é projetado para ser executado em sistemas Linux.")
        return
    
    print("Gerando dicionário de senhas...")
    for word in generate_dictionary():
        print(word)

if __name__ == "__main__":
    main()
