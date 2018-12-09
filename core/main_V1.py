#Author:Jason Lou
from core.autoGUI.virtKey import*
from core.autoGUI.virtCursor import*

from core.ssh.sshClient import*

import threading
import socket
import time

global dict_socket_flag
dict_socket_flag = {"socket": b'null', "voice": "audioCtrl1"}
dict_virtKey_flag = {'virtKey': 'null', }
dict_SSH_flag = {'ssh': "null", }

lock = threading.Lock()


def auto_gui():
    dict_coordinate = {'2DPoseEstimate': {'x': 619, 'y': 41},
                       '2DPoseGaol': {'x': 524, 'y': 46},
                       'pointA': {'x': 755, 'y': 742},
                       'pointB': {'x': 524, 'y': 854},
                       'pointC': {'x': 674, 'y': 703},
                       'pointD': {'x': '0', 'y': '0'}}


    cursor = virtCursor()
    print("宽：", cursor.width, "高", cursor.height)
    print("x：", cursor.currentMouseX, "y", cursor.currentMouseY)

    while True:
        time.sleep(1)

        if dict_socket_flag.get('socket') == b'pointa':
            print('SSH_threading pointA active')
            try:
                lock.acquire()
                dict_socket_flag['socket'] = 'null'
            finally:
                lock.release()
                pass
            print('goal active')
            pyautogui.moveTo(dict_coordinate.get("2DPoseGaol").get("x"),
                             dict_coordinate.get("2DPoseGaol").get("y"))

            pyautogui.click(button='left')
            time.sleep(1)
            pyautogui.moveTo(dict_coordinate.get("pointA").get("x"),
                             dict_coordinate.get("pointA").get("y"))
            pyautogui.click(button='left')
            print('goal point')
        elif dict_socket_flag.get('socket') == b'pointb':
            print('SSH_threading pointB active')
            try:
                lock.acquire()
                dict_socket_flag['socket'] = 'null'
            finally:
                lock.release()
                pass
            print('goal active')
            pyautogui.moveTo(dict_coordinate.get("2DPoseGaol").get("x"),
                             dict_coordinate.get("2DPoseGaol").get("y"))
            pyautogui.click(button='left')
            time.sleep(1)
            pyautogui.moveTo(dict_coordinate.get("pointB").get("x"),
                             dict_coordinate.get("pointB").get("y"),)
            pyautogui.click(button='left')
            print('goal pointB')
        elif dict_socket_flag.get('socket') == b'pointC':
            print('SSH_threading pointC active')
            try:
                lock.acquire()
                dict_socket_flag['socket'] = 'null'
            finally:
                lock.release()
                pass
            print('goal active')
            pyautogui.moveTo(dict_coordinate.get("2DPoseGaol").get("x"),
                             dict_coordinate.get("2DPoseGaol").get("y"))
            pyautogui.click(button='left')
            time.sleep(1)
            pyautogui.moveTo(dict_coordinate.get("pointC").get("x"),
                             dict_coordinate.get("pointC").get("y"), )
            pyautogui.click(button='left')
            print('goal pointC')
            # cursor.clickLeft(dict_coordinate.get("2DPoseGaol").get("x"),
            #                  dict_coordinate.get("2DPoseGaol").get("y"))
            # cursor.clickLeft(dict_coordinate.get("pointA").get("x"),
            #                  dict_coordinate.get("pointA").get("y"))
            # cursor.clickLeft(int(dict_coordinate.get("2DPoseGaol").get("x"), 'utf-8'),
            #                  int(dict_coordinate.get("2DPoseGaol").get("y"), 'utf-8'))
            # cursor.clickLeft(int(dict_coordinate.get("pointA").get("x"), 'utf-8'),
            #                  int(dict_coordinate.get("pointA").get("y"), 'utf-8'))


        # if dict_virtKey_flag.get('virtKey') == '链接小车并且启动小车':
        #
        #     try:
        #         # global dict_virtKey_flag
        #         lock.acquire()
        #         pass
        #
        #     finally:
        #         lock.release
        #         pass
        #
        # # 需要在终端查看返回数据
        # elif dict_virtKey_flag.get('virtKey') == '打开本地终端，启动RVIZ':
        #     keyboard = virtKey()
        #     keyboard.openTerminal()
        #     keyboard.input("export ROS_MASTER_URI=http://192.168.31.160:11311")
        #     keyboard.enter()
        #     keyboard.input("roslaunch multi_goal.launch")
        #     keyboard.enter()
        #     keyboard.winMin()
        #     time.sleep(2000)
        #     #RVIZ窗口最大化
        #     keyboard.winMax()
        #
        # elif dict_virtKey_flag.get('virtKey') == '2DPoseEstimate':
        #     cursor.clickLeft(dict_coordinate.get("2DPoseEstimate").get("x"),
        #                      dict_coordinate.get("2DPoseEstimate").get("y"))
        #
        # elif dict_virtKey_flag.get('virtKey') == '启动设目标点':
        #     cursor.clickLeft(dict_coordinate.get("2DPoseGaol").get("x"),
        #                      dict_coordinate.get("2DPoseGaol").get("y"))
        #
        # elif dict_socket_flag.get('socket') == 'pointA':
        #     print('SSH_threading pointA active')
        #     try:
        #         lock.acquire()
        #         dict_socket_flag['socket'] = 'null'
        #     finally:
        #         lock.release()
        #     cursor.clickLeft(dict_coordinate.get("2DPoseGaol").get("x"),
        #                      dict_coordinate.get("2DPoseGaol").get("y"))
        #     cursor.clickLeft(dict_coordinate.get("pointA").get("x"),
        #                      dict_coordinate.get("pointA").get("y"))
        #
        # elif dict_virtKey_flag.get('virtKey') == 'pointB':
        #     cursor.clickLeft(dict_coordinate.get("2DPoseGaol").get("x"),
        #                      dict_coordinate.get("2DPoseGaol").get("y"))
        #     cursor.clickLeft(dict_coordinate.get("pointB").get("x"),
        #                      dict_coordinate.get("pointB").get("y"))
        #
        # elif dict_virtKey_flag.get('virtKey') == 'pointC':
        #     cursor.clickLeft(dict_coordinate.get("2DPoseGaol").get("x"),
        #                      dict_coordinate.get("2DPoseGaol").get("y"))
        #     cursor.clickLeft(dict_coordinate.get("pointC").get("x"),
        #                      dict_coordinate.get("pointC").get("y"))
        #
        # elif dict_virtKey_flag.get('virtKey') == 'pointD':
        #     cursor.clickLeft(dict_coordinate.get("2DPoseGaol").get("x"),
        #                      dict_coordinate.get("2DPoseGaol").get("y"))
        #     cursor.clickLeft(dict_coordinate.get("pointD").get("x"),
        #                      dict_coordinate.get("pointD").get("y"))
        #
        # elif dict_virtKey_flag.get('virtKey') == 'over':
        #     break


