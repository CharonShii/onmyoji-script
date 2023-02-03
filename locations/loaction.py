import action as ac
import thread_loaction as tl


# 御魂队员
def yuhun_duiyuan():
    while True:
        result = ac.loading("/shengli.png", 60)
        ac.click_mouse(result.x, result.y, 40)
        result = ac.loading("/tiaozwancheng.png")
        ac.click_mouse(result.x, result.y, 60)


# 御魂队长
def yuhun_duizhang():
    while True:
        result = ac.loading("/tiaozhan_yuhunduizhang.png")
        ac.click_mouse(result.x, result.y)
        result = ac.loading("/shengli.png")
        ac.click_mouse(result.x, result.y, 40)
        result = ac.loading("/tiaozwancheng.png")
        ac.click_mouse(result.x, result.y, 60)


# 困28队员
def kun28_duiyuan():
    while True:
        result = ac.loading("/shengli.png")
        if result is not None:
            ac.click_mouse(result.x, result.y, 40)
        else:
            result = ac.loading("/shengli.png", 1)
            ac.click_mouse(result.x, result.y)

        result = ac.loading("/tiaozwancheng.png", 1)
        if result is not None:
            ac.click_mouse(result.x, result.y, 60)

        result = ac.loading("/jieshou.png", 1)
        if result is not None:
            ac.click_mouse(result.x, result.y, 60)


# 困28队长，未完成
def kun28_duizhang():
    while True:
        result = ac.loading("/shengli")
        ac.click_mouse(result.x, result.y)
