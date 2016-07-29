# Simple web server written in Python

# Browser (client) sends an HTTP request to a physical server (server)
# The server is listening on port 80, receives and parses the request
# the response is sent back to the client with a status code

# The web address http://localhost:8888/path
# URL is a uniform resource locator
# http://			HTTP protocol
# localhost			hostname
# 8888				port
# /hello 			path

# Tells the browser the address of the webserver and the path
# that it needs to find to get your page.
# TCP connection is made first
# The client sends an HTTP request
# The server responds with a HTTP response
# The browser renders the page

# Client and server use sockets to establish the TCP for a two way flow of info
# Server creates, binds, listens and accepts in a loop

# Server sends back the HTTP version (HTTP/1.1), status code (200) and response body (Hello, World)

import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()