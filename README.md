# Playing around with unix domain sockets and python

# Example Client/Server 
```
kmille@homebox unix-socket.git master % python2 server.py
starting up on ./uds_socket
waiting for a connection
connection from 
received "This is the mess"
sending data back to the client
received "age.  It will be"
sending data back to the client
received " repeated."
sending data back to the client
received ""
no more data from 
waiting for a connection

kmille@homebox unix-socket.git master # python2 client.py
connecting to ./uds_socket
sending "This is the message.  It will be repeated."
received "This is the mess"
received "age.  It will be"
received " repeated."
closing socket
```

# Socket proxy: show traffic of docker client
```
kmille@homebox unix-socket.git master % sudo docker -H unix:///var/run/my_docker.sock  ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

```
kmille@homebox unix-socket.git master % sudo python2 proxy.py
Waiting for a connection
Client sent us:
GET /_ping HTTP/1.1
Host: docker
User-Agent: Docker-Client/18.09.5-ce (linux)


Sending data to docker deamon
Docker deamon sent us
HTTP/1.1 200 OK
Api-Version: 1.39
Docker-Experimental: false
Ostype: linux
Server: Docker/18.09.5-ce (linux)
Date: Sun, 16 Jun 2019 12:20:16 GMT
Content-Length: 2
Content-Type: text/plain; charset=utf-8

OK
Sending data back to client
Waiting for a connection
Client sent us:
GET /v1.39/containers/json HTTP/1.1
Host: docker
User-Agent: Docker-Client/18.09.5-ce (linux)


Sending data to docker deamon
Docker deamon sent us
HTTP/1.1 200 OK
Api-Version: 1.39
Content-Type: application/json
Docker-Experimental: false
Ostype: linux
Server: Docker/18.09.5-ce (linux)
Date: Sun, 16 Jun 2019 12:20:16 GMT
Content-Length: 3

[]

Sending data back to client
Waiting for a connection

```
