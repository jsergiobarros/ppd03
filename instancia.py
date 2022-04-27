
import gc
import random
import threading
import time
from tkinter import *
from tkinter import messagebox

from paho.mqtt import client as mqtt
class instancia:
    # client_id = f'python-mqtt-{random.randint(0, 1000)}'
    broker = 'mqtt.eclipseprojects.io'
    port = 1883
    bool =True
    leitura =0
    def setLimite(self ,linf ,lsup):
        self.linf = float(linf)
        self.lsup = float(lsup)


    def __init__(self ,topico ,nome ,linf ,lsup):
        self.topic =topico
        self.nome = nome
        self.client = mqtt.Client(nome)
        self.client.connect(self.broker)
        self.setLimite(linf, lsup)
        self.atual = (self.linf +self.lsup)/2
        jan = threading.Thread(target=self.janela)
        jan.start()
        self.client.loop_start()
        while self.bool:
            print(f"o Sensor de {self.topic}: {self.nome} superou os limites com o valor {self.atual} ")
            if self.atual > self.lsup or self.atual < self.linf:
                self.client.publish(self.topic,
                                    str(f"O Sensor de {self.topic}: {self.nome} superou os limites com o valor {self.atual} "))
            if self.leitura != 0:
                self.leitura["text"] = f"leitura atual {self.atual}"
            self.atual += random.randint(-3, 3)
            time.sleep(5)
        self.client.loop_stop()

    def janela(self):
        def redefinir():
            def testeint():
                try:
                    aux0 = entry0.get()
                    aux0 = aux0.replace(",", ".")
                    aux1 = entry1.get()
                    aux1 = aux1.replace(",", ".")
                    float(aux0)
                    float(aux1)
                    if aux0 > aux1:
                        float("as")
                    self.setLimite(aux0, aux1)
                    lable[
                        "text"] = f"sensor {self.nome} : {self.topic}\n Limite Inferior {self.linf}\nLimite Superior {self.lsup}"
                    redef.destroy()
                except:
                    messagebox.showerror(title="valor incorreto", message="valor nao aceito, \ntente novamente")
            redef = Tk()
            redef.geometry(("220x290"))
            redef.resizable(False, False)
            canvas0 = Canvas(redef, width=100, height=100)
            lable0 = Label(canvas0, text=f"sensor {self.nome} : {self.topic}\n Limite Inferior: {self.linf}")
            entry0 = Entry(canvas0, width=20)
            lable1 = Label(canvas0, text=f"Limite Superior: {self.lsup}")
            entry1 = Entry(canvas0, width=20)
            button = Button(canvas0, text="Redefinir", borderwidth=1, command=testeint)
            lable0.grid(row=0)
            entry0.grid(row=1)
            lable1.grid(row=2)
            entry1.grid(row=3)
            button.grid(row=4)
            canvas0.pack()
            redef.mainloop()

        def enviaValor():
            try:
                aux = float(entry1.get())
                self.atual = aux
                self.leitura["text"] = f"leitura atual {self.atual}"
                entry1.delete(0, END)
            except:
                messagebox.showerror(title="Valor invalido", message="Valor inválido, tente novamente")

        win = Tk()
        win.geometry(("250x250"))
        win.resizable(False, False)
        canvas = Canvas(win, width=250, height=250)
        button = Button(canvas, text="Redefinir Limites", borderwidth=1, command=redefinir)
        enviar = Button(canvas, text="Enviar Leitura", borderwidth=1, command=enviaValor)
        lable = Label(canvas, text=f"sensor {self.nome} : {self.topic}\n Limite Inferior {self.linf}\nLimite Superior {self.lsup}")
        self.leitura = Label(canvas, font=("Arial", 14), text=f"leitura atual {self.atual}")
        entry1 = Entry(canvas, width=10)
        lable.grid(row=0)
        self.leitura.grid(pady=10, row=2)
        entry1.grid(row=3, column=0)
        enviar.grid(row=3, column=1)
        button.grid(row=1)
        canvas.pack()

        def desliga():
            win.destroy()
            self.leitura = False
            self.bool = False

        win.protocol("WM_DELETE_WINDOW", desliga)
        win.mainloop()
