import socket ; 


hote = ''
port = 12800

sock_serv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock_serv.bind(hote,port)

sock_serv.listen(5)




