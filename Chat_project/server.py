import socket
import time

host_name = "localhost"
port = 7777

internet_socket = socket.socket()
internet_socket.bind((host_name, port))
internet_socket.listen(1)

connection, address = internet_socket.accept()

print(str(address)+" Connection established.")

while True:
    while True:
        try:
            incoming_data = str(connection.recv(1024).decode())
            print("CLIENT : "+incoming_data)
            break
        except ConnectionResetError:
            time.sleep(2)
            connection, address = internet_socket.accept()
            print(str(address)+"Connection established.")
    if incoming_data == "exit":
        break
    else:
        message = input("----::")
        print("Clint Waiting...")
        connection.send(message.encode())

connection.close()
