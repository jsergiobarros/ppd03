# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import paho.mqtt.client as paho
from random import randrange,uniform
import time

broker = 'broker.emqx.io'
client = paho.Client("Temperatura")
client1 = paho.Client("Temperatura")

#client = paho.Client("Velocidade")
client.connect(broker)
client1.connect(broker)
client.publish("temperatura",1)
client1.publish("temperatura",1)
port = 1883



