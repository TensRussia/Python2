from selenium import webdriver
from MainPageShop import MainShop
from CartPageShop import CartPage
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def test_shop():
    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    main_shop = MainShop(browser)
    main_shop.log_pass()
    main_shop.select()

    cart_shop = CartPage(browser)
    cart_shop.checkout()
    cart_shop.UserName()
    cart_shop.rezult()

    rezu = cart_shop.rezult()
    assert rezu == "Total: $58.29", ("ошибка вычисления")
    cart_shop.CloseDriver()
