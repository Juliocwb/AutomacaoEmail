import tkinter as tk
from tkinter import ttk
from interface_cadastro import EmailCadastroInterface
from interface_envio import EmailEnvioInterface

class EmailApp:
    def __init__(self, master):
        self.master = master
        master.title("Aplicativo de E-mail")

        self.create_widgets()

    def create_widgets(self):
        self.tabControl = ttk.Notebook(self.master)
        self.tabCadastro = ttk.Frame(self.tabControl)
        self.tabEnvio = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tabCadastro, text='Cadastro')
        self.tabControl.add(self.tabEnvio, text='Envio')
        self.tabControl.pack(expand=1, fill="both")

        self.create_cadastro_interface()
        self.create_envio_interface()

    def create_cadastro_interface(self):
        self.cadastro_interface = EmailCadastroInterface(self.tabCadastro)

    def create_envio_interface(self):
        self.envio_interface = EmailEnvioInterface(self.tabEnvio)

def main():
    root = tk.Tk()
    app = EmailApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
