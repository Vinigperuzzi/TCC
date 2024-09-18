import os
import pty
import subprocess
import time

class GDBController:
    def __init__(self):
        # Cria um pseudoterminal (pty)
        self.master, self.slave = pty.openpty()

        # Inicia o GDB em modo subprocesso
        self.gdb_process = subprocess.Popen(
            ['gdb', '--interpreter=mi2'],  # Usando a interface de máquina MI2
            stdin=subprocess.PIPE,         # Entrada padrão (enviar comandos)
            stdout=self.master,        # Saída padrão (ler respostas)
            stderr=self.master,        # Erros padrão
            universal_newlines=True       # Para trabalhar com strings (texto)                  # Bufferização em modo linha
        )

    def send_command(self, command):
        # Envia um comando para o GDB e lê a resposta
        self.gdb_process.stdin.write(command + '\n')
        self.gdb_process.stdin.flush()  # Garante que o comando é enviado

    def send_input_to_program(self, user_input):
        # Escreve a entrada para o programa em execução no pseudoterminal escravo (simula o stdin)
        os.write(self.slave, user_input.encode('utf-8') + b'\n')

    def read_output(self):
        # Lê a saída do GDB (incluindo a resposta para o comando enviado)
        output = ""
        while True:
            try:
                # Lê a saída do programa via pseudoterminal
                data = os.read(self.master, 1024).decode('utf-8')
                output += data
                if "(gdb)" in data:  # Quando o GDB retorna o prompt
                    break
            except OSError:
                break
        return output

    def close(self):
        # Fecha o subprocesso GDB
        if self.gdb_process:
            self.gdb_process.terminate()
            self.gdb_process.wait()

def interactive_loop():
    gdb = GDBController()
    
    try:
        while True:
            # Solicita um comando do usuário
            command = input("gdb> ")
            if command.lower() in ['exit', 'quit']:
                break
            elif command.startswith('input '):
                # Envia a entrada para o programa (usando o terminal escravo)
                user_input = command.split(' ', 1)[1]
                gdb.send_input_to_program(user_input)
            else:
                # Envia o comando para o GDB
                gdb.send_command(command)

            # Lê e imprime a saída do GDB (inclui o output do programa depurado)
            time.sleep(2)
            output = gdb.read_output()
            print(output)

    except KeyboardInterrupt:
        print("\nEncerrando o GDB...")

    finally:
        gdb.close()

if __name__ == '__main__':
    interactive_loop()
