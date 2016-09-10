import socket

s = socket.socket()
host = "143.215.108.131"
port = 42069

s.connect((host, port))
s.send("hello")
s.close
