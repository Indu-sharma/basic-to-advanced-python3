import socket
def main():
    host = '127.0.0.1'
    port = 4002
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    message = raw_input('-->')
    server = ('127.0.0.1',4001)
    while message != 'q':
        s.sendto(message, server)
        data, addr = s.recvfrom(1024)
        print("Recived from server:{}".format(str(data)))
        message = raw_input('->')
    s.close()


main()