import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
os.environ["PATH"] += os.pathsep + r'C:\Users\m.zasetskii\Webdrivers'
from selenium import webdriver


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
        self.wd.get("http://10.201.48.25:8080/inrights")

    def login(self, username, password):
        while self.__if_element_clickable_by_name('login').get_attribute("value") != username:
            self.__if_element_clickable_by_name('login').click()
            self.__if_element_clickable_by_name('login').clear()
            self.__if_element_clickable_by_name('login').send_keys(username)
        self.__if_element_clickable_by_name('password').click()
        self.__if_element_clickable_by_name('password').send_keys(password)
        self.__if_element_clickable_by_xpath("//a[contains(@id, 'button')and contains(@role,'button') and contains(@class, 'x-btn btn-login btn-radius-3 x-unselectable x-box-item x-btn-default-medium')and contains(@aria-hidden, 'false')]").click()

    def navigate_to_submenu_element(self, elementid, submenu_title):
        menu_element_number = self.__menu_element_number
        if_element_clickable_by_xpath = self.__if_element_clickable_by_xpath

        menu_element_number(elementid).click()
        if_element_clickable_by_xpath('//a[.//*[contains(text(), "' + submenu_title + '")]]').click()

    def click_on_button_in_toolbar_by_id(self, index):
        wd = self.wd
        element = wd.find_elements_by_xpath("//a[contains(@class, 'x-btn x-unselectable x-box-item x-toolbar-item x-btn-default-toolbar-medium')]")
        element[index].click()

    def new_user_name(self):
        self.navigate_to_submenu_element(2, "Пользователи")
        element = self.wd.find_elements_by_xpath("//*[contains(@class,'x-column-header-text-inner')]")
        element[0].click()
        #time.sleep(1)
        self.__if_element_clickable_by_xpath("//tr[contains(@class,'x-grid-row')]").click()
        #print(self.wd.find_elements_by_xpath("//tr[contains(@class,'x-grid-row')]//a[contains(@class, 'click-link ')]")[0].get_attribute("text"))

    def __if_element_clickable_by_name(self, locator):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        element = wait.until(EC.element_to_be_clickable((By.NAME, locator)))
        return element

    def __if_element_clickable_by_xpath(self, locator):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        return element

    def __menu_element_number(self, index):
        wd = self.wd
        menu_element_user = wd.find_elements_by_xpath("//*[contains(@class,'app-menu')]//a")
        return menu_element_user[index]

    def destroy(self):
        wd = self.wd
        wd.quit()
