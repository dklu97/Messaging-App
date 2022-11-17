import socket
import sys
import time

new_socket = socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(hostname)
port =  8080

#binding the host
new_socket.bind((host_name, port))

print("binding successful")
print("This is your IP adress", s_ip)

#listening for connections
name = input("Enter name:")
new_socket.listen(1)


#accepting an incoming connection

# client will return a value pair
#conn = new socket object
#adress
conn, add = new_socket.accept()
print("received connection from",add [0])

#storing incoming connection data
client = (conn.recv(1024)).decode()
print(client + 'has connected.')
conn.send(name.enconde())


while True:
    message = input("Me: ")
    conn.send(message.encode())
    message = conv.recv(1024)
    message = message.decode()
    print(client, ':', message)

    