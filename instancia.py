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
    bool=True
    def setLimite(self,linf,lsup):
        self.linf = linf
        self.lsup = lsup



    def __init__(self,topico,nome,linf,lsup):
        self.topic=topico
        self.nome = nome
        self.client = mqtt.Client(nome)
        self.client.connect(self.broker)
        #self.client.subscribe("sensor/ppd03")
        self.setLimite(linf,lsup)
        print(self.client)
        jan =threading.Thread(target=self.janela)
        jan.start()
        i=0
        self.client.loop_start()
        while self.bool:
            self.client.subscribe("topico/pdd")

            self.client.publish("topico/pdd",str(f"a {i}"))
            print(f"ok {i}")
            time.sleep(5)
            i+=1
        self.client.loop_stop()
        print("out")
    def janela(self):
        win = Tk()
        win.geometry(("220x220"))
        win.resizable(False, False)
        canvas=Canvas(win,width=100,height=100)
        def redefinir():
            redef = Tk()
            win.geometry(("220x220"))
            win.resizable(False, False)
            canvas = Canvas(redef, width=100, height=100)

            def testeint():
                try:
                    aux0 = entry0.get()
                    aux0=aux0.replace(",",".")
                    aux1 = entry1.get()
                    aux1 = aux1.replace(",", ".")
                    float(aux0)
                    float(aux1)
                    if aux0>aux1:
                        float("as")
                    self.setLimite(aux0,aux1)
                    lable["text"]=f"sensor {self.nome} : {self.topic}\n Limite Inferior {self.linf}\nLimite Superior {self.lsup}"
                    redef.destroy()
                except:
                    messagebox.showerror(title="valor incorreto", message="valor nao aceito, \ntente novamente")



            lable0 = Label(canvas, text=f"sensor {self.nome} : {self.topic}\n Limite Inferior: {self.linf}")
            entry0 = Entry(canvas, width=20)
            lable1 = Label(canvas, text=f"Limite Superior: {self.lsup}")
            entry1 = Entry(canvas, width=20)
            button = Button(canvas, text="Redefinir", borderwidth=1, command=testeint )
            lable0.grid(row=0)
            entry0.grid(row=1)
            lable1.grid(row=2)
            entry1.grid(row=3)
            button.grid(row=4)
            canvas.pack()
            redef.mainloop()
        button = Button(canvas, text="Redefinir Limites", borderwidth=1, command = redefinir)
        enviar = Button(canvas, text="Enviar Leitura", borderwidth=1, command=print)

        lable = Label(canvas,text=f"sensor {self.nome} : {self.topic}\n Limite Inferior {self.linf}\nLimite Superior {self.lsup}")
        #entry0 = Entry(canvas,width=20)
        leitura = Label(canvas, text="leitura atual {self.atual}")
        entry1 = Entry(canvas, width=10)
        lable.grid(row=0)
        #entry0.grid(row=1)
        leitura.grid(pady=10, row=2)
        entry1.grid(row=3,column=0)
        enviar.grid(row=3,column=1)
        button.grid(row=1)
        canvas.pack()


        def desliga():
            win.destroy()
            self.bool=False
        win.protocol("WM_DELETE_WINDOW", desliga)
        win.mainloop()

"""    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
        client = mqtt.Client(self.client_id)
        client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client"""