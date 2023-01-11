import action as ac


def yuhun_duiyuan():
    while True:
        result = ac.loading("/shengli.png", 60)
        ac.click_mouse(result.x, result.y, 40)
        result = ac.loading("/tiaozwancheng.png")
        ac.click_mouse(result.x, result.y, 60)


def yuhun_duizhang():
    while True:
        result = ac.loading("/tiaozhan_yuhunduizhang.png")
        ac.click_mouse(result.x, result.y)
        result = ac.loading("/shengli.png")
        ac.click_mouse(result.x, result.y, 40)
        result = ac.loading("/tiaozwancheng.png")
        ac.click_mouse(result.x, result.y, 60)
