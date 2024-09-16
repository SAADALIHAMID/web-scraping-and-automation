from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.ajio.com/s/footwear-4792-56592?query=%3Arelevance%3Al1l3nestedcategory%3AWomen%20-%20Sneakers&curated=true&curatedid=footwear-4792-56592&gridColumns=3")
time.sleep(5)
height=driver.execute_script("return document.body.scrollHeight")
print(height)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight) ")