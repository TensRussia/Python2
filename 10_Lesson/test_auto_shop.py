import allure
from selenium import webdriver
from MainPageShop import MainShop
from CartPageShop import CartPage
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@allure.id("SKYPRO-1")
@allure.story("Тест магазина. Общая стоимость товара")
@allure.epic("Магазин")
@allure.feature("Functional")
@allure.title("Сравнение суммы заказа с заявленной")
@allure.description(
    "Наполнение корзины товарами и получение итоговой стоимости"
    )
@allure.severity("critical")
def test_shop_o():
    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    with allure.step("Перейти на страницу регистрации"):
        browser.get("https://www.saucedemo.com/")
        main_shop = MainShop(browser)
    main_shop.log_pass()
    main_shop.select()
    cart_shop = CartPage(browser)
    cart_shop.checkout()
    cart_shop.full_user_data()
    with allure.step("Cохранить итоговую сумму"):
        rezu = cart_shop.get_rezult()
    with allure.step("Сравнить итоговую сумму с указанной"):
        assert rezu == "Total: $58.29", ("ошибка вычисления")
    cart_shop.close_driver()
