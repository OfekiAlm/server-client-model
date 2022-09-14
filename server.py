import socket
from datetime import datetime
import random

HOST = '127.0.0.1'
PORT = 5000


def main():

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((HOST, PORT))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    connection, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    data = ""
    while data != "quit":
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = connection.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("command from connected user.\nThe command: " + str(data))

        if data == "time":
            data_to_send = str(datetime.now())
            print("time to send: " + data_to_send)

        elif data == "random":
            data_to_send = str(random.randint(1, 100))
            print("random number to send: " + data_to_send)

        else:
            data_to_send = "An invalid command"
            print("Invalid command: " + data_to_send)

        connection.send(data_to_send.encode())  # send data to the client

    connection.close()  # close the connection
    print("Connection closed")


if __name__ == '__main__':
    main()