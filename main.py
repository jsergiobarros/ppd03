# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter.scrolledtext import ScrolledText

import paho.mqtt.client as paho
from tkinter import *
from random import randrange,uniform
import time
class Cliente:
    def onMessage(self,client,userdata,message):
        print(f"messagem {str(message.payload.decode('utf-8'))}")
        self.insertTxt(str(message.payload.decode('utf-8')))
    def __init__(self):
        #self.client = Cliente()
        self.broker = 'mqtt.eclipseprojects.io'
        self.client = paho.Client("pessoa")
        self.client.on_message = self.onMessage
        self.client.connect(self.broker)

        self.client.loop_start()
        self.janela()
    def subscribe(self,temp,umi,velo):
        self.client.loop_stop()
        if temp!="0":
            print(temp)
            self.client.subscribe("Temperatura")
        if umi!="0":
            print(umi)
            self.client.subscribe("Umidade")
        if velo!="0":
            print(velo)
            self.client.subscribe("Velocidade")
        self.client.loop_start()

    def insertTxt(self,txt):  ###metodo de INSERIR MENSAGEM
        self.chat.configure(state='normal')
        self.chat.insert(END, txt)
        self.chat.insert(END, "\n")
        self.chat.see('end')
        self.chat.configure(state='disabled')

    def janela(self):


        janela=Tk()
        janela.geometry("700x400")
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        label=Label(janela,text="Canais")
        label2 = Label(janela, text="Leituras")
        c0 = Checkbutton(janela, text="Temperatura",onvalue="Temperatura", variable=var1,command=lambda: self.subscribe(var1.get(),var2.get(),var3.get()))
        c1 = Checkbutton(janela, text="Umidade", variable=var2, onvalue="Umidade", command=lambda: self.subscribe(var1.get(),var2.get(),var3.get()))
        c2 = Checkbutton(janela, text="Velocidade", onvalue="Velocidade", variable=var3, command=lambda: self.subscribe(var1.get(),var2.get(),var3.get()))

        self.chat = ScrolledText(janela, width=70, height=20, state='disabled')
        self.chat.place(x=100,y=40)
        label.place(x=35,y=10)
        label2.place(x=300,y=10)
        c0.place(x=5,y=40)
        c1.place(x=5,y=70)
        c2.place(x=5,y=100)
        c0.deselect()
        c1.deselect()
        c2.deselect()


        janela.mainloop()







def main():
    def onMessage(client,userdata,message):
        print(f"messagem {str(message.payload.decode('utf-8'))}")


    cliente = Cliente()



    #client.loop_stop()
main()

