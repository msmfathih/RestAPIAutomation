import time
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestAdminLogin():

    def test_setup(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.maximize_window()

    def test_login(self):
        driver.implicitly_wait(8)
        driver.get("https://web.zabehaty.com")
        time.sleep(10)
        page_title = driver.title
        expected_title = "Zabehaty"
        assert page_title == expected_title, f"Page title is incorrect. Expected: {expected_title}, Actual: {page_title}"

    def test_enter_credentials(self):
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/button[1]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/button[3]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/button[1]/span").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/button[4]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/div[1]/div/input").send_keys("556467370")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/div[2]/div/input").send_keys("123456")
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/button[3]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[3]/button").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/button").click()

    def test_search_chicken(self):
        driver.find_element(By.XPATH,"//img[@alt='Aqeeqa']").click()
        driver.find_element(By.XPATH, "//img[@alt='Zabehti Chicken']").click()
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(4)
        #driver.find_element(By.CSS_SELECTOR, "//*[local-name()='svg' and @width='27' and @height='27' "
                                             #"and @viewBox='0 0 27 27']").click()
        # time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div[1]/div[6]/div/div/textarea").send_keys("test")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div[2]/div/button").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Go to Cart']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Complete The Order']").click()

        # def wait_until_clickable(by, value, timeout=10):
        #     return WebDriverWait(driver, timeout).until(
        #         EC.element_to_be_clickable((by, value))
        #     )
        # element = wait_until_clickable(By.XPATH, "//button[normalize-space()='Complete The Order']")
        # element.click()

    def test_select_cart(self):
        driver.find_element(By.XPATH, "//span[@class='text-lg font-medium text-[rgba(38,38,38,1)]']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//body//div//div//div//div//div//div//div//div//div//button[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@class='transition hover:scale-110']//*[name()='svg']").click()
        time.sleep(3)
        # select_payment_method = driver.find_element(By.XPATH, "//button[@class='transition hover"
        #                                                       ":scale-110']//*[name()='svg']")
        # select_payment_method.click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@class='mt-20 flex items-center justify-center rounded-lg "
                                      "bg-primary px-6 py-[18px] text-center text-white transition hover:opacity-80']").click()








































