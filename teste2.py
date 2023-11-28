import subprocess
import time

def run_gdb_commands(binary_path):
    # Comandos GDB a serem executados
    gdb_commands = [
        "break calc",    # Define um breakpoint na função "calc"
        "run",           # Inicia a execução do programa
        "1 + 2",
        "next",          # Executa a próxima linha de código
        "next",          # Executa a próxima linha de código novamente
        "print v1",      # Imprime o valor da variável "v1"
        "print v2",
        "continue",      # Continua a execução até o próximo breakpoint
        "quit"           # Sai do GDB
    ]

    # Executa os comandos no GDB usando subprocess e captura a saída
    with subprocess.Popen(['gdb', binary_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as gdb_process:
        for command in gdb_commands:
            # Envia o comando para o GDB
            gdb_process.stdin.write(command + '\n')
            gdb_process.stdin.flush()
            time.sleep(0.1)

        # Agora, você pode processar a saída do GDB
        output, errors = gdb_process.communicate()

        # Verifica se houve algum erro
        if errors:
            print(f"Erro ao executar o GDB: {errors}")
        else:
            # Processa a saída do GDB como uma string no Python
            print("Saída do GDB:")
            print(output)

if __name__ == "__main__":
    # Caminho para o executável compilado
    executable_path = "./teste1"

    # Executa os comandos no GDB
    run_gdb_commands(executable_path)
