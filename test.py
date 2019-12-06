from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import numpy as np

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
button = browser.find_element_by_id("su")
print(button)
print(button.get_attribute('class'))
print(button.get_property('value'))