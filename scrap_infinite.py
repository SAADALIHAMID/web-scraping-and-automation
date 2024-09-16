import time
from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.ajio.com/s/footwear-4792-56592?query=%3Arelevance%3Al1l3nestedcategory%3AWomen%20-%20Sneakers&curated=true&curatedid=footwear-4792-56592&gridColumns=3")
time.sleep(5)

# Scroll loop
while True:
    # Get the current scroll height
    height = driver.execute_script("return document.body.scrollHeight")
    print(f"Current height: {height}")
    
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # Wait for new content to load
    time.sleep(3)  # Allow time for dynamic content to load
    
    # Get the new scroll height after content has loaded
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(f"New height: {new_height}")
    
    # Break the loop if the scroll height hasn't changed
    if height == new_height:
        print("Reached the end of the page.")
        break

# Optionally close the browser after scrolling
driver.close()

    

