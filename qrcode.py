#Importações
from tkinter import *
import pyqrcode

#tela
tela = Tk()
tela.geometry('640x480')
tela.resizable(width = 0, height = 0)
tela.title('Gerador de QRcode')
tela['bg'] = "gray"

#Função que gera o QRcode
def gerar():
    try:
        link = str(url.get())
        ti = str(titulo.get())
        qr = pyqrcode.create(link)
        qr.png(ti, scale = 10)
        msg3['text'] = 'SUCESSO'
    except:
        msg3['text'] = 'E R R O'


#Mensagem 
msg = Label (tela, text = "Digite uma URL")
msg['bg'] = "gray"
msg.pack(side = TOP)
#Input com a URL do QRcode
url = Entry (tela, width = 60)
url.pack(side = TOP)

#Botão que dispara a função de gerar QRcode
gerador = Button(tela, width = 40, text = "gerar", command = gerar)
gerador.pack(side = BOTTOM)

#Mensagem 2
msg2 = Label (tela, text = 'Digite o nome do arquivo (com a extensão .png)')
msg2.place (x = 190, y = 200)
msg2['bg'] = 'gray'
titulo = Entry (tela, width = 60)
titulo.place(x = 140, y = 240)

#Mensagem de erro
msg3 = Label (tela, text = ' ')
msg3['bg'] = 'gray'
msg3.pack(side = TOP)

tela.mainloop()

