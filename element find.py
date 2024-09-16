import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup WebDriver
driver = webdriver.Chrome()

# Open the target website
driver.get("https://www.tutorialsfreak.com/")

# Find the element by XPath
element = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/section[3]/div/div/div[2]/div/div/div/div[6]/div/div/a/div/p")

# Print the text of the element (if it has any)
print(element.text)

# Click the element
element.click()

# Optional: Pause for a while to see the effect
time.sleep(5)

# Close the browser
driver.quit()



# driver.close()