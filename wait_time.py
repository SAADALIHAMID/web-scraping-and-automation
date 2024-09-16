import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/python/pandas/default.asp")
time.sleep(9)
search=driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/input")
search.send_keys('PYTHON')
search.send_keys(Keys.ENTER)