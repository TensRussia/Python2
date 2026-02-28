from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, browser):
        self._driver = browser

    def checkout(self):
        self._driver.find_element(By.ID, "checkout").click()

    def full_user_data(self):
        self._driver.find_element(By.ID, "first-name").send_keys("Иван")
        self._driver.find_element(By.ID, "last-name").send_keys("Иванов")
        self._driver.find_element(By.ID, "postal-code").send_keys("620078")
        self._driver.find_element(By.ID, "continue").click()

    def get_rezult(self):
        rezu = self._driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
        return (rezu)

    def close_driver(self):
        self._driver.quit()
