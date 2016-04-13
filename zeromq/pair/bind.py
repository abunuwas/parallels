import zmq
import random
import sys
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
port = "5556"
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:
	socket.send_string("Server message sent to client3")
	msg = socket.recv()
	print(msg)
	time.sleep(1)

