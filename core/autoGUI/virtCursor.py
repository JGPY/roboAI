#Author:Jason Lou
import pyautogui


class virtCursor:

    width = 0
    height = 0

    currentMouseX = 0
    currentMouseY = 0

    def __init__(self):
        self.width, self.height = pyautogui.size() #获取屏幕分辨率
        self.mousePosition()
        pass

    def clickLeft(self, x=None, y=None, button='left'):
        pyautogui.click(x, y, button)

    def clickRight(self, x=None, y=None, button='left'):
        pyautogui.click(x, y, button)

    def doubleClick(self, x=None, y=None, button='left'):
        pyautogui.doubleClick(x, y, button)

    def moveTo(self, x=None, y=None):
        pyautogui.moveTo(x, y)

    def moveRel(self, x=None, y=None):
        pyautogui.moveRel(x, y)

    def moveDown(self, x0=None, y0=None):
        pyautogui.mouseDown(x0, y0)

    def moveUp(self, x1=None, y1=None):
        pyautogui.mouseUp(x1, y1)

    def mousePosition(self):
        self.currentMouseX, self.currentMouseY = pyautogui.position()

if __name__ == '__main__':
    cursor = virtCursor()
    print("宽：", cursor.width, "高", cursor.height)
    print("x：", cursor.currentMouseX, "y", cursor.currentMouseY)
    print(pyautogui.size())
    print(pyautogui.position())

