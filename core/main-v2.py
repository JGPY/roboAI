#Author:Bing Liu

from core.SSH.SshClient import*
from core.Requsets.ReqAPI import*
import core.utils.dataTrans as utils

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
    print("HttpClient-SSH Connected")
    command = "cd ./liu/Audio;python3 AudioPlay.py audio"
    print("HttpClient-SSH command:", command)
    strData = client.command(command)
    print("HttpClient-SSH-strData:", strData)

    while True:
            try:
                lock.acquire()
                if Socket_dictMsg["flag"] == "trigger":
                    Socket_dictMsg["flag"] = "null"
                    if Socket_dictMsg["Msg"] == "A":

                        command = "cd ./liu/Audio;python3 AudioPlay.py audioA"
                        print("HttpClient-SSH command:", command)
                        client.command(command)

                        jsonData = httpReq.setCommData("addGoalQueue", "GoalQueueA", "A")
                        print("addGoalQueue-currentGoalA-A:", jsonData)
                        jsonData = httpReq.setCommData("addGoalQueue", "currentGoalA", "A")
                        print("addGoalQueue-currentGoalB-B:", jsonData)
                        jsonData = httpReq.setCommData("updateGoalState", "currentState", "running")
                        print("updateGoalState-currentState-running:", jsonData)
                    elif Socket_dictMsg["Msg"] == "B":

                        command = "cd ./liu/Audio;python3 AudioPlay.py audioB"
                        print("HttpClient-SSH command:", command)
                        client.command(command)

                        httpReq.setCommData("addGoalQueue", "GoalQueueA", "B")
                        httpReq.setCommData("addGoalQueue", "currentGoalA", "B")
                        httpReq.setCommData("updateGoalState", "currentState", "running")
                    elif Socket_dictMsg["Msg"] == "C":

                        command = "cd ./liu/Audio;python3 AudioPlay.py audioC"
                        print("HttpClient-SSH command:", command)
                        client.command(command)

                        httpReq.setCommData("addGoalQueue", "GoalQueueA", "C")
                        httpReq.setCommData("addGoalQueue", "currentGoalA", "C")
                        httpReq.setCommData("updateGoalState", "currentState", "running")
                    elif Socket_dictMsg["Msg"] == "D":

                        command = "cd ./liu/Audio;python3 AudioPlay.py audioD"
                        print("HttpClient-SSH command:", command)
                        client.command(command)

                        httpReq.setCommData("addGoalQueue", "GoalQueueA", "D")
                        httpReq.setCommData("addGoalQueue", "currentGoalA", "D")
                        httpReq.setCommData("updateGoalState", "currentState", "running")
                    else:
                        print("Socket_dictMsg[\"Msg\"] no run,Msg:", Socket_dictMsg["Msg"])

                    currentState = "running"
                    while currentState == "running":
                        jsonData = httpReq.getGoalState()
                        strDate = jsonData['result']
                        # dictData = utils.getGoalStateDataStransDict(strDate)
                        listData = strDate.split("\",\"")
                        currentState = listData[21]
                        time.sleep(0.2)
                        print("CarCurrentState:", currentState)

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
            print("SSH Connected")
            command = "cd ./liu/Audio;python3 AudioPlay.py audio"
            print("SSH command:", command)
            strData = client.command(command)
            print("SSH-strData:", strData)
            while True:
                if Audio_dictMsg.get("flag") == "trigger":
                    try:
                        lock.acquire()
                        Audio_dictMsg["flag"] == "null"
                        voice = Audio_dictMsg["Msg"]
                        command = "cd ./liu/Audio;python3 AudioPlay.py " + voice
                        print("SSH command:", command)
                        strData = client.command(command)
                        print("SSH-strData:", strData)
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

    '''socket服务端口'''
    socket_server_port = 9994
    # hostname = '0.0.0.0'
    # username = 'liu'
    # password = '123456'

    socket_threading = threading.Thread(target=socket_server, args=(socket_server_port, ),  name='socket')
    HttpClient_threading = threading.Thread(target=HttpClient, args=(hostname, username, password), name='HttpClient')
    SSH_threading = threading.Thread(target=SSH, args=(hostname, username, password),  name='SSH')

    socket_threading.start()
    HttpClient_threading.start()
    # SSH_threading.start()
