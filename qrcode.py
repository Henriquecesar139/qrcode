#Importações
from tkinter import *
import pyqrcode
import png
#tela
tela = Tk()
tela.geometry('640x480')
tela.resizable(width = 0, height = 0)
tela.title('Gerador de QRcode')
tela.iconbitmap('icon.ico')
tela['bg'] = "gray"

#Função que gera o QRcode
def gerar():
    try:
        #Caso o usuário não digite nada no campo de tamanho, a escala será 15
        try:
            tamanho = int (escala.get())
        except:
            tamanho = 15

        link = str(url.get())
        ti = str(titulo.get())
        qr = pyqrcode.create(link)
        qr.png(ti, scale = tamanho)
        msg3['text'] = 'SUCESSO'
    except:
        msg3['text'] = 'E R R O'


#Mensagem 
msg = Label (tela, text = "Digite uma URL", bg = 'gray')
msg.pack(side = TOP)
#Input com a URL do QRcode
url = Entry (tela, width = 60)
url.pack(side = TOP)

#Botão que dispara a função de gerar QRcode
gerador = Button(tela, width = 40, text = "gerar", command = gerar)
gerador.pack(side = BOTTOM)

#Mensagem 2
msg2 = Label (tela, text = 'Digite o nome do arquivo (com a extensão .png)', bg = 'gray')
msg2.place (x = 190, y = 200)
titulo = Entry (tela, width = 60)
titulo.place(x = 140, y = 240)

#Mensagem de erro
msg3 = Label (tela, text = ' ', bg = 'gray')
msg3.pack(side = TOP)

#Campo para definir o tamanho do qrcode
escala = Entry (tela, width = 5)
escala.place(x = 580, y = 240)

#Mensagem do campo de tamanho
escala_texto = Label (tela, text = 'Tamanho: ', bg = 'gray')
escala_texto.place(x = 570, y = 200)

tela.mainloop()
