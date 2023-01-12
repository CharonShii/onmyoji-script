import os
import pyautogui
import random
import time

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = False
print(pyautogui.size())
main_path = os.getcwd() + "/png"


def random_point(point, offset_point=10):
    return point + random.randint(-offset_point, offset_point)


# 寻找页面中是否有对应的图片存在，并返回其x、y轴位置
# 等待一定次数，未找到图片，返回None
def loading(img_path, number=30):
    point = number
    while point > 0:
        t = random.randint(50, 150) / 100
        print("正在寻找" + img_path + " ", point, t)
        time.sleep(t)
        point = point - 1
        result = pyautogui.locateCenterOnScreen(main_path + img_path, confidence=0.95)
        if result is None:
            continue
        return result
    return None


# 鼠标点击指定位置
def click_mouse(move_to_x, move_to_y, offset_point=10):
    # 延时
    t = random.randint(50, 150) / 100
    time.sleep(t)
    # 偏移，偏移量由offset_point决定，默认±10
    px = random_point(move_to_x, offset_point)
    py = random_point(move_to_y, offset_point)
    # 鼠标左键点击
    pyautogui.leftClick(x=px, y=py)
    print("点击", px, py)
