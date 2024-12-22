from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set the path to your ChromeDriver
chrome_driver_path = "/usr/bin/chromedriver"

driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("http://127.0.0.1:54069")
driver.maximize_window()

try:
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("johndoe@example.com")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Patient added successfully" in driver.page_source

    driver.find_element(By.ID, "name").send_keys("")  # Missing name
    driver.find_element(By.ID, "email").send_keys("invalid_email")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Invalid input" in driver.page_source

finally:
    driver.quit()
