import time
import os
import csv
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# List of websites to check
websites = [
    "https://www.marketingtechnews.net/",
    "https://alyze.co.uk/",
    "https://wire19.com/",
    "https://www.oemsecrets.com/articles/",
    "https://blog.contactpigeon.com/",
    "https://www.apress.com/gp/",
    "https://developergang.com/",
    "https://makeanapplike.com/"
]

# Create a new folder for output
output_folder = 'guest_post_opportunities'
os.makedirs(output_folder, exist_ok=True)

# Path to the CSV file
csv_file_path = os.path.join(output_folder, 'guest_post_opportunities.csv')

def check_for_guest_post_opportunities(url):
    """
    Check if a website has pages indicating guest post opportunities.
    """
    driver = webdriver.Chrome()  # Ensure 'chromedriver' is in your PATH

    result = {"url": url, "opportunities": []}

    try:
        driver.get(url)
        driver.implicitly_wait(5)  # Wait for the page to load

        # Keywords to search for
        keywords = ["guest post", "write for us", "contributor", "submit an article"]

        # Check if any of the keywords are present in the page
        for keyword in keywords:
            if keyword.lower() in driver.page_source.lower():
                result["opportunities"].append(keyword)

    except Exception as e:
        print(f"Error processing {url}: {e}")
        result["opportunities"] = ["Error"]

    finally:
        driver.quit()
    
    return result

def process_website(url):
    """
    Process a single website to check for guest post opportunities.
    """
    print(f"Processing {url}...")
    return check_for_guest_post_opportunities(url)

def main():
    # Use ThreadPoolExecutor to run checks concurrently
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(process_website, websites))
    
    # Write results to CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['url', 'opportunities']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow({'url': result['url'], 'opportunities': ', '.join(result['opportunities'])})

    print(f"Results saved to {csv_file_path}")

if __name__ == "__main__":
    main()



    