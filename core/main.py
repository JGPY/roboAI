#Author:Bing Liu

#
from core.AutoGUI.virtKey import*
from core.AutoGUI.virtCursor import*

from core.SSH.SshClient import*

import threading
import socket
import time

dict_socket_flag = {'socket': 'null', }
dict_virtKey_flag = {'virtKey': 'null', }
dict_SSH_flag = {'SSH': 'null', }

lock = threading.Lock()


def auto_gui():
    dict_coordinate = {'2DPoseEstimate': {'x': '618', 'y': '46'},
                       '2DNavGoal': {'x': '733', 'y': '46'},
                       'pointA': {'x': '0', 'y': '0'},
                       'pointB': {'x': '0', 'y': '0'},
                       'pointC': {'x': '0', 'y': '0'},
                       'pointD': {'x': '0', 'y': '0'}}

    cursor = virtCursor()
    print("宽：", cursor.width, "高", cursor.height)
    print("x：", cursor.currentMouseX, "y", cursor.currentMouseY)

    while True:
        if dict_virtKey_flag.get('virtKey') == '链接小车并且启动小车':
            try:
                # global dict_virtKey_flag
                lock.acquire()
                pass

            finally:
                lock.release()
                pass

        # 需要在终端查看返回数据
        elif dict_virtKey_flag.get('virtKey') == '打开本地终端，启动RVIZ':
            keyboard = virtKey()
            keyboard.openTerminal()
            keyboard.input("export ROS_MASTER_URI=http://192.168.31.160:11311")
            keyboard.enter()
            keyboard.input("roslaunch multi_goal.launch")
            keyboard.enter()
            keyboard.winMin()
            time.sleep(2000)
            #RVIZ窗口最大化
            keyboard.winMax()

        elif dict_virtKey_flag.get('virtKey') == '2DPoseEstimate':
            cursor.clickLeft(dict_coordinate.get("2DPoseEstimate").get("x"),
                             dict_coordinate.get("2DPoseEstimate").get("y"))

        elif dict_virtKey_flag.get('virtKey') == '2DNavGOAL':
            cursor.clickLeft(dict_coordinate.get("2DNavGoal").get("x"),
                             dict_coordinate.get("2DNavGoal").get("y"))

        elif dict_virtKey_flag.get('virtKey') == 'pointA':
            cursor.clickLeft(dict_coordinate.get("2DNavGoal").get("x"),
                             dict_coordinate.get("2DNavGoal").get("y"))
            cursor.clickLeft(dict_coordinate.get("pointA").get("x"),
                             dict_coordinate.get("pointA").get("y"))

        elif dict_virtKey_flag.get('virtKey') == 'pointB':
            cursor.clickLeft(dict_coordinate.get("2DNavGoal").get("x"),
                             dict_coordinate.get("2DNavGoal").get("y"))
            cursor.clickLeft(dict_coordinate.get("pointB").get("x"),
                             dict_coordinate.get("pointB").get("y"))

        elif dict_virtKey_flag.get('virtKey') == 'pointC':
            cursor.clickLeft(dict_coordinate.get("2DNavGoal").get("x"),
                             dict_coordinate.get("2DNavGoal").get("y"))
            cursor.clickLeft(dict_coordinate.get("pointC").get("x"),
                             dict_coordinate.get("pointC").get("y"))

        elif dict_virtKey_flag.get('virtKey') == 'pointD':
            cursor.clickLeft(dict_coordinate.get("2DNavGoal").get("x"),
                             dict_coordinate.get("2DNavGoal").get("y"))
            cursor.clickLeft(dict_coordinate.get("pointD").get("x"),
                             dict_coordinate.get("pointD").get("y"))

        elif dict_virtKey_flag.get('virtKey') == 'over':
            break


def socket_server():    # 客户端数据不要超过1024个字节
    server = socket.socket()
    server.bind(('0.0.0.0', 9998))
    try:
        server.listen()
        while True:
            conn, addr = server.accept()
            print("new conn:", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    print("客户端已断开")
                    break
                state = "ok"
                try:
                    lock.acquire()
                    global dict_socket_flag
                    dict_socket_flag['virtKey'] = data
                    print()
                finally:
                    lock.release

                conn.send(state.encode("utf-8"))
                print("客户端数据：", data)
    finally:
        server.close()

def SSH(hostname, username, password):

    while True:
        if dict_SSH_flag.get('SSH') == '连接小车，启动多点定位导航':
            try:
                Client = SshClient()
                Client.connect(hostname, username, password)
                Client.command('ls; ls -l')
                # Client.SSHClientComm('ls -l;cd Audio;ls;python3 AudioPlay.py')
            finally:
                Client.close()


if __name__ == '__main__':

    '''SSH登录信息'''
    hostname = '192.168.31.155'
    username = 'eaibot'
    password = 'eaibot'

    AutoGUI_threading = threading.Thread(target=auto_gui, name='auto_gui')
    socket_threading = threading.Thread(target=socket_server,  name='socket')
    SSH_threading = threading.Thread(target=SSH, args=(hostname, username, password),  name='SSH')

    socket_threading.start()
    # SSH_threading.start()
