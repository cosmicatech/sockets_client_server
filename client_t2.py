# Echo client program
import socket
import multiprocessing

HOST = '127.0.0.1'# The remote host
PORT = int(input("Connection Port: "))# The same port as used by the server

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data = s.recv(1024)
            print('CONNECTION CONFIRMATION: ', data.decode('utf-8'))
            while True:
                try:
                    sendput = input("Send? ")
                    if sendput == "":
                        tosend = "newline".encode('utf-8')
                    else:
                        tosend = sendput.encode('utf-8')
                    s.sendall(tosend)
                    data = s.recv(1024)
                    print(data.decode('utf-8'))
                except ConnectionResetError:
                    print("--- Server forcibly closed connection ---")
                    break
    except KeyboardInterrupt as e:
        exit(e)
    except Exception as e:
        print("Unknown error: " + str(e))
        exit(e)
