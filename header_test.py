from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions as se_exception
import time


driver = webdriver.Chrome()
print(time.time())
driver.get("https://www.airbnb.com")
print(time.time())
driver.implicitly_wait(10)
print(time.time())

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "my_id"))
    )
except se_exception.TimeoutException:
    print("here")

finally:
    driver.quit()