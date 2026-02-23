from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(20)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 40)
img3 = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#image-container img:nth-of-type(3)")))

print(img3.get_attribute("src"))

driver.quit()
