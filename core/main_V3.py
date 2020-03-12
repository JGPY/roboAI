#Author:Jason Lou
from core.ssh.sshClient import*
from core.http.ReqAPI import*

import threading
import socket
import time
import logging

SSH_dictMsg = {"flag": 'null', 'Msg': 'null', }
HttpReq_dictMsg = {"flag": 'null', 'Msg': 'null', }
Audio_dictMsg = {"flag": 'null', 'Msg': 'null', }
Handle_dictMsg = {"state": 'stopped'}

lock = threading.Lock()


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

    HttpClient_threading = threading.Thread(target=HttpClient, args=(hostname, username, password), name='HttpClient')
    SSH_threading = threading.Thread(target=SSH, args=(hostname, username, password),  name='ssh')

    HttpClient_threading.start()
    SSH_threading.start()
