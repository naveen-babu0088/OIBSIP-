import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass

def handle(client):
    while True:
        try:
            msg = client.recv(4096)
            broadcast(msg)
        except:
            if client in clients:
                clients.remove(client)
            client.close()
            break

print("Server running...")

while True:
    client, addr = server.accept()
    print("Connected:", addr)

    clients.append(client)

    threading.Thread(
        target=handle,
        args=(client,),
        daemon=True
    ).start()