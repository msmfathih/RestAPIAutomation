import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from PageLocators.login_page_locators import LoginPageLocators
from TestData.OrderData import userCredentials,orderDetails
from PageLocators.dashboard_page_locators import DashboardPageLocators
from Configuration.conftest import init_driver


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestAdminLogin():

    def test_setup(self):
        global driver
        options = webdriver.ChromeOptions()   #not closing browser
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.maximize_window()

    def test_login(self):
        driver.implicitly_wait(8)
        driver.get(userCredentials["URL"])
        actual_title = driver.title
        expected_title = "test"
        assert actual_title == expected_title, f"Page title is not as expected. Actual: {actual_title}, Expected: {expected_title}"

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

    def test_navigate_sales(self):
        ack = ActionChains(driver)
        ack.move_to_element(driver.find_element(By.XPATH, DashboardPageLocators.MOUSEHOVER_SALES_XPATH)).perform()
        print("Clicked on interaction page")
        driver.find_element(By.XPATH, DashboardPageLocators.CLICK_ORDERS_XPATH).click()
        time.sleep(5)

    def test_select_order(self):
        driver.find_element(By.XPATH, DashboardPageLocators.CLICK_CHICKEN_XPATH).click()
        driver.find_element(By.XPATH, DashboardPageLocators.CLICK_CREATE_ORDER_XPATH).click() #create button for new order
        time.sleep(2)
        driver.find_element(By.XPATH, DashboardPageLocators.CLICK_SECTION_DROPDOWN_XPATH).click()
        time.sleep(2)
        # driver.find_element(By.XPATH, DashboardPageLocators.SEARCH_DROPDOWN_XPATH).send_keys(orderDetails["section"])
        # time.sleep(3)

    def test_create_chicken_order(self):
        click_section = driver.find_element(By.XPATH, DashboardPageLocators.CLICK_ON_SEARCHBOX_XPATH)
        click_section.send_keys(orderDetails["section"])
        time.sleep(3)
        click_section.send_keys(Keys.ENTER)
        time.sleep(2)

        # actions = ActionChains(driver)
        # actions.send_keys(keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
        # try:   #test still will pass
        #     elem = driver.find_element(By.CSS_SELECTOR, "#select2-category_id-06-container")
        #     elem.click()
        # except NoSuchElementException:
        #     pass
        selectShop = driver.find_element(By.NAME, DashboardPageLocators.CLICK_ON_SHOPDROPDOWN_NAME)
        sel = Select(selectShop)
        sel.select_by_visible_text("Zabehti Chicken")
        time.sleep(3)

        selectemirates = driver.find_element(By.NAME, DashboardPageLocators.EMIRATE_ID_NAME)  #emrates
        sel = Select(selectemirates)
        sel.select_by_visible_text("Abu Dhabi")
        time.sleep(5)

        selectregion = driver.find_element(By.NAME, DashboardPageLocators.REGION_NAME_NAME) #region
        sel = Select(selectregion)
        sel.select_by_index(5)
        time.sleep(3)

        driver.find_element(By.XPATH, DashboardPageLocators.SEARCH_USER_XPATH).send_keys(orderDetails["user"])
        time.sleep(3)
        driver.find_element(By.XPATH, DashboardPageLocators.CLICK_ON_NAMEDROPDOWN_XPATH).click()
        time.sleep(3)

        select_user_address = driver.find_element(By.NAME, DashboardPageLocators.ADDRESS_ID_NAME)
        sel = Select(select_user_address)
        sel.select_by_index(1)

        select_date = driver.find_element(By.CSS_SELECTOR, DashboardPageLocators.CLICK_ON_DATE_CSS)
        select_date.send_keys(orderDetails["date"])

        select_time = driver.find_element(By.NAME, "time")
        sel = Select(select_time)
        sel.select_by_index(3)

        select_payment_method = driver.find_element(By.NAME, DashboardPageLocators.PAYMENT_METHOD_NAME)
        sel = Select(select_payment_method)
        sel.select_by_visible_text("paylink")
        time.sleep(3)

        select_shipping_method = driver.find_element(By.NAME, DashboardPageLocators.SHIPPING_METHOD_NAME)
        sel = Select(select_shipping_method)
        sel.select_by_index(3)

        enter_additional_request = driver.find_element(By.CSS_SELECTOR, DashboardPageLocators.ENTER_ADDITIONAL_REQUEST_CSS)
        enter_additional_request.send_keys("test order")
        time.sleep(2)

    #@pytest.mark.skip(reason="no way of currently testing this")
    #@pytest.mark.xfail(run=False) make the TC fails
    def test_order_details(self):
        enter_category_details = driver.find_element(By.NAME, DashboardPageLocators.ENTER_CATOGORY_DETAILS_NAME)
        sel = Select(enter_category_details)
        sel.select_by_visible_text("chicken")
        time.sleep(3)

        select_product = driver.find_element(By.NAME, DashboardPageLocators.SELECT_PRODUCT_NAME)
        sel = Select(select_product)
        sel.select_by_visible_text("fresh chicken 1200g box")
        time.sleep(3)

        enter_quantity = driver.find_element(By.NAME, DashboardPageLocators.ENTER_QUANTITY_NAME)
        enter_quantity.send_keys("1")
        time.sleep(3)

        # submit_order = driver.find_element(By.NAME, DashboardPageLocators.SAVE_NAME)
        # submit_order.click()
