Name
--
    robotAI

Author information:
---
    Author:Jason Lou
    Email:vip.iotworld@gmail.com
    Website:www.iotworld.vip
    Github:www.github.com/JGPY

Environment:
---
    OS:ubuntu16.04
    Project IDE:Pycharm
    Project Interpreter:python3.6
    
    
Evolution:
---
    version：main_V1.*.py
        Functional_description:
            室内设置ABCD四个目标点，通过模拟鼠标和键盘自动完成ABCD四个目标点的启动设置。
        Dependent_file:
            ./core/AutoGUI/*
            ./core/Socket/*
            ./core/SSH/*
---            
    version：main_V2.*.py
        Functional_description:
            室内设置ABCD四个目标点。
            通过手机人机交互识别指令后，通过socket将指令传输给本系统程序。
            通过HTT调用WebAPI自动完成ABCD四个目标点的启动设置,
            并在到达每个目标点后通过SSH连接下位机调用脚本播放一段语音，再进行下一个目标点。
        Dependent_file:
            ./core/Audio/*
            ./core/Socket/*
            ./core/SSH/*
            ./core/HTTP/*
            ./core/baidu_API/*
        
 ![Image text](https://github.com/JGPY/roboAI/blob/master/data/image/V2%E7%A8%8B%E5%BA%8F%E6%A1%86%E6%9E%B6.png)
 ![Image text](https://github.com/JGPY/roboAI/blob/master/data/image/V2%E7%A1%AC%E4%BB%B6%E5%9B%BE.png)   

---              
    version：main_V3.*.py
        Dependent_file:
            ./core/Audio/*
            ./core/SSH/*
            ./core/HTTP/*
            ./core/Face/*  
