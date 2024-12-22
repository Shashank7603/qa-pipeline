from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    time.sleep(2)
    assert "Required field" in driver.page_source

    driver.find_element(By.ID, "go_to_dashboard").click()
    time.sleep(2)
    assert "Dashboard" in driver.page_source

finally:
    driver.quit()
