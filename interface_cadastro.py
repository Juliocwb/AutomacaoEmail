import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cadastro import EmailManager

class EmailCadastroInterface:
    def __init__(self, master):
        self.master = master
        self.create_widgets()
        self.email_manager = EmailManager()

    def create_widgets(self):
        self.label_email = ttk.Label(self.master, text="Digite os e-mails (separados por vírgula):")
        self.label_email.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.email_entry = ttk.Entry(self.master, width=50)
        self.email_entry.grid(row=1, column=0, padx=10, pady=5)

        self.button_cadastrar_email = ttk.Button(self.master, text="Cadastrar E-mails", command=self.cadastrar_emails)
        self.button_cadastrar_email.grid(row=1, column=1, padx=10, pady=5)

        self.label_tipo_corpo = ttk.Label(self.master, text="Digite o tipo de corpo padrão:")
        self.label_tipo_corpo.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.tipo_corpo_entry = ttk.Entry(self.master, width=50)
        self.tipo_corpo_entry.grid(row=3, column=0, padx=10, pady=5)

        self.label_corpo_email = ttk.Label(self.master, text="Digite o corpo de e-mail padrão:")
        self.label_corpo_email.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        self.corpo_email_text = tk.Text(self.master, width=50, height=10)
        self.corpo_email_text.grid(row=5, column=0, padx=10, pady=5)

        self.button_cadastrar_corpo = ttk.Button(self.master, text="Cadastrar Corpo de E-mail", command=self.cadastrar_corpo_email)
        self.button_cadastrar_corpo.grid(row=6, column=0, padx=10, pady=5)

    def cadastrar_emails(self):
        emails = self.email_entry.get().split(",")
        destinatarios_cadastrados = self.email_manager.cadastrar_emails(emails)
        messagebox.showinfo("Sucesso", "Endereços de e-mail cadastrados com sucesso!")
        self.email_entry.delete(0, 'end')

    def cadastrar_corpo_email(self):
        tipo_corpo = self.tipo_corpo_entry.get()
        corpo_email = self.corpo_email_text.get("1.0", "end-1c")
        tipos_corpo_padrao_cadastrados = self.email_manager.cadastrar_corpo_email(tipo_corpo, corpo_email)
        messagebox.showinfo("Sucesso", "Corpo de e-mail padrão cadastrado com sucesso!")
        self.tipo_corpo_entry.delete(0, 'end')
        self.corpo_email_text.delete("1.0", tk.END)

def main():
    root = tk.Tk()
    app = EmailCadastroInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
