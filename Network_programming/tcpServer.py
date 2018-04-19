import socket


def socket_server():
    host = '127.0.0.1'
    port = 4000
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    c, add = s.accept()
    print("Connection from:", str(add))
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("From connected user: " + str(data))
        data = str(data).upper()
        print("Sending " + str(data))
        c.send(data)
    c.close()


socket_server()
