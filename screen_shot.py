import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.tutorialsfreak.com/")
# driver.save_screenshot("D:/BSCS/selenium.py/full-page.png")
element = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/section[11]/div/div/div[6]/div/div[1]/div[1]/img").screenshot("D:/BSCS/selenium.py/pics.png")


