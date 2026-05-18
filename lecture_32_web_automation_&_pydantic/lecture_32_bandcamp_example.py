from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome()
driver.get("https://daily.bandcamp.com/features/myriam-gendron-mayday-interview")
driver.implicitly_wait(10)
print(driver.title)

sleep(10)
driver.find_element(By.XPATH, "//icon").click()
sleep(60)

driver.close()
