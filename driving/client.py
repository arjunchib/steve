import socket
import sys

s = socket.socket()
host = "143.215.104.197"
port = 8006

try:
    s.connect((host, port))
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print s.send("-100 100")
# while True:
#     message = s.recv(128)
#     if message:
#         print message

# s.send("hello")
# s.close
