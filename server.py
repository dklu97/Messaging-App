import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        message_length = conn.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = conn.recv(message_length).decode(FORMAT)
            if message == DISCONNECT_MESSAGE:
                connected = False
                print(f"[{addr}] {message}")
    conn.close()


def start():
    server.listen()
    print("Server is listening")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[NEW CONNECTION] {addr} connected.")
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


print("[STARTING] starting the server")
start()
