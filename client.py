import socket
import time
import colors

COLORS = colors.bcolors()
HOST = '127.0.0.1'
PORT = 5000


def close_socket_connection(client_socket: socket):
    client_socket.close()  # close the connection

    print(COLORS.HEADER + "Connection is closing now...." + COLORS.ENDC)
    time.sleep(0.5)
    print(COLORS.OKCYAN + "Connection is closing now.........." + COLORS.ENDC)
    time.sleep(0.5)
    print(COLORS.WARNING + "Connection is closing now...................." + COLORS.ENDC)
    time.sleep(0.5)
    print(COLORS.BOLD + "Connection closed" + COLORS.ENDC)


def main():
    client_socket = socket.socket()  # instantiate
    client_socket.connect((HOST, PORT))  # connect to the server

    message = input("insert command -> ")  # take input

    while message != 'quit':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input("insert command -> ")  # take input

    close_socket_connection(client_socket)


if __name__ == '__main__':
    main()
