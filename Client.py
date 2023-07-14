import socket
import threading

connection = True

def recievemessage(connect):
    while True:
        data= s.recv(1024)
        print(data.decode())
        if connect[len(connect)-1] == False:
            break

def sendmessage(connect):
    while True:
        message = input()
        s.send(message.encode('utf-8'))
        if message == 'q':
            s.close()
            connect.append(False)
            break
    
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'localhost'
port = 43389

name = input("Enter the name you wish to login as: ")

s.connect((host,port))
s.send(name.encode('utf-8'))

connected = []
connected.append(True)

t1 = threading.Thread(target=sendmessage,args=(connected,))
t1.start()
print("Messaging started")
t2 = threading.Thread(target=recievemessage,args=(connected,))
t2.start()
print("Recieving started")