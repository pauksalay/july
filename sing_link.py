from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_subscription_link():
    # Chrome options
    options = Options()
    options.add_argument('--headless')  # Remove this line if you want to see the browser
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # ChromeDriver path (adjust if needed)
    driver = webdriver.Chrome(options=options)

    try:
        url = "https://jc.809089.xyz/https://dashboard.sing-link.com"
        driver.get(url)

        time.sleep(5)  # wait for page to load fully

        # Try finding the subscription link
        elements = driver.find_elements(By.TAG_NAME, "a")
        for elem in elements:
            href = elem.get_attribute("href")
            if href and "sub" in href:
                print("Found subscription link:")
                print(href)
                break
        else:
            print("No subscription link found.")

    finally:
        driver.quit()

if __name__ == "__main__":
    get_subscription_link()