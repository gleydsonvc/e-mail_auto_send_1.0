from tkinter import *
import os
import subprocess

c=os.path.dirname(__file__)
nomeArquivo=c+"/nomes.py" #não precisa criar esse arquivo, automaticamente o sistema vai criar pra voce///Se for sistema Windows, troque a barra antes do nomes.py por 2 barras invertidas \\



def impDados(): #função do que vai ser feito com os dados digitados
    arquivo=open(nomeArquivo, "w")
    arquivo.write(f'nome="{vnome.get()}"\n')
    arquivo.write(f'assunto="{vfone.get()}"\n')
    arquivo.write(f'destinatario="{vmail.get()}"\n')
    arquivo.write(f'mensagem="{vmsg.get("1.0",END).strip()}"\n\n')
    arquivo.write("\n\n")
    arquivo.close()

def executar_programa(): #função pra chamar o processo externo "app.py"
    subprocess.run(["python", "app.py"], bufsize=0)

def salvar_executar(): #Quando clicares em salvar e executar ela ativa as função anteriores
    impDados()
    executar_programa()
    


app=Tk()
app.title("Mensagem Rápida de E-mail") #Todo o texto entre "" (aspas) pode ser trocado.
app.geometry("500x300")
app.configure(background="#E0FFFF") #Cor meio que "padrão" mas voce pode trocar pelo nome ou pelo código (google it!)

Label(app, text="Nome", font="Sans" ,background="white", foreground="#009", anchor=W).place(x=10, y=10, width=480, height=20) #se quiser pode personalizar a fonte, o tamanho da fonte e o fundo
vnome=Entry(app) #Esse Entry é somente pra 1 linha, já o TEXT é pra várias linhas
vnome.place(x=10, y=30, width=480, height=20)

Label(app, text="Assunto", font="Sans" ,background="white", foreground="#009", anchor=W).place(x=10, y=60, width=480, height=20)
vfone=Entry(app)
vfone.place(x=10, y=80, width=480, height=20)

Label(app, text="E-mail Destinatário", font="Sans" ,background="white", foreground="#009", anchor=W).place(x=10, y=110, width=480, height=20)
vmail=Entry(app)
vmail.place(x=10, y=130, width=480, height=20)

Label(app, text="Mensagem", font="Sans" ,background="white", foreground="#009", anchor=W, wraplength=479).place(x=10, y=160, width=480, height=20)
vmsg = Text(app, wrap=WORD, height=2)
vmsg.place(x=10, y=180, width=480, height=80)

btn_executar = Button(app, text="Salvar e Enviar", command=salvar_executar)
btn_executar.place(x=10, y=270, width=90, height=20)






app.mainloop()
