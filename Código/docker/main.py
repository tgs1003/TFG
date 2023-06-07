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

    for i in range(len(data.data)):
        client_socket.sendall(str(data.data[i]).encode())
        time.sleep(0.1)
        
    client_socket.sendall("end".encode())
    client_socket.close()