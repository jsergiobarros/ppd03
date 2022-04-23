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




    client = paho.Client("pessoa")

    client.connect(broker)
    #client.loop_start()
    client.subscribe("topico/pdd")
    client.on_message=onMessage
    client.loop_forever()
    #client.loop_stop()
main()

