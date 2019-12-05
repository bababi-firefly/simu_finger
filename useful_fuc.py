from time import sleep
import numpy as np
import win32api
import win32con


# 随机时间等待
def random_wait():
    wait_time = 4 * np.random.randn() + 20
    if wait_time < 10:
        wait_time += 10
    sleep(wait_time)


# 按比例调整屏幕分辨率
def random_resolution_size():
    dm = win32api.EnumDisplaySettings(None, 0)
    dm.PelsHeight = 768
    dm.PelsWidth = 1366
    dm.BitsPerPel = 32
    dm.DisplayFixedOutput = 0
    win32api.ChangeDisplaySettings(dm, 0)


def get_UA(type):
    """FireFox, Google Chrome, Edge, IE"""
    # 通过类型，远程连接数据库，获取UA信息，参数type已通过webdriver启动时确定。

def conn_mysql():
    """
    连接远程数据库，返回游标
    :return:cursor
    """