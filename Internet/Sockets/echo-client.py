"""
Client side: use sockets to send data to the server, and print server's
reply to each message line; 'localhost' means that the server is running
on the same machine as the client, which lets us test client and server
on one machine; to test over the Internet, run a server on a remote machine,
and set serverHost or argv[1] to machine's domain name or IP addr; Python
sockets are a portable BSD socket interface, with object methods for the
standard socket calls available in the system's C library;
"""

import sys
from socket import *
serverHost = 'localhost'
serverPort = 50007

message = [b'Hello network world']  # default text to send to server
print(message)

if len(sys.argv) > 1:
    serverHost = sys.argv[1]        # server from cmd line arg 1
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

sockobj = socket(AF_INET, SOCK_STREAM) # make a TCP/IP socket object
sockobj.connect((serverHost,serverPort))

for line in message:
    sockobj.send(line)              # send line  to server over socket
    data = sockobj.recv(1024)       # receive line from server: up to 1k
    print('Client received:', data)

sockobj.close()