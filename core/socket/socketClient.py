#Author:Jason Lou
import socket

class Client:
    client = None
    def __init__(self, localhost='localhost', pots=9998):
        self.client = socket.socket()
        self.client.connect((localhost, pots))

    def sendmsgs(self, str):
        if len(str) == 0:
            return
        self.client.send(str.encode("utf-8"))
        server_ack = self.client.recv(1024)  # 服务端确认接收
        print("服务端已接收命令：", server_ack)

    def closeclient(self):
        self.client.close()

if __name__ == '__main__':
    client = Client()
    client.sendmsgs("cmd")
    client.closeclient()
