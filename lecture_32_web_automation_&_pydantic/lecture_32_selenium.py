from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
driver.implicitly_wait(10)
print(driver.title)

sleep(20)
search_bar = driver.find_element(By.NAME, "q")
sleep(5)
search_bar.clear()
sleep(5)
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
sleep(30)

driver.close()
