import socket
import time

host_name = "localhost"
port = 7777

internet_socket = socket.socket()
internet_socket.connect((host_name, port))


print("Connection established!! {}:{}".format(host_name, port))

message = input("----::")
print("Server Waiting..")

while message != "cikis":
    internet_socket.send(message.encode())
    incoming_data = internet_socket.recv(1024).decode()

    print("SERVER : "+incoming_data)

    message = input("----::")
    print("Server Waiting...")

internet_socket.close()
