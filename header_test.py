from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import numpy as np

browser = webdriver.Chrome()
browser.get("https://whatismyipaddress.com/blacklist-check")
button = browser.find_element_by_name("Lookup Hostname")
button.click()
all_img = browser.find_elements_by_xpath("//table//img")
for i in all_img:
    print(i.get_attribute('src'))






