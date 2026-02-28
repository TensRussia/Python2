from selenium import webdriver
from MainPageCalc import MainPage


def test_calculator():
    browser = webdriver.Chrome()
    browser.get(
            "https://bonigarcia.dev/selenium-webdriver"
            "-java/slow-calculator.html"
            )
    main_page = MainPage(browser)
    main_page.set_delay()
    main_page.enter_digits()
    main_page.get_result()

    res = main_page.get_result()
    assert res == "15"
    main_page.close_driver()
