#Publisher.py
import zmq
from random import randrange


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5588")
socket.bind("ipc://weather.ipc")

while True:
    topic = "test"
    zipcode = randrange(1, 100000)
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)
    socket.send_string("%i %i %i" % (zipcode, temperature, relhumidity))
    # socket.send_string("%s %i %i %i" % (topic, zipcode, temperature, relhumidity))
