#Author:Bing Liu
import socket
import os

class Server:

    server = None

    def __init__(self, localhost='localhost', pots=9999):
        self.server = socket.socket()
        self.server.bind((localhost, pots))
        self.server.listen()


    while True:
        conn, addr = server.accept()
        print("new conn:", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                print("客户端已断开")
                break
            print("执行指令：", data)
            cmd_res = os.popen(data.decode()).read() #接收字符串，执行结果也是字符串
            print("before send", len(cmd_res))
            if len(cmd_res) == 0:
                cmd_res = 'cmd has no output...'
            conn.send( str(len(cmd_res.encode("utf-8"))).encode("utf-8") ) #先发大小给客户端
            client_ack = conn.recv(1024)
            print("ack from client:", client_ack)
            conn.send(cmd_res.encode("utf-8")) #连续发送conn.send()会出现数据黏包

            print("send done")
            server.close()
