import queue
from threading import Thread

import action as ac


q = queue.Queue()
window_title = ["任务管理器", "文件资源管理器"]
t_arr = []


def start_thread():
    for title in window_title:
        matches = ac.pag.getWindowsWithTitle(title)
        match = matches[0]

        t1 = Thread(target=aaaa)
        t_arr.append(t1)
    for t in t_arr:
        t.start()
    for t in t_arr:
        t.join()


def aaaa():
    return 1


def queue_move():
    while True:
        qitem = q.get()
        if qitem is None:
            continue
        ac.click_mouse(qitem.x, qitem.y, qitem.offset)
        q.task_done()



