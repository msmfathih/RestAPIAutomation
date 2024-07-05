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
        driver.find_element(By.XPATH,"//img[@alt='Chicken']").click()
        driver.find_element(By.XPATH, "//img[@alt='Zabehti Chicken']").click()
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(4)
        #driver.find_element(By.CSS_SELECTOR, "//*[local-name()='svg' and @width='27' and @height='27' "
                                             #"and @viewBox='0 0 27 27']").click()
        time.sleep(3)
        # (driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div[1]/div[5]/div[2]/div/textarea")
        #  .send_keys("test"))
        # driver.find_element(By.XPATH, "//body//div//div//div//div//div//div//div//button[2]//*[name()='svg']").click()
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center"
        #                               " rounded-lg bg-primary py-[18px] text-white transition hover:opacity-80']").click()
        # time.sleep(3)
        # driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/button[2]").click() #click on go to card
        # time.sleep(3)

    # def test_continue_shopping(self):
    #     driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[2]/div/div[2]/a").click()
    #     time.sleep(3)
    #     driver.find_element(By.XPATH, "//img[@alt='Aqeeqa']").click()
    #     time.sleep(3)
    #     driver.find_element(By.XPATH, "//img[@alt='Naemi Sheep']").click()
    #     time.sleep(3)
    #     driver.find_element(By.XPATH, "//div[2]//div[1]//div[1]//div[2]//button[1]//*[name()='svg']").click()
    #     select_cutting = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div[1]/div[5]/div"
    #                                                    "[3]/div/div/div/div[2]/button/div/div/img")
    #     select_cutting.click()
    #     select_packaging = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div[1]/div[5]/div[4]"
    #                                                      "/div/div/div/div[2]/button/div/div/img")
    #     select_packaging.click()
    #     add_special_instruction = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]"
    #                                                             "/div[1]/div[5]/div[5]/div/textarea")
    #     add_special_instruction.send_keys("Test instructions")
    #     driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div[2]/div/button").click()
    #     go_to_cart = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/button[2]")
    #     go_to_cart.click()
    #     time.sleep(3)
    #     complete_order = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div[2]/div/button")
    #     complete_order.click()


    # def test_delivery_method(self):
    #     driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div/div/div[1]/div[1]/button/div").click()
    #     time.sleep(3)
    #     driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div/div/div[1]/div[1]"
    #                                   "/div[4]/div/div/div[3]/button").click()

    # def test_payment_method(self):
    #     choose_cash_on_delivery = driver.find_element(By.CSS_SELECTOR, "#root > div.flex.min-h-screen.flex-col > div.flex-1 > div >"
    #                                          " div > div:nth-child(2) > div:nth-child(1) > div > "
    #                                          "div:nth-child(1) > button > svg")
    #     choose_cash_on_delivery.click()















































