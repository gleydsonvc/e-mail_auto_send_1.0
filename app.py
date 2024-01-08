import os
import smtplib
from email.message import EmailMessage
from passe import senha
from nomes import nome, assunto, destinatario, mensagem

#Configurando email e senha

your_email = '#####################' #Aqui voce coloca seu e-mail/Put your E-mail here
email_password = senha #arquivo externo tem a variável senha com a sua senha no 2factor do google

#Criando uma mensagem

msg = EmailMessage()
msg['Subject'] =assunto
msg['From'] = your_email
msg['To'] = destinatario
msg.set_content(mensagem)

#Enviar o e-mail

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: #Podes trocar a porta smtp, google it!
    smtp.login(your_email,email_password)
    smtp.send_message(msg)

