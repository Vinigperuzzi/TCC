import tkinter as tk
from tkinter import scrolledtext
import subprocess

class GDBInterface:
    def __init__(self, master):
        self.master = master
        master.title("GDB Interface")

        self.create_widgets()

    def create_widgets(self):
        # Caixa de texto para inserir comandos GDB
        self.command_entry = tk.Entry(self.master)
        self.command_entry.pack(pady=10)

        # Botão para enviar comando GDB
        self.send_button = tk.Button(self.master, text="Enviar Comando", command=self.send_command)
        self.send_button.pack(pady=5)

        # Botão para exibir registros
        self.show_registers_button = tk.Button(self.master, text="Exibir Registros", command=self.show_registers)
        self.show_registers_button.pack(pady=5)

        # Área de texto para exibir a saída do GDB
        self.output_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=50, height=15)
        self.output_text.pack(pady=10)

    def send_command(self):
        # Obter o comando da caixa de texto
        command = self.command_entry.get()

        # Limpar a saída anterior
        self.output_text.delete('1.0', tk.END)

        try:
            # Executar o comando no GDB usando subprocess
            result = subprocess.run(["gdb", "-q", "-ex", command], capture_output=True, text=True)
            output = result.stdout

            # Exibir a saída na área de texto
            self.output_text.insert(tk.END, output)
        except Exception as e:
            # Exibir mensagens de erro, se houver
            self.output_text.insert(tk.END, f"Erro: {e}")

    def show_registers(self):
        # Função para exibir registros usando GDB
        self.send_command_with_output("info registers")

    def send_command_with_output(self, command):
        # Função para enviar um comando GDB e exibir a saída
        self.command_entry.delete(0, tk.END)
        self.command_entry.insert(0, command)
        self.send_command()

if __name__ == "__main__":
    root = tk.Tk()
    gdb_interface = GDBInterface(root)
    root.mainloop()
