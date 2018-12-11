#Author:Jason Lou
from core.ssh.sshClient import*
from core.http.ReqAPI import*

import threading
import socket
import time
import logging

Socket_dictMsg = {"flag": 'null', 'Msg': 'null', }
SSH_dictMsg = {"flag": 'null', 'Msg': 'null', }
HttpReq_dictMsg = {"flag": 'null', 'Msg': 'null', }
Audio_dictMsg = {"flag": 'null', 'Msg': 'null', }
Handle_dictMsg = {"state": 'stopped'}

lock = threading.Lock()


def socket_server(port):    # 客户端数据不要超过1024个字节
    server = socket.socket()
    try:
        server.bind(('0.0.0.0', port))
        server.listen()
        while True:
            conn, addr = server.accept()
            print("new conn IP:", addr)
            while True:
                data = conn.recv(1024)
                print(data)
                if not data:
                    print("客户端已断开", data)
                    break
                try:
                    lock.acquire()
                    if Handle_dictMsg['state'] == "stopped":
                        Handle_dictMsg['state'] == "running"
                        Socket_dictMsg["flag"] = "trigger"
                        Socket_dictMsg['Msg'] = str(data, "utf8")
                        conn.send('ok'.encode('utf-8'))
                    else:
                        conn.send('err'.encode('utf-8'))
                finally:
                    print('socket:', Socket_dictMsg['Msg'])
                    lock.release()
                    # break
                print("客户端数据：", data)
    finally:
        server.close()


def HttpClient(host, name, pwd):
    url = "http://192.168.31.200:8080"
    httpReq = HttpReq(url)

    client = SshClient()
    client.connect(host, name, pwd)
    print("HttpClient-ssh Connected")
    command = "cd ./liu/audio;python3 AudioPlay.py Init"
    print("HttpClient-ssh command:", command)
    strData = client.command(command)
    print("HttpClient-ssh-strData:", strData)

    while True:
            try:
                lock.acquire()
                if Socket_dictMsg["flag"] == "trigger":
                    Socket_dictMsg["flag"] = "null"
                    # 初始化后ROS被默认导航队列循环，需要清除
                    httpReq.getDelGoalState()

                    ######## 单点控制 ########
                    if Socket_dictMsg["Msg"] == "A":
                        command = "cd ./liu/audio;python3 AudioPlay.py audioA"
                        print("HttpClient-ssh command:", command)
                        client.command(command)
                        jsonData = httpReq.setCommData("addGoalQueue", "GoalQueueA", "A")
                        print("addGoalQueue-GoalQueueA-A:", jsonData)
                        jsonData = httpReq.setCommData("addGoalQueue", "currentGoalA", "A")
                        print("addGoalQueue-currentGoalA-B:", jsonData)
                        jsonData = httpReq.setCommData("updateGoalState", "currentState", "running")
                        print("updateGoalState-currentState-running:", jsonData)
                    elif Socket_dictMsg["Msg"] == "B":
                        command = "cd ./liu/audio;python3 AudioPlay.py audioB"
                        print("HttpClient-ssh command:", command)
                        client.command(command)
                        httpReq.setCommData("addGoalQueue", "GoalQueueA", "B")
                        httpReq.setCommData("addGoalQueue", "currentGoalA", "B")
                        httpReq.setCommData("updateGoalState", "currentState", "running")
                    elif Socket_dictMsg["Msg"] == "C":
                        command = "cd ./liu/audio;python3 AudioPlay.py audioC"
                        print("HttpClient-ssh command:", command)
                        client.command(command)
                        httpReq.setCommData("addGoalQueue", "GoalQueueA", "C")
                        httpReq.setCommData("addGoalQueue", "currentGoalA", "C")
                        httpReq.setCommData("updateGoalState", "currentState", "running")
                    elif Socket_dictMsg["Msg"] == "D":
                        command = "cd ./liu/audio;python3 AudioPlay.py audioD"
                        print("HttpClient-ssh command:", command)
                        client.command(command)
                        httpReq.setCommData("addGoalQueue", "GoalQueueA", "D")
                        httpReq.setCommData("addGoalQueue", "currentGoalA", "D")
                        httpReq.setCommData("updateGoalState", "currentState", "running")
                    # else:
                    #     print("Socket_dictMsg[\"Msg\"] no run,Msg:", Socket_dictMsg["Msg"])
                    # currentState = "running"
                    # while currentState == "running":
                    #     jsonData = httpReq.getGoalState()
                    #     strDate = jsonData['result']
                    #     # dictData = utils.getGoalStateDataStransDict(strDate)
                    #     listData = strDate.split("\",\"")
                    #     currentState = listData[21]
                    #     time.sleep(0.2)
                    #     print("CarCurrentState:", currentState)
                    # if currentState == "stopped":
                    #     currentState == "null"
                    #     command = "cd ./liu/audio;python3 AudioPlay.py audio"+Socket_dictMsg["Msg"]+"ed"
                    #     print("HttpClient-ssh command:", command)
                    #     client.command(command)


                    ######## loop ########
                    if Socket_dictMsg["Msg"] == "loop":
                        # jsonData = httpReq.setCommData("updateGoalState", "currentState", "stopped")
                        # httpReq.getDelGoalState()
                        # httpReq.setCommData("updateGoalState","mode", "order")
                        # httpReq.setCommData("updateGoalState", "loopWay", "auto")

                        httpReq.setCommData("updateGoalState", "intervalTime", "0")

                        jsonData = httpReq.setCommData("addGoalQueue", "GoalQueueA", "A")
                        # jsonData = httpReq.setCommData("addGoalQueue", "currentGoalA", "")
                        # jsonData = httpReq.setCommData("addGoalQueue", "GoalQueueB", "")
                        # jsonData = httpReq.setCommData("addGoalQueue", "currentGoalB", "")
                        jsonData = httpReq.setCommData("updateGoalState", "currentState", "running")
                        currentState = "running"
                        print("CarCurrentState:", currentState)
                        while currentState == "running":
                            currentState = httpReq.getGoalState()['result'].split("\",\"")[21]
                        if currentState == "stopped":
                            print("CarCurrentState:", currentState)
                            currentState == "null"
                            ####### 欢迎词 #######
                            command = "cd ./liu/audio;python3 AudioPlay.py LO11"
                            print("HttpClient-ssh command:", command)
                            client.command(command)

                        jsonData = httpReq.setCommData("addGoalQueue", "GoalQueueA", "B")
                        # jsonData = httpReq.setCommData("addGoalQueue", "currentGoalA", "B")
                        jsonData = httpReq.setCommData("updateGoalState", "currentState", "running")
                        currentState = "running"
                        print("CarCurrentState:", currentState)
                        while currentState == "running":
                            currentState = httpReq.getGoalState()['result'].split("\",\"")[21]
                        if currentState == "stopped":
                            print("CarCurrentState:", currentState)
                            currentState == "null"
                            ####### 介绍方向三 #######
                            command = "cd ./liu/audio;python3 AudioPlay.py LO12"
                            print("HttpClient-ssh command:", command)
                            client.command(command)

                        jsonData = httpReq.setCommData("addGoalQueue", "GoalQueueA", "C")
                        # jsonData = httpReq.setCommData("addGoalQueue", "currentGoalA", "C")
                        jsonData = httpReq.setCommData("updateGoalState", "currentState", "running")
                        currentState = "running"
                        print("CarCurrentState:", currentState)
                        while currentState == "running":
                            currentState = httpReq.getGoalState()['result'].split("\",\"")[21]
                        if currentState == "stopped":
                            print("CarCurrentState:", currentState)
                            currentState == "null"
                            ####### 介绍方向二 #######
                            command = "cd ./liu/audio;python3 AudioPlay.py LO13"
                            print("HttpClient-ssh command:", command)
                            client.command(command)

                        jsonData = httpReq.setCommData("addGoalQueue", "GoalQueueA", "D")
                        # jsonData = httpReq.setCommData("addGoalQueue", "currentGoalA", "D")
                        jsonData = httpReq.setCommData("updateGoalState", "currentState", "running")
                        currentState = "running"
                        print("CarCurrentState:", currentState)
                        while currentState == "running":
                            currentState = httpReq.getGoalState()['result'].split("\",\"")[21]
                        if currentState == "stopped":
                            currentState == "null"
                            ####### 介绍方向一 #######
                            command = "cd ./liu/audio;python3 AudioPlay.py LO14"
                            print("HttpClient-ssh command:", command)
                            client.command(command)

                        ####### 返回初始位置 #######
                        jsonData = httpReq.setCommData("addGoalQueue", "GoalQueueA", "A")
                        # jsonData = httpReq.setCommData("addGoalQueue", "currentGoalA", "A")
                        jsonData = httpReq.setCommData("updateGoalState", "currentState", "running")
                        currentState = "running"
                        print("CarCurrentState:", currentState)
                        while currentState == "running":
                            currentState = httpReq.getGoalState()['result'].split("\",\"")[21]
                        if currentState == "stopped":
                            print("CarCurrentState:", currentState)
                            currentState == "null"
                            ####### 结束词 #######
                            command = "cd ./liu/audio;python3 AudioPlay.py 912E"
                            print("HttpClient-ssh command:", command)
                            client.command(command)

            finally:
                Socket_dictMsg["Msg"] = "null"
                Audio_dictMsg["flag"] == "trigger"
                Audio_dictMsg["Msg"] == Socket_dictMsg["Msg"]
                Handle_dictMsg['state'] = "stopped"
                lock.release()


