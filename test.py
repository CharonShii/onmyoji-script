import os
import pyautogui

tansuo = pyautogui.locateCenterOnScreen(os.getcwd() + "/png/huodejiangli.png", confidence=0.95)  # 探索灯笼的图片
print(tansuo)



