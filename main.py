import os
import pyautogui
import random
import time

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = False
print(pyautogui.size())


# 鼠标点击指定位置
def click_mouse(move_to_x, move_to_y, offset_point):
    # 延时
    t = random.randint(50, 150) / 100
    time.sleep(t)
    # 偏移
    offset = random.randint(-offset_point, offset_point)
    print(move_to_x + offset)
    print(move_to_y + offset)
    # 鼠标左键点击
    pyautogui.leftClick(x=move_to_x + offset, y=move_to_y + offset)


# 将鼠标移到指定位置
def mouse_move_to(move_to_x, move_to_y, offset_point):
    # 偏移
    offset = random.randint(-offset_point, offset_point)
    print(move_to_x + offset)
    print(move_to_y + offset)
    # 移动鼠标到指定位置
    pyautogui.moveTo(move_to_x + offset, move_to_y + offset, 0.5)


# 寻找页面中是否有对应的图片存在，并返回其x、y轴位置
# 等待一定次数，未找到图片，返回None
def loading(img_path, number):
    point = number
    while point > 0:
        point = point - 1
        result = pyautogui.locateCenterOnScreen(img_path, confidence=0.95)
        if (result != None):
            return result
        t = random.randint(50, 150) / 100
        time.sleep(t)
    if (point <= 0):
        return None


def yunhun_danren():
    while True:
        tiaozhan = loading(os.getcwd() + "/png/tiaozhan.png", 30)  # 八岐大蛇挑战的图片
        if (tiaozhan == None):
            print("未能找到八岐大蛇挑战入口")
            return
        click_mouse(tiaozhan.x, tiaozhan.y, 20)  # 点击八岐大蛇挑战图片

        tiaozwancheng = loading(os.getcwd() + "/png/tiaozwancheng.png", 50)  # 八岐大蛇挑战完成的图片
        if (tiaozwancheng == None):
            print("未能找到八岐大蛇挑战完成入口")
            return
        time.sleep(1)
        click_mouse(tiaozwancheng.x, tiaozwancheng.y, 80)  # 点击八岐大蛇挑战完成图片


# 御魂挑战
yunhun_danren()


def mengjun():
    while True:
        mengjunzhandou = loading(os.getcwd() + "/png/mengjunzhandou.png", 30)
        if (mengjunzhandou == None):
            print("未能找到梦境挑战入口")
            return
        click_mouse(mengjunzhandou.x, mengjunzhandou.y, 40)  # 点击八岐大蛇挑战图片

        tiaozwancheng = loading(os.getcwd() + "/png/tiaozwancheng.png", 50)
        if (tiaozwancheng == None):
            print("未能找到梦境挑战完成入口")
            return
        click_mouse(tiaozwancheng.x, tiaozwancheng.y, 200)  # 点击八岐大蛇挑战完成图片

# mengjun()


def zhounianqing():
    while True:
        zhounianzhandou = loading(os.getcwd() + "/png/zhounianzhandou.png", 30)
        if (zhounianzhandou == None):
            print("未能找到zhandou入口")
            return
        click_mouse(zhounianzhandou.x, zhounianzhandou.y, 30)  # 点击八岐大蛇挑战图片

        huodejiangli = loading(os.getcwd() + "/png/huodejiangli.png", 50)
        if (huodejiangli == None):
            print("未能找到梦境挑战入口")
            return
        click_mouse(huodejiangli.x, huodejiangli.y + 500, 40)  # 点击八岐大蛇挑战图片

        shengli = loading(os.getcwd() + "/png/shengli.png", 50)
        if (shengli == None):
            print("未能找到梦境挑战完成入口")
            return
        click_mouse(shengli.x, shengli.y + 300, 50)  # 点击八岐大蛇挑战完成图片

# zhounianqing()