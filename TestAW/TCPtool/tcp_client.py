#coding=utf-8

import socket

class tcpClient():

    def __init__(self):

        self.s =None

    def connect(self,*args):
        #建立socket
        self.s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #连接
        self.s.connect(args)

    def disconect(self):
        self.s.close()

    def sendMsg(self,msg):
        self.s.send(msg)

    def recvMsg(self):

        Buffer =[]
        while True:
            data =self.s.recv(1024)
            if data:
                Buffer.append(data)
            else:
                break
        data =b''.join(Buffer)
        return data

if __name__ == '__main__':

    s=tcpClient()
    s.connect('127.0.0.1',8080)
    print s.recvMsg()

    s.sendMsg(b'Hanmeimei')
    recData =s.recvMsg()
    print recData
    s.disconect()