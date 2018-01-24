import socket
import os
from time import sleep

proxy_socket_name = "/var/run/docker.sock"
org_socket_name = "/var/run/docker.sock.org"

listen_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
os.unlink(proxy_socket_name)
listen_socket.bind(proxy_socket_name)
listen_socket.listen(1)

while True:
    print("Waiting for a connection")
    connection, client_address =  listen_socket.accept()
    try:
        data = connection.recv(4096)
        print("Client sent us:\n{}".format(data.decode()))
        client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        client_socket.connect(org_socket_name)
        print("Sending data to docker deamon")
        client_socket.sendall(data)
        sleep(0.2)
        data2 = client_socket.recv(4096)
        print("Docker deamon sent us\n{}".format(data2.decode()))
        connection.sendall(data2)
        print("Sending data back to client")


    except Exception as e:
        print(e)
    finally: 
        connection.close()


