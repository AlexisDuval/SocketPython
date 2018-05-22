import socket 


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port


sock_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_serv.bind((HOST, PORT))
sock_serv.listen(1)

while 1:
    print("ok")


sock_serv.close()




