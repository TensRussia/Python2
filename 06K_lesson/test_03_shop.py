import pytest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form(driver):
    driver.get("https://www.saucedemo.com/")
    driver.set_page_load_timeout(10)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.ID, 'user-name')))

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.set_page_load_timeout(10)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.set_page_load_timeout(10)
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("620078")
    driver.find_element(By.ID, "continue").click()
    driver.set_page_load_timeout(10)
    rezu = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    assert rezu == "Total: $58.29", ("ошибка вычисления")

    driver.quit()
