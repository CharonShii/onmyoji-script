import action as ac
import loaction as la
import pyautogui

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


# 获取指定窗口
title = "任务管理器"
matches = pyautogui.getWindowsWithTitle(title)
if len(matches) > 0:
    # do something with the first match
    match = matches[0]
    print(matches)
    print(match)
else:
    print("No window with title " + title + " was found.")