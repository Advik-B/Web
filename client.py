import socket
import os
import dotenv
from logfunc import log, INFO, ERROR, DEBUG

dotenv.load_dotenv()

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!dis'

IP = socket.gethostbyname(socket.gethostname()) #NOTE: Change this to the IP of the server you want to connect to

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((IP, PORT))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

for i in range(10):
    send(f'Hello {i}')
    log(f'Sent-{i}', INFO)

send(DISCONNECT_MESSAGE)
