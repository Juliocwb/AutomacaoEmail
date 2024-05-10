import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cadastro import EmailManager
import csv

class EmailEnvioInterface:
    def __init__(self, master):
        self.master = master
        self.create_widgets()
        self.email_manager = EmailManager()

    def create_widgets(self):
        self.label_destinatario = ttk.Label(self.master, text="Selecione o destinatário:")
        self.label_destinatario.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.destinatarios_combo = ttk.Combobox(self.master, values=self.carregar_destinatarios(), width=47)
        self.destinatarios_combo.grid(row=1, column=0, padx=10, pady=5)

        self.label_corpo_email = ttk.Label(self.master, text="Selecione o corpo de e-mail padrão:")
        self.label_corpo_email.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.corpo_email_combo = ttk.Combobox(self.master, values=self.carregar_corpos_email(), width=47)
        self.corpo_email_combo.grid(row=3, column=0, padx=10, pady=5)

        self.label_titulo_email = ttk.Label(self.master, text="Digite o título do e-mail:")
        self.label_titulo_email.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        self.titulo_email_entry = ttk.Entry(self.master, width=50)
        self.titulo_email_entry.grid(row=5, column=0, padx=10, pady=5)

        self.label_anexo = ttk.Label(self.master, text="Selecione o(s) anexo(s):")
        self.label_anexo.grid(row=6, column=0, sticky="w", padx=10, pady=5)

        self.anexos_listbox = tk.Listbox(self.master, width=50, height=3, selectmode=tk.MULTIPLE)
        self.anexos_listbox.grid(row=7, column=0, padx=10, pady=5)

        self.button_adicionar_anexo = ttk.Button(self.master, text="Adicionar Anexo", command=self.adicionar_anexo)
        self.button_adicionar_anexo.grid(row=8, column=0, padx=10, pady=5)

        self.button_enviar = ttk.Button(self.master, text="Enviar Email", command=self.enviar_email)
        self.button_enviar.grid(row=9, column=0, padx=10, pady=5)       

    def carregar_destinatarios(self):
        try:
            with open('emails_cadastrados.csv', 'r') as file:
                reader = csv.reader(file)
                destinatarios = [row[0] for row in reader]
            return destinatarios
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'emails_cadastrados.csv' não encontrado.")
            return []

    def carregar_corpos_email(self):
        try:
            with open('corpos_padrao.csv', 'r') as file:
                reader = csv.reader(file)
                corpos_email = [row[0] for row in reader]
            return corpos_email
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'corpos_padrao.csv' não encontrado.")
            return []

    def adicionar_anexo(self):
        anexo = filedialog.askopenfilename()
        if anexo:
            self.anexos_listbox.insert(tk.END, anexo)
        else:
            messagebox.showinfo("Erro", "Nenhum anexo selecionado!")

    def enviar_email(self):
        destinatario = self.destinatarios_combo.get()
        corpo_selecionado = self.corpo_email_combo.get()
        titulo_email = self.titulo_email_entry.get()
        anexos = self.anexos_listbox.get(0, tk.END)

        self.email_manager.enviar_email(titulo_email, corpo_selecionado, destinatario, attachments=anexos)

        messagebox.showinfo("Sucesso", "E-mail enviado com sucesso!")

def main():
    root = tk.Tk()
    app = EmailEnvioInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
