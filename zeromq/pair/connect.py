import zmq
import random
import sys
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket usign the "Context"
port = "5556"
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while True:
	msg = socket.recv()
	print(msg)
	socket.send_string("client message to server1")
	socket.send_string("client message sent to server2")
	time.sleep(1)
		


