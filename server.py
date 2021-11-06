import socket
import threading
import time
from logfunc import log, INFO, WARNING, ERROR, DEBUG
import os
import dotenv

dotenv.load_dotenv()
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
IP = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (IP, PORT)
DISCON_MSG = ['!dis', '!disconnect']
MAX_CON = int(os.getenv('MAX_CON'))
server.bind(ADDR)


active_con = 0

def __set_active_con():
    while True:
        log('Active connections: %d' % (active_con), DEBUG)
        time.sleep(60)

def set_active_con():
    """A thread to set the active connections"""
    t2 = threading.Thread(target=__set_active_con)
    t2.daemon = True
    t2.start()

def handle_client(conn, addr):
    global active_con
    active_con += 1
    log(f'{addr[0]} is connected', INFO)
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg not in DISCON_MSG:
                log(f'[-{addr[0]}-]: {msg}', DEBUG) 
            elif msg.startswith(DISCON_MSG[0]):
                connected = False
                conn.close()
                log(f'{addr[0]} is disconnected', INFO)
                active_con -= 1

def start():
    log('Server is starting at %s:%d' % (IP, PORT), INFO)
    server.listen(int(os.getenv('MAX_CON')))
    log(f'Max-Clients: {int(os.getenv("MAX_CON"))}', INFO)
    while True:
        con, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(con, addr))
        t.daemon = True
        t.start()

set_active_con()
start()