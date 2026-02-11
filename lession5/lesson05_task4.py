from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")

input_field = driver.find_element(By.ID, "username")

input_field.send_keys("tomsmith")

input_field = driver.find_element(By.ID, "password")

input_field.send_keys("SuperSecretPassword!")


driver.find_element(By.CSS_SELECTOR, "button.radius").click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, 'flash')))

text = element.text
print(text)

driver.quit()
