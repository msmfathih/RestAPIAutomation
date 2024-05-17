import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from PageLocators.login_page_locators import LoginPageLocators
from TestData.OrderData import userCredentials,orderDetails
from PageLocators.dashboard_page_locators import DashboardPageLocators
from selenium.webdriver import ActionChains
from PageLocators.appointment_locators import appointmentLocators
from Configuration.conftest import init_driver


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestAdminLogin():

    def test_setup(self):
        global driver
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        # driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.maximize_window()

    @pytest.mark.run(order=5)
    def test_login(self):
        driver.implicitly_wait(8)
        driver.get(userCredentials["URL"])
        title = driver.title
        print(title)

    @pytest.mark.run(order=6)
    def test_enter_credentials(self):
        enter_username = driver.find_element(By.NAME, LoginPageLocators.USERNAME_NAME)
        enter_username.send_keys(userCredentials["username"])
        enter_password = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_XPATH)
        enter_password.send_keys(userCredentials["password"])
        click_login_btn = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON_XPATH)
        click_login_btn.click()
        time.sleep(3)
        driver.find_element(By.XPATH, DashboardPageLocators.LANGUAGE_DROPDOWN_XPATH).click()
        driver.find_element(By.XPATH, DashboardPageLocators.SELECT_ENGLISH_XPATH).click()

        ack = ActionChains(driver)
        ack.move_to_element(driver.find_element(By.XPATH, appointmentLocators.MOUSEHOVER_MANAGEMENT_XPATH)).perform()
        driver.find_element(By.XPATH, appointmentLocators.SECTION_SELECTION_XPATH).click()
        time.sleep(5)

        select_personal_button = driver.find_element(By.XPATH, appointmentLocators.CHOOSE_PERSONAL_XPATH)
        select_personal_button.click()

        click_preparation_date = driver.find_element(By.XPATH, appointmentLocators.SELECT_PREPARATION_DATE_XPATH)
        click_preparation_date.click()

    @pytest.mark.run(order=7)
    def test_create_special_appointment(self):
        click_special_appointment = driver.find_element(By.XPATH, appointmentLocators.SPECIAL_APPOINTMENT_XPATH)
        click_special_appointment.click()
        click_special_appointment = driver.find_element(By.NAME, appointmentLocators.EXPRESS_SHIPPING_NAME)
        click_special_appointment.click()

        choose_from_time = driver.find_element(By.NAME, "delivery_times[times][0][from]")
        choose_from_time.send_keys("04:25:PM")
        # choose_to_time = driver.find_element(By.NAME, appointmentLocators.TO_TIME_XPATH)
        # choose_to_time.send_keys("04:25:PM")

        element = driver.find_element(By.XPATH, "//input[@name='delivery_times")
        driver.execute_script("arguments[0].click();", element)







