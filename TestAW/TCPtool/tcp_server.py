#coding=utf-8
import socket
import threading
import time

class tcpServer():

    def __init__(self):
        self.s =None

    def startServer(self):
        self.s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bind(('127.0.0.1',8080))
        self.s.listen(5)
        print "TCP Server '127.0.0.1' started..."

    def recvClient(self):
        sock,addr =self.s.accept()
        t =threading.Thread(target=self.msgInteractive,args=(sock,addr))
        t.start()

    def msgInteractive(self,sock,addr):
        print 'Accept new connection from %s' %addr
        sock.send('Welcome to MyServer!')
        while True:
            data =sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') =='exit':
                break
            else:
                sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        sock.close()
        print 'Connection from %s closed!' %addr

if __name__ =='__main__':
    s =tcpServer()
    s.startServer()
    while True:
        s.recvClient()
