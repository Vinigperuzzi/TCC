import subprocess

def run_gdb_commands(binary_path):
    # Comandos GDB a serem executados
    gdb_commands = [
        "break 5",    # Define um breakpoint na função "calc"
        "run",           # Inicia a execução do programa
        "print i",
        "continue",      # Continua a execução até o próximo breakpoint
        "quit"           # Sai do GDB
    ]

    # Executa os comandos no GDB usando subprocess e captura a saída
    with subprocess.Popen(['gdb', binary_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, universal_newlines=True) as gdb_process:
        for command in gdb_commands:
            # Envia o comando para o GDB
            gdb_process.stdin.write(command + '\n')
            gdb_process.stdin.flush()

        # Coleta a saída do GDB linha por linha
        output_lines = []
        while True:
            line = gdb_process.stdout.readline()
            if not line:
                break
            output_lines.append(line)
            print(line, end='')

        # Obtém a saída do GDB como uma string
        output, errors = gdb_process.communicate()

        # Imprime a saída do GDB
        print("\n\n\n\n\n\n\nTudo o que vier agora é gerado pelo python:\n\n")
        print("\nSaída final do GDB:")
        print(output)

        # Imprime as linhas coletadas durante a execução
        print("\nLinhas coletadas durante a execução:")
        for line in output_lines:
            print(line, end='')

        # Verifica se houve algum erro
        if errors:
            print(f"Erro ao executar o GDB: {errors}")

if __name__ == "__main__":
    # Caminho para o executável compilado
    executable_path = "./test"

    # Executa os comandos no GDB
    run_gdb_commands(executable_path)
