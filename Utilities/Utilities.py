from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.SearchPageLocators import *
from conftest import *

class Util:
    def find(self,element):
        if element.startswith('//'):
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
            find_element=driver.find_element(By.XPATH,element)
        else:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
            find_element=driver.find_element(By.CSS_SELECTOR, element)
        return find_element
    def click_on(self,element):
        self.find(element).click()

    def enter_data_in(self,element,data):
        self.find(element).send_keys(data)

    def wait_for(self,element):
        if element.startswith('//'):
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,element)))
        else:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,element)))


    def switch_tab_to(self, num):
        tabs = driver.window_handles
        driver.switch_to.window(tabs[num])

    def search_for(self,element,value):
        self.find(element).send_keys(value)
        self.find(element).send_keys(u'\ue007')

    def select_from_search_products(self,value):
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, search_products)))
        all_products=driver.find_elements(By.CSS_SELECTOR,search_products)
        all_products[value].click()

    def switch_to_frame(self):
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(cart_iframe))
        element=driver.find_element(By.CSS_SELECTOR,cart_iframe)
        driver.switch_to.frame(element)qa

    def switch_to_window(self):
        driver.switch_to.default_content()

    def wait_for_tab(self):
        WebDriverWait(driver,10).until(EC.number_of_windows_to_be(2))