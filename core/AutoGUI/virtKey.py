#Author:Bing Liu
import pyautogui

class virtKey:

    def __init__(self):
        pass

    def keyDown(self, key):
        pyautogui.keyDown(key)

    def keyUp(self, key):
        pyautogui.keyUp(key)

    def press(self, key):
        pyautogui.press(key)

    def press(self, k1, k2, k3):
        pyautogui.hotkey(k1, k2, k3)

    def openTerminal(self):
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('alt')
        pyautogui.press('t')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('alt')

    def input(self, str):
        pyautogui.typewrite(str, interval=0.25) #每次输入之间暂停0.25秒

    def enter(self):
        pyautogui.press('enter')

    def closeFront(self):
        pyautogui.keyDown('alt')
        pyautogui.press('f4')
        pyautogui.keyUp('alt')

    def winMax(self):
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('win')
        pyautogui.press('up')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('win')

    def winMin(self):
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('win')
        pyautogui.press('down')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('win')

    def screenshot(self):
        return pyautogui.screenshot() #返回一个Pillow/PIL的Image对象

    def screenshotSize(self, x0, y0, x1, y1):
        return pyautogui.screenshot(region=(x0, y0, x1, y1)) #返回一个Pillow/PIL的Image对象


if __name__ == '__main__':
    keyboard = virtKey()
    keyboard.openTerminal()
    keyboard.input("ls")
    keyboard.enter()
    keyboard.closeFront()

