import socket
import sys
import time

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
port = 8080


#connecting to the server
print("this is your ip adress: ", ip)
server_host = input('Enter friends IP adress')


socket_server.connect(server_host, port)


#receive messages/packages from the server
socket_server.send(name.encode)
server_name = socket_server.recv(1024)
server_name = server_name.decode()


print(server_name, 'has joined...')
while True:
    message = socket_server.recv(1024).decode()
    print(server_name, ':', message)
    message = input('Me :')
    socket_server.send(message.encode())