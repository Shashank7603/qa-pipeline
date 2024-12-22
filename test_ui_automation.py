from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set the path to your ChromeDriver
chrome_driver_path = "C:/Users/MANVI SINGH/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path))
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
