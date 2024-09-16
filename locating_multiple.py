import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
query="laptop"
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=3HKD1SIJKEIJS&sprefix=la%2Caps%2C435&ref=nb_sb_ss_ts-doa-p_1_2")
    elems = driver.find_elements(By.CLASS_NAME, "puisg-col-inner")
# print(elem.get_attribute("outerHTML"))
    print(f"{len(elems)}Items found")
    for elem in elems:
        print(elem.text)
    time.sleep(5)
    driver.close()