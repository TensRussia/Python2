import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainShop:

    def __init__(self, driver):
        """
        Конструктор класса MainShop.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.ID, 'user-name')))

    @allure.step("Ввести логин, пароль, выполнить вход")
    def log_pass(self)  -> None:
        """
        Вводит данные в поля 'Логин' и 'Пароль'
        Нажимает кнопку 'Login'
        """
        self._driver.find_element(
            By.ID, "user-name").send_keys("standard_user")
        self._driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self._driver.find_element(By.ID, "login-button").click()

    @allure.step("Добавить товары и перейти в корзину")
    def select(self) -> None:
        """
        Добавляет три товара в корзину.
        Нажимает на кнопку 'Корзина для покупок'
        """
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()
        self._driver.find_element(By.ID, "shopping_cart_container").click()
