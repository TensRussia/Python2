from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainShop:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.ID, 'user-name')))

    def log_pass(self):
        self._driver.find_element(
            By.ID, "user-name").send_keys("standard_user")
        self._driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self._driver.find_element(By.ID, "login-button").click()

    def select(self):
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()
        self._driver.find_element(By.ID, "shopping_cart_container").click()
