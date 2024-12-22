from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set the path to your ChromeDriver
chrome_driver_path = "C:/Users/MANVI SINGH/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("http://127.0.0.1:54069")

try:
    next_button = driver.find_element(By.ID, "next_page")
    next_button.click()
    time.sleep(2)
    assert "Page 2" in driver.page_source

    sort_button = driver.find_element(By.ID, "sort_by_name")
    sort_button.click()
    time.sleep(2)
    assert "Sorted by Name" in driver.page_source

finally:
    driver.quit()
