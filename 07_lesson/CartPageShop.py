from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, browser):
        self._driver = browser

    def checkout(self):
        self._driver.find_element(By.ID, "checkout").click()

    def UserName(self):
        self._driver.find_element(By.ID, "first-name").send_keys("Иван")
        self._driver.find_element(By.ID, "last-name").send_keys("Иванов")
        self._driver.find_element(By.ID, "postal-code").send_keys("620078")
        self._driver.find_element(By.ID, "continue").click()
        self._driver.set_page_load_timeout(10)

    def rezult(self):
        rezu = self._driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
        return (rezu)

    def CloseDriver(self):
        self._driver.quit()