def socket_server(port):    # 客户端数据不要超过1024个字节
    server = socket.socket()
    server.bind(('0.0.0.0', port))
    server.listen()
    try:
        while True:
            conn, addr = server.accept()
            print("new conn:", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    print("客户端已断开", data)
                    break
                conn.send('ok'.encode('utf-8'))
                try:
                    lock.acquire()
                    dict_socket_flag['socket'] = data
                    dict_socket_flag['voice'] = str(data, "utf8")
                finally:
                    lock.release()
                    print('socket:', dict_socket_flag.get('socket'))
                    break
                print("客户端数据：", data)
    finally:
        server.close()


def SSH(host, name, pwd):

    while True:
        # if dict_SSH_flag.get('ssh') == '连接小车，启动多点定位导航':
        try:
            client = SshClient()
            client.connect(host, name, pwd)
            flag = 1
            while True:
                if flag == 1:
                    flag = 0
                    print("ssh Connected")
                    # try:
                    #     lock.acquire()
                    #     dict_socket_flag['voice'] = "audioCtrl1"
                    # finally:
                    #     lock.release()
                if dict_socket_flag.get('voice') != "null":
                    voice = dict_socket_flag.get('voice')
                    command = "cd ./liu/audio;python3 AudioPlay.py " + voice
                    print("ssh command:", command)
                    client.command(command)
                    try:
                        lock.acquire()
                        dict_socket_flag['voice'] = "null"
                    finally:
                        lock.release()
        finally:
            client.close()


if __name__ == '__main__':

    '''SSH登录信息'''
    hostname = '192.168.155.2'
    username = 'eaibot'
    password = 'eaibot'

    AutoGUI_threading = threading.Thread(target=auto_gui, name='auto_gui')
    Socket_threading = threading.Thread(target=socket_server, args=(9994, ), name='socket')
    SSH_threading = threading.Thread(target=SSH, args=(hostname, username, password),  name='ssh')

    Socket_threading.start()
    SSH_threading.start()
    AutoGUI_threading.start()
