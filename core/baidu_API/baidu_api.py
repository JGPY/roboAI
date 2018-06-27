#Author:Bing Liu
from aip import AipSpeech
import time
import pygame

import numpy as np
from pyaudio import PyAudio, paInt16
from datetime import datetime
import wave
from tkinter import *

class baiduAI:

    """ 你的 APPID AK SK """
    APP_ID = 'xxx'
    API_KEY = 'xxx'
    SECRET_KEY = 'xxx'
    client = None


    # define of params
    NUM_SAMPLES = 2000
    framerate = 16000
    # paInt16 = 8
    channels = 1
    sampwidth = 2
    # record time
    TIME = 5


    def __init__(self):
        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    '''功能：字符串转化成声音'''
    def strToVoice(self,str, name = "auido.mp3"):
        result = self.client.synthesis(str, 'zh', 1, {
            'vol': 5,
        })
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('../../data/'+name, 'wb') as f:
                f.write(result)


    '''功能：声音转化成字符串'''
    def voiceToStr(self, Path):
        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                return fp.read()
        # 识别本地文件
        result = self.client.asr(get_file_content(Path), 'wav', 16000, {
            'lan': 'zh',
        })
        # 从URL获取文件识别
        self.client.asr('', 'wav', 16000, {
            'url': 'http://121.40.195.233/res/16k_test.pcm',
            'callback': 'http://xxx.com/receive',
        })
        print(result["result"])

    '''功能：声音播放'''
    def play(self, music):
        freq = 16000  # audio  quality
        bitsize = -16  # unsigned 16 bit
        channels = 2  # 1 is mono, 2 is stereo

        filePath = r'../../data/'+music
        pygame.mixer.init(freq, bitsize, channels)
        print("语音合成")
        track = pygame.mixer.music.load(filePath)
        pygame.mixer.music.fadeout(1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.music.stop()

    '''功能：声音采集'''
    def save_wave_file(self,filename, data):
        '''''save the date to the wav file'''
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.sampwidth)
        wf.setframerate(self.framerate)
        wf.writeframes(b"".join(data))
        wf.close()


    def record_wave(self):
         # open the input of wave
        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1,
                            rate=self.framerate, input=True,
                            frames_per_buffer=self.NUM_SAMPLES)
        save_buffer = []
        count = 0
        while count < self.TIME * 4:
             # read NUM_SAMPLES sampling data
            string_audio_data = stream.read(self.NUM_SAMPLES)
            save_buffer.append(string_audio_data)
            count += 1
            print('.')

        # filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav"
        self.save_wave_file("../../data/auido.wav", save_buffer)
        # save_buffer = []
        print("auido.wav", "saved")
        self.voiceToStr("../../data/auido.wav")


    def my_test_button(self, root, label_text, button_text, button_func):
        '''''''function of creat label and button'''
        # label details
        label = Label(root)
        label['text'] = label_text
        label.pack()
        # label details
        button = Button(root)
        button['text'] = button_text
        button['command'] = button_func
        button.pack()


if __name__ == '__main__':
    syn = "欢迎使用定位导航智能语音交互系统"
    AI = baiduAI()
    # AI.strToVoice(syn,"auido.mp3")
    # AI.play("auido.mp3")

    root = Tk()
    AI.my_test_button(root, "Record a wave", "clik to record", AI.record_wave)


    # AI.my_test_button(root, "Record a wave", "clik to record", AI.voiceToStr("../../data/auido.wav") )
    root.mainloop()
    pass



    #
# ygame.init() 进行全部模块的初始化，
# pygame.mixer.init() 或者只初始化音频部分
# pygame.mixer.music.load('xx.mp3') 使用文件名作为参数载入音乐 ,音乐可以是ogg、mp3等格式。载入的音乐不会全部放到内容中，而是以流的形式播放的，即在播放的时候才会一点点从文件中读取。
# pygame.mixer.music.play()播放载入的音乐。该函数立即返回，音乐播放在后台进行。
# play方法还可以使用两个参数
# pygame.mixer.music.play(loops=0, start=0.0) loops和start分别代表重复的次数和开始播放的位置。
# pygame.mixer.music.stop() 停止播放，
# pygame.mixer.music.pause() 暂停播放。
# pygame.mixer.music.unpause() 取消暂停。
# pygame.mixer.music.fadeout(time) 用来进行淡出，在time毫秒的时间内音量由初始值渐变为0，最后停止播放。
# pygame.mixer.music.set_volume(value) 来设置播放的音量，音量value的范围为0.0到1.0。
# pygame.mixer.music.get_busy() 判断是否在播放音乐,返回1为正在播放。
# pygame.mixer.music.set_endevent(pygame.USEREVENT + 1) 在音乐播放完成时，用事件的方式通知用户程序，设置当音乐播放完成时发送pygame.USEREVENT+1事件给用户程序。 pygame.mixer.music.queue(filename) 使用指定下一个要播放的音乐文件，当前的音乐播放完成后自动开始播放指定的下一个。一次只能指定一个等待播放的音乐文件。
