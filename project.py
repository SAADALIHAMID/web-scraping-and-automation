import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Ensure the 'data' directory exists
os.makedirs('data', exist_ok=True)

# Initialize the WebDriver
driver = webdriver.Chrome()

query = "laptop"
file = 0

try:
    for i in range(1, 20):
        driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=3HKD1SIJKEIJS&sprefix=la%2Caps%2C435&ref=nb_sb_ss_ts-doa-p_2")
        elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
        
        print(f"{len(elems)} Items found on page {i}")

        for elem in elems:
            d = elem.get_attribute("outerHTML")
            
            # Write to the file
            with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
                f.write(d)
            file += 1

        # Wait before loading the next page
        time.sleep(5)
finally:
    # Close the browser after all pages are processed
    driver.close()
