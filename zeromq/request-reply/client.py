import zmq
import sys

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

# Send a "message" using the socket
if len(sys.argv) > 1:
	message = sys.argv[1:]
	sock.send_string(" ".join(message))
print(sock.recv())