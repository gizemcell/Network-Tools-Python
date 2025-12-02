import socket

IP="127.0.0.1"
PORT=9997

def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server.bind((IP,PORT))
    print("server binded")
    while True:
        message,client_addr=server.recvfrom(2048)
        print(message.decode())
        server.sendto(b"ACK",client_addr)





if __name__=='__main__':
    main()