import action as ac


def yuhun_duizhang():
    while True:
        result = ac.loading("/tiaozhan_yuhunduizhang.png")
        ac.click_mouse(result.x, result.y)
        result = ac.loading("/shengli.png")
        ac.click_mouse(result.x, result.y)
        result = ac.loading("/tiaozwancheng.png")
        ac.click_mouse(result.x, result.y)


yuhun_duizhang()
# tansuo = ac.loading("/tiaozhan_yuhunduizhang.png")
# print(tansuo)
