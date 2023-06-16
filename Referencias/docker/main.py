import time
import socket
from sklearn.datasets import load_iris

data = load_iris()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0",9999))

server.listen()

while True:
    client_socket, address = server.accept()
    print("Connection from {}".format(address))
    client_socket.send("You are connected!\n".encode())
    client_socket.send(f"{data['data'][:,0]}\n".encode())
    time.sleep(2)
    client_socket.send("You are being disconnected!\n".encode())
    client_socket.close()