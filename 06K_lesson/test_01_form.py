import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    edge_driver_path = r"C:\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
    driver.set_page_load_timeout(10)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.NAME, 'first-name')))

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    WebDriverWait(driver, 10)

    z_c_field = driver.find_element(By.ID, "zip-code")
    assert "danger" in z_c_field.get_attribute("class"), "Zip-code not red"

    f_n_field = driver.find_element(By.ID, "first-name")
    assert "success" in f_n_field.get_attribute("class"), "F-name not green"

    l_n_field = driver.find_element(By.ID, "last-name")
    assert "success" in l_n_field.get_attribute("class"), "L-name not green"

    a_field = driver.find_element(By.ID, "address")
    assert "success" in a_field.get_attribute("class"), "Address not  green"

    e_mail_field = driver.find_element(By.ID, "e-mail")
    assert "success" in e_mail_field.get_attribute("class"), "e-mail not green"

    phone_field = driver.find_element(By.ID, "phone")
    assert "success" in phone_field.get_attribute("class"), "Phone not green"

    city_field = driver.find_element(By.ID, "city")
    assert "success" in city_field.get_attribute("class"), "City not green"

    c_field = driver.find_element(By.ID, "country")
    assert "success" in c_field.get_attribute("class"), "Country not green"

    j_p_field = driver.find_element(By.ID, "job-position")
    assert "success" in j_p_field.get_attribute("class"), "J-pos not green"

    co_field = driver.find_element(By.ID, "company")
    assert "success" in co_field.get_attribute("class"), "Company not green"

    driver.quit()
