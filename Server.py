import socket
import threading
from datetime import datetime

def new_join(client,client_list):
    for i in client_list:
        if i!= client:
            join_message = "Server: time" + datetime.now().strftime("%H:%M:%S") + ' ' + client[0] + " has joined, Member count=" + str(len(client_list))
            i[1].send(join_message.encode('utf-8'))
    
    leave_request = False
    
    while True:
        message = client[1].recv(1024)
        if message.decode() == 'q':
            leave_request = True
        
        broadcast = ''
        if leave_request:
            client_list.remove(client)
            broadcast = "Server: time" + datetime.now().strftime("%H:%M:%S") + ' ' + client[0] + " has left, Member count=" + str(len(client_list))
        else:
            broadcast = client[0] + ": " + message.decode()
        
        for j in client_list:
            if j != client:
                j[1].send(broadcast.encode('utf-8'))
        if leave_request:
            break
    client[1].close()


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'localhost'
port = 43389  
s.bind((host,port))

print("Server Started....")

members = []

while True:
    s.listen(1)
    connection_socket,addr = s.accept()
    data = connection_socket.recv(1024)
    temp = [data.decode(),connection_socket,addr]
    members.append(temp)
    print("MEmber Added")
    t1 = threading.Thread(target=new_join,args=(temp,members))
    t1.start()
    print("Thread Started")