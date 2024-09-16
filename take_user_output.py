import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Setup WebDriver
driver = webdriver.Chrome()

# Open the target website
driver.get("https://www.facebook.com/")
email=driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
email.send_keys("emmadalesco@gmail.com")
time.sleep(3)

password=driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
password.send_keys("qwerty91225123")
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()
time.sleep(7)