import win32com.client as win32
import csv
import os

class EmailManager:
    def __init__(self):
        self.destinatarios = []
        self.tipos_corpo_padrao = {}

    def cadastrar_emails(self, emails):
        for email in emails:
            if email.strip() != "":
                self.destinatarios.append(email.strip())
        self.salvar_emails()
        return self.destinatarios

    def cadastrar_corpo_email(self, tipo_corpo, corpo):
        self.tipos_corpo_padrao[tipo_corpo] = corpo
        self.salvar_corpos_padrao()
        return self.tipos_corpo_padrao

    def salvar_emails(self):
        with open('emails_cadastrados.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            for email in self.destinatarios:
                writer.writerow([email])

    def salvar_corpos_padrao(self):
        with open('corpos_padrao.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            for tipo, corpo in self.tipos_corpo_padrao.items():
                writer.writerow([tipo, corpo])

    def enviar_email(self, subject, body, to, cc=None, attachments=None):
        outlook = win32.Dispatch('Outlook.Application')
        mail = outlook.CreateItem(0)
        mail.Subject = subject
        mail.Body = body        
        for recipient in to:
            mail.Recipients.Add(recipient)
        if cc:            
            for recipient in cc:
                mail.Recipients.Add(recipient)            
        mail.Send()


def main():
    email_manager = EmailManager()

    # Exemplo de cadastro de e-mails
    emails = ["email1@example.com", "email2@example.com"]
    destinatarios_cadastrados = email_manager.cadastrar_emails(emails)
    print("Destinatários cadastrados:", destinatarios_cadastrados)

    # Exemplo de envio de email com destinatários em cópia
    subject = "Teste de Email"
    body = "Este é um teste de email."
    to = ["email3@example.com"]
    cc = ["email4@example.com"]
    email_manager.enviar_email(subject, body, to, cc)
    print("E-mail enviado com sucesso para:", to)
    print("Cópia carbono para:", cc)

if __name__ == "__main__":
    main()
