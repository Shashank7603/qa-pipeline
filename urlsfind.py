from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.google.com")
print("ChromeDriver is working!")
driver.quit()
