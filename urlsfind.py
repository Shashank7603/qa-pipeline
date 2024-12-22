from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "/usr/bin/chromedriver"
# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Headless mode
chrome_options.add_argument("--no-sandbox")  # No sandbox mode
chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage
chrome_options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging for debugging

# Initialize WebDriver with options
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
driver.get("https://www.google.com")
print("ChromeDriver is working!")
driver.quit()
