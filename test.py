import queue
import time

import action as ac
import loaction as la
import pyautogui
from threading import Thread
from queue import Queue

# size = pyautogui.size()
# print(size)
# la.kun28_duiyuan()

# tansuo = ac.loading("/tiaozhan_yuhunduizhang.png")
# print(tansuo)


# a = pyautogui.locateOnScreen(ac.main_path + "/Snipaste_2023-01-13_14-06-44.png",
#                             region=(0, 0, round(size.width / 2), size.height))
# print(a)
# b = pyautogui.center(a)
# print(b)

# 参数region(左、上、宽、高)，限定查找的区域
# c = pyautogui.locateCenterOnScreen(ac.main_path + "/Snipaste_2023-01-13_14-06-44.png",
#                                   region=(0, 0, round(size.width / 2), size.height), confidence=0.95)
# print(c)

# 线程安全队列
q = queue.Queue()


# 获取窗口位置，只搜索窗口位置出现的图片
def getrenwu():
    title = "任务管理器"
    while True:
        time.sleep(1)
        matches = pyautogui.getWindowsWithTitle(title)
        if len(matches) > 0:
            # do something with the first match
            match = matches[0]
            print(match)
            c = pyautogui.locateCenterOnScreen(ac.main_path + "/Snipaste_2023-01-13_16-38-35.png",
                                               region=(match.left, match.top, match.width, match.height),
                                               confidence=0.95)
            print(c)
            q.put([c.x, c.y])
        else:
            print("No window with title " + title + " was found.")


# 获取窗口位置，只搜索窗口位置出现的图片
def getexpor():
    title = "文件资源管理器"
    while True:
        time.sleep(1)
        matches = pyautogui.getWindowsWithTitle(title)
        if len(matches) > 0:
            # do something with the first match
            match = matches[0]
            print(match)
            c = pyautogui.locateCenterOnScreen(ac.main_path + "/Snipaste_2023-01-13_16-41-28.png",
                                               region=(match.left, match.top, match.width, match.height),
                                               confidence=0.95)
            print(c)
            q.put([c.x, c.y])
        else:
            print("No window with title " + title + " was found.")


# 多线程处理不同窗口的判断
t1 = Thread(target=getrenwu)
t1.start()
t2 = Thread(target=getexpor)
t2.start()

# 点击队列中记录的坐标，先进先出
while True:
    item = q.get()
    if item is None:
        continue
    ac.click_mouse(item[0], item[1])
    print(item)
    q.task_done()

t1.join()
t2.join()

q.join()
