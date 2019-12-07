from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import numpy as np
import sys


# 随机时间等待
def random_wait():
    wait_time = 4 * np.random.randn() + 20
    if wait_time < 10:
        wait_time += 10
    sleep(wait_time)


# 按比例调整屏幕分辨率
class ScreenRes(object):
    @classmethod
    def set(cls, width=None, height=None, depth=32):
        '''
        Set the primary display to the specified mode
        '''
        if width and height:
            print('Setting resolution to {}x{}'.format(width, height, depth))
        else:
            print('Setting resolution to defaults')

        if sys.platform == 'win32':
            cls._win32_set(width, height, depth)
        elif sys.platform.startswith('linux'):
            cls._linux_set(width, height, depth)
        elif sys.platform.startswith('darwin'):
            cls._osx_set(width, height, depth)

    @classmethod
    def get(cls):
        if sys.platform == 'win32':
            return cls._win32_get()
        elif sys.platform.startswith('linux'):
            return cls._linux_get()
        elif sys.platform.startswith('darwin'):
            return cls._osx_get()

    @classmethod
    def get_modes(cls):
        if sys.platform == 'win32':
            return cls._win32_get_modes()
        elif sys.platform.startswith('linux'):
            return cls._linux_get_modes()
        elif sys.platform.startswith('darwin'):
            return cls._osx_get_modes()

    @staticmethod
    def _win32_get_modes():
        '''
        Get the primary windows display width and height
        '''
        import win32api
        from pywintypes import DEVMODEType, error
        modes = []
        i = 0
        try:
            while True:
                mode = win32api.EnumDisplaySettings(None, i)
                modes.append((
                    int(mode.PelsWidth),
                    int(mode.PelsHeight),
                    int(mode.BitsPerPel),
                    ))
                i += 1
        except error:
            pass

        return modes

    @staticmethod
    def _win32_get():
        '''
        Get the primary windows display width and height
        '''
        import ctypes
        user32 = ctypes.windll.user32
        screensize = (
            user32.GetSystemMetrics(0),
            user32.GetSystemMetrics(1),
            )
        return screensize

    @staticmethod
    def _win32_set(width=None, height=None, depth=32):
        '''
        Set the primary windows display to the specified mode
        '''
        # Gave up on ctypes, the struct is really complicated
        #user32.ChangeDisplaySettingsW(None, 0)
        import win32api
        from pywintypes import DEVMODEType
        if width and height:

            if not depth:
                depth = 32

            mode = win32api.EnumDisplaySettings()
            mode.PelsWidth = width
            mode.PelsHeight = height
            mode.BitsPerPel = depth

            win32api.ChangeDisplaySettings(mode, 0)
        else:
            win32api.ChangeDisplaySettings(None, 0)


    @staticmethod
    def _win32_set_default():
        '''
        Reset the primary windows display to the default mode
        '''
        # Interesting since it doesn't depend on pywin32
        import ctypes
        user32 = ctypes.windll.user32
        # set screen size
        user32.ChangeDisplaySettingsW(None, 0)

    @staticmethod
    def _linux_set(width=None, height=None, depth=32):
        raise NotImplementedError()

    @staticmethod
    def _linux_get():
        raise NotImplementedError()

    @staticmethod
    def _linux_get_modes():
        raise NotImplementedError()

    @staticmethod
    def _osx_set(width=None, height=None, depth=32):
        raise NotImplementedError()

    @staticmethod
    def _osx_get():
        raise NotImplementedError()

    @staticmethod
    def _osx_get_modes():
        raise NotImplementedError()


def get_UA(type):
    """FireFox, Google Chrome, Edge, IE"""
    # 通过类型，远程连接数据库，获取UA信息，参数type已通过webdriver启动时确定。


def conn_mysql():
    """
    连接远程数据库，返回游标
    :return:cursor
    """


class IpThings(object):
    check_ip_url = "https://whatismyipaddress.com/blacklist-check"

    def __init__(self, ip):
        self.ip = ip

    def check_if_ip_black(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        desired_capabilities = DesiredCapabilities().CHROME
        desired_capabilities['pageLoadStrategy'] = 'none'
        browser = webdriver.Chrome(chrome_options=chrome_options,
                                   executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver",
                                   desired_capabilities=desired_capabilities)

        browser.get(self.check_ip_url)
        sleep(5)
        button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "Lookup Hostname"))
        )
        button.click()
        sleep(20)
        all_check_tag = browser.find_elements_by_xpath("//table[1]//img")
        # 获取到了所有的检验链接，接下来统计有多少个red
        red = 0
        sleep(10)
        Blacklists = []
        # 先获取所有链接
        for i in all_check_tag:
            url = i.get_attribute("src")
            print(url)
            Blacklists.append(url)

        for black in Blacklists:
            browser.get(black)
            sleep(0.1)
            if "bl_red_" in browser.page_source:
                red += 1
        return red