def SSH(host, name, pwd):
    client = SshClient()
    while True:
        try:
            client.connect(host, name, pwd)
            print("ssh Connected")
            command = "cd ./liu/audio;python3 AudioPlay.py audio"
            print("ssh command:", command)
            strData = client.command(command)
            print("ssh-strData:", strData)
            while True:
                if Audio_dictMsg.get("flag") == "trigger":
                    try:
                        lock.acquire()
                        Audio_dictMsg["flag"] == "null"
                        voice = Audio_dictMsg["Msg"]
                        command = "cd ./liu/audio;python3 AudioPlay.py " + voice
                        print("ssh command:", command)
                        strData = client.command(command)
                        print("ssh-strData:", strData)
                        Handle_dictMsg['state'] = "stopped"
                    finally:
                        lock.release()
        finally:
            client.close()


if __name__ == '__main__':

    '''SSH登录信息'''
    hostname = '192.168.31.200'
    username = 'eaibot'
    password = 'eaibot'

    '''本地SSH登录信息'''
    # hostname = '0.0.0.0'
    # username = 'liu'
    # password = '123456'

    '''socket服务端口'''
    socket_server_port = 9994

    socket_threading = threading.Thread(target=socket_server, args=(socket_server_port, ),  name='socket')
    HttpClient_threading = threading.Thread(target=HttpClient, args=(hostname, username, password), name='HttpClient')
    SSH_threading = threading.Thread(target=SSH, args=(hostname, username, password),  name='ssh')

    socket_threading.start()
    HttpClient_threading.start()
    # SSH_threading.start()
