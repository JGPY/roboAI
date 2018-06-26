#Author:Bing Liu
from tkinter import *

class GUI_Tkinter:

    speech_message = None

    def __init__(self):
        root = Tk()  #初始化Tk()
        root.title("18.927交互系统")  # 设置窗口标题
        root.geometry("560x300")  # 设置窗口大小 注意：是x 不是*
        root.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
        Label(root, text="欢迎使用定位导航智能语音交互系统", bg="pink", font=("楷体", 14), width=55, height=1).pack()

        #显示接收速度数据显示信息文本
        Label(root, text="速度数据", bg="pink", font=("楷体", 12), width=33, height=1) \
            .place(x=150, y=67, anchor=CENTER)
        speed_message = Text(root, width=37, height=1)
        speed_message.place(x=150, y=90, anchor=CENTER)

        #显示接收声呐数据显示信息文本
        Label(root, text="声呐数据", bg="pink", font=("楷体", 12), width=33, height=1) \
            .place(x=150, y=120, anchor=CENTER)
        sonar_message = Text(root, width=37, height=1)
        sonar_message.place(x=150, y=143, anchor=CENTER)

        #显示接收语音数据显示信息文本
        Label(root, text="语音数据", bg="pink", font=("楷体", 12), width=33, height=1)\
            .place(x=150, y=194, anchor=CENTER)
        self.speech_message = Text(root, width=37, height=5)
        self.speech_message.place(x=150, y=246, anchor=CENTER)

        # 创建按钮
        Button(root, text="1", width=6, height=1, command=self.test).place(x=350, y=70, anchor=CENTER)
        Button(root, text="2", width=6, height=1, command=self.test).place(x=430, y=70, anchor=CENTER)
        Button(root, text="3", width=6, height=1, command=self.test).place(x=510, y=70, anchor=CENTER)
        Button(root, text="5", width=6, height=1, command=self.test).place(x=350, y=110, anchor=CENTER)
        Button(root, text="6", width=6, height=1, command=self.test).place(x=430, y=110, anchor=CENTER)
        Button(root, text="7", width=6, height=1, command=self.test).place(x=510, y=110, anchor=CENTER)
        Button(root, text="5", width=6, height=1, command=self.test).place(x=350, y=150, anchor=CENTER)
        Button(root, text="6", width=6, height=1, command=self.test).place(x=430, y=150, anchor=CENTER)
        Button(root, text="7", width=6, height=1, command=self.test).place(x=510, y=150, anchor=CENTER)

        Button(root, text="8", width=15, height=3, command=self.test).place(x=430, y=240, anchor=CENTER)

        root.mainloop()  # 进入消息循环
    # #按键发送数据显示
    # def key_message(self, comm, fun):
    #     t_key_message.insert('1.0', "\n命令:", 'end', comm, 'end', "功能：", 'end', fun, 'end', "\n")  # 插入
    #     t_key_message.delete('3.0', END)   # 删除第三行到最后一行
    #     pass
    # #控制按键功能
    # def test(self):
    #     pass
    # def LPower(self):
    #     t_lider_message.insert('1.0', rx_0, END, '\n')
    # def StartM(self):
    #     t_lider_message.insert('1.0', rx_0, END, '\n')
    # def MStatus(self):
    #     t_lider_message.insert('1.0', rx_0, END, '\n')



if __name__ == "__main__":
    GUI = GUI_Tkinter()
