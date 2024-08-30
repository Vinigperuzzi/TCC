import tkinter as tk
from pygdbmi.gdbcontroller import GdbController

def submit_text():
    global gdbmi
    entered_text = entry.get()
    response = gdbmi.write(entered_text)
    
    output_text.delete(1.0, tk.END)

    for res in response:
        output_text.insert(tk.END, str(res) + "\n")


gdbmi = GdbController()
root = tk.Tk()
root.title("Vai e Vem GDBMI")

entry = tk.Entry(root, width=200)
entry.pack(pady=10)

submit_button = tk.Button(root, text="Submeter", command=submit_text)
submit_button.pack(pady=10)

output_text = tk.Text(root, width=150, height=20, wrap="word", bg="lightgrey")
output_text.pack(pady=10)

root.mainloop()
