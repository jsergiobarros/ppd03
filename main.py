# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import paho.mqtt.client as paho
from random import randrange,uniform
import time

def main():
    def onMessage(client,userdata,message):
        print(f"messagem {str(message.payload.decode('utf-8'))}")


    broker = 'mqtt.eclipseprojects.io'

    """var1 = IntVar()
    Checkbutton(canvas, text="male", variable=var1).grid(row=5, sticky=W)
    var2 = IntVar()
    Checkbutton(canvas, text="female", variable=var2, command=lambda: print("click")).grid(row=6, sticky=W)"""


    client = paho.Client("pessoa")

    client.connect(broker)
    print("teste")
    #client.loop_start()
    client.subscribe("Velocidade")
    client.subscribe("Temperatura")
    client.subscribe("Umidade")
    #client.unsubscribe("Velocidade")
    client.on_message=onMessage
    client.loop_forever()
    print("teste")

    #client.loop_stop()
main()

