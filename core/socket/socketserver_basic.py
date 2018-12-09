#Author:Liu Bing
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                if len(self.data) == 0:
                    continue
                # print("{} wrote:".format(self.client_address[0]).encode())
                print("地址：", self.client_address[0].encode())
                print("信息：", self.data)
                self.request.send(b"OK!")
            except ConnectionResetError as e:
                print("err", e)
                break
if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9996 #服务器多网卡 "0.0.0.0"
    # Create the server, binding to localhost on port 9999
    # server = socketserver.TCPServer((HOST, PORT), MyTCPHandler) #单用户
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) #并发(线程)
    # server = socketserver.ForkingUDPServer((HOST, PORT), MyTCPHandler)  # 并发(进程)(不适用Windows系统)
    server.serve_forever()


