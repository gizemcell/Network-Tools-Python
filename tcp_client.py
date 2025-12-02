import socket

target_host="#ip"
target_port="#port"


#socket object for client,AF_INET=> ipv4 , STREAM=>TCP protocol 
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))

client.send(b"GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")
print("[*] CLient sent get request")

response=client.recv(4096)
print(response.decode())
client.close()

