import allure
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, browser):
        """
        Конструктор класса CartPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = browser

    @allure.step("Нажать на кнопку 'Выполнить заказ/Checkout'")
    def checkout(self) -> None:
        """
        Находит и нажимает кнопку 'Checkout'
        """
        self._driver.find_element(By.ID, "checkout").click()

    @allure.step("Ввести данные покупателя")
    def full_user_data(self) -> None:
        """
        Вводит данные покупателя ('first-name', 'last-name', 'postal-code').
        Нажимает на кнопку 'Continue'
        """
        self._driver.find_element(By.ID, "first-name").send_keys("Иван")
        self._driver.find_element(By.ID, "last-name").send_keys("Иванов")
        self._driver.find_element(By.ID, "postal-code").send_keys("620078")
        self._driver.find_element(By.ID, "continue").click()

    @allure.step("Найти итоговую сумму")
    def get_rezult(self) -> str:
        """
        Находит и возваращает текст итоговой суммы
        """
        rezu = self._driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
        return (rezu)

    @allure.step("Закрыть сессию браузера")
    def close_driver(self):
        self._driver.quit()
