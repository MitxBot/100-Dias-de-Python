import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

#Carrega Variáveis do .env
load_dotenv()

#Pega o e-mail e a senha(ou senha de app)das variáveis de ambiente
EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")

#Configurações do servidor SMTP do gmail e da porta TLS
smtp_server = "smtp.gmail.com"
smtp_port = 587

def enviar_email(destinatario,nome):

    assunto = "Teste de envio automático"

    mensagem = f"""
Olá {nome},

Este e-mail foi enviado automaticamente usando Python.

Tenha um ótimo dia!

Atenciosamente,
Marcos
"""
    
    msg = MIMEMultipart()

    msg["From"] = EMAIL
    msg["To"] = destinatario
    msg["Subject"] = assunto

    msg.attach(MIMEText(mensagem, "plain"))

    try:

        servidor = smtplib.SMTP(smtp_server, smtp_port)
        servidor.starttls()

        servidor.login(EMAIL, SENHA)

        servidor.send_message(msg)

        servidor.quit()

        print(f"Email enviado para {nome}")

    except Exception as e:
        print(f"Erro ao enviar email para {nome}")
        print(erro)

def main():

    with open("contatos.csv",newline="",encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for contato in leitor:

            enviar_email(
                contato["email"],
                contato["nome"]
            )

if __name__ == "__main__":
    main()