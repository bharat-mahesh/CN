
import socket
import random


def sendAcknowledgment(k):
    print("\nSending acknowledgement for ", k)
    while True:
        
        ack = str(random.randint(1,2))
        s.send(ack.encode())
        if ack == '2':
            print("Discarded frames\n\n")
            return k
        elif ack == '1':
            k = k+1
            return k



host = 'localhost'
port = 5050


s = socket.socket()

s.connect(('10.0.120.32', port))


window_size = s.recv(1024)

N = s.recv(1024)

k = 0

while True:
    frame = s.recv(1024)
    if frame.decode() == "Request":
        k = sendAcknowledgment(k)
        continue
    if frame.decode() == "All Sent":
        s.close()
        break
    if frame.decode().find("Request") == -1:
        print("Receiving frame ", frame.decode())
        print("\n")
