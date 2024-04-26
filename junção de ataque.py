import sys
import subprocess

if len(sys.argv) != 4:
    print("Uso: python3 script.py -w - arquivo.cap")
    sys.exit(1)

# Captura os argumentos da linha de comando
modo = sys.argv[1]
dicionario = sys.argv[2]
arquivo_cap = sys.argv[3]

# Verifica se o modo está correto
if modo != "-w":
    print("Modo inválido. Use -w para indicar entrada de dicionário.")
    sys.exit(1)

# Subprocesso para chamar o aircrack-ng
p = subprocess.Popen(['aircrack-ng', modo, dicionario, arquivo_cap], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Captura a saída do processo
output, error = p.communicate()

# Verifica se houve algum erro
if error:
    print("Erro:", error.decode('utf-8'))
else:
    print(output.decode('utf-8'))  # Imprime a saída
