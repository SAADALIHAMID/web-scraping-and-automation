import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
query="laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=3HKD1SIJKEIJS&sprefix=la%2Caps%2C435&ref=nb_sb_ss_ts-doa-p_1_2")
elem = driver.find_element(By.CLASS_NAME, "a-size-medium a-color-base a-text-normal")
print(elem.get_attribute("outerHTML"))
time.sleep(5)
driver.close()