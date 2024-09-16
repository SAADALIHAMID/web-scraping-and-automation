import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(4)
search=driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
search.send_keys("House of dragon")
search.send_keys(Keys.ENTER)
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[13]/div[4]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[8]/div/div/div/div/div/div[1]/div/div/span/a/h3").click()
time.sleep(5)
driver.save_screenshot("D:\BSCS\selenium.py/web.png")
driver.close()
