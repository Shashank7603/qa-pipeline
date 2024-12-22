from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set the path to your ChromeDriver
chrome_driver_path = "/usr/bin/chromedriver"

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Headless mode
chrome_options.add_argument("--no-sandbox")  # No sandbox mode
chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage
chrome_options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging for debugging

# Initialize WebDriver with options
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
driver.get("http://127.0.0.1:54069")

try:
    search_box = driver.find_element(By.ID, "search")
    search_box.send_keys("John Doe")
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)
    assert "John Doe" in driver.page_source

    search_box.clear()
    search_box.send_keys("Nonexistent Patient")
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)
    assert "No results found" in driver.page_source

finally:
    driver.quit()
