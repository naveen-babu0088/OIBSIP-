import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

window = tk.Tk()
window.title("Advanced Chat")

chat = ScrolledText(window)
chat.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(window)
entry.pack(fill=tk.X)

def send():
    message = entry.get()

    if message:
        client.send(message.encode())
        entry.delete(0, tk.END)

def receive():
    while True:
        try:
            msg = client.recv(4096).decode()
            chat.insert(tk.END, msg + "\n")
        except:
            break

tk.Button(
    window,
    text="Send",
    command=send
).pack()

threading.Thread(
    target=receive,
    daemon=True
).start()

window.mainloop()