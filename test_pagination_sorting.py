from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Navigate to the URL
driver.get("http://127.0.0.1:54069")


try:
    # Wait for the next button to be clickable, then click it
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "next_page"))
    )
    next_button.click()

    # Wait for the next page to load and assert the page title or content
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Page 2")
    )

    # Wait for the sort button to be clickable, then click it
    sort_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "sort_by_name"))
    )
    sort_button.click()

    # Wait for the sorted page to load and assert the content
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Sorted by Name")
    )

finally:
    # Close the browser after the operations are done
    driver.quit()
