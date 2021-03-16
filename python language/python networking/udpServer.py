import socket


def main():
    host = '127.0.0.1'
    port = 4001
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print("UDP server is started")
    while True:
        data, addr = s.recvfrom(1024)
        print("Message from :{}".format(str(addr)))
        print("Message is : {}".format(str(data)))
        data = str(data).upper()
        print("Sending Same data:")
        s.sendto(data, addr)
    s.close()


main()
