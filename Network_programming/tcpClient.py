import socket

def socket_client():
    host = '127.0.0.1'
    port =4000
    s=socket.socket()
    s.connect((host, port))
    message = raw_input('-->')
    while message!='q':
        s.send(message)
        data = s.recv(1024)
        print("Recived from server:{}".format(str(data)))
        message = raw_input('->')
    s.close()
socket_client()