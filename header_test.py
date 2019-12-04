from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import numpy as np


def random_wait():
    wait_time = 4 * np.random.randn() + 20
    if wait_time < 10:
        wait_time += 10
    sleep(wait_time)


