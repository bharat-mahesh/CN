
import socket


def sendAcknowledgment(k):
    print("\nSending ACK for ", k)
    ack = input("Enter 1 to send ACK\nEnter 2 to not send ACK\n")
    s.send(ack.encode())
    if ack == '2':
        print("Discarded Remaining Frames!\n\n")
        return k
    elif ack == '1':
        k = k+1
        return k
    else:
        return k


host = 'localhost'
port = 5050


s = socket.socket()

s.connect(('192.168.26.112', port))


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
