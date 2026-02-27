from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = None


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver"
            "-java/slow-calculator.html"
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_delay(self):
        text_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        text_input.clear()
        text_input.send_keys("45")

    def enter_digits(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()
        WebDriverWait(self._driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
        )

    def get_result(self):
        WebDriverWait(self._driver, 60).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15")
                )
        res = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return (res)

    def close_driver(self):
        self._driver.quit()
