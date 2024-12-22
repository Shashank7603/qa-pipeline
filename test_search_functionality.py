from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set the path to your ChromeDriver
chrome_driver_path = "C:/Users/MANVI SINGH/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path))
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
