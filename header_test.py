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

# 识别selenium的方法
# 1 window.navigator.webdriver的值为True
#    应对方法 options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 2 通过查找js中是否包含$cdc_类的变量来确定
#    应对方法，vim编辑chromedriver文件，并将此串替换为等长的其它串
# 3 window.navigator.languages中不要出现zh中文标识等
#   window.navigator.language应为en

driver1 = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver"
driver2 = r"C:\Users\BABABI\Desktop\chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(executable_path=driver2)
browser.get("http://www.baidu.com")






