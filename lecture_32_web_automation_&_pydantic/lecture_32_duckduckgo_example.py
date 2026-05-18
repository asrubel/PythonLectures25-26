from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.duckduckgo.org/")
driver.implicitly_wait(10)
print(driver.title)

sleep(10)
search = driver.find_element(By.NAME, "q")
search.clear()
search.send_keys("python")
search.submit()

sleep(20)

results = driver.find_elements(By.XPATH, ".//li")
for r in results:
    print(r.text)

driver.close()
