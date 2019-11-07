import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
os.environ["PATH"] += os.pathsep + r'C:\Users\Администратор'
from selenium import webdriver


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
        self.wd.get("http://10.201.48.25:8080/inrights")


    def login(self, username, password):
        self.if_element_clickable_by_name('login').click()
        self.if_element_clickable_by_name('login').send_keys(username)
        self.if_element_clickable_by_name('password').click()
        self.if_element_clickable_by_name('password').send_keys(password)
        self.if_element_clickable_by_xpath("//a[contains(@id, 'button')and contains(@role,'button') and contains(@class, 'x-btn btn-login btn-radius-3 x-unselectable x-box-item x-btn-default-medium')and contains(@aria-hidden, 'false')]").click()

    def open_users_page(self):
        wd = self.wd
        menu_element_number = self.menu_element_number
        if_element_clickable_by_xpath = self.if_element_clickable_by_xpath
        actions = ActionChains(wd)

        menu_element_number(2).click()
        if_element_clickable_by_xpath('//a[.//*[contains(text(), "Пользователи")]]').click()
        if_element_clickable_by_xpath('//a[./asdext(), "Пользователи")]]').click()


    def if_element_clickable_by_name(self, locator):
        wd = self.wd
        wait = WebDriverWait(wd, 5)
        element = wait.until(EC.element_to_be_clickable((By.NAME, locator)))
        return element

    def if_element_clickable_by_xpath(self, locator):
        wd = self.wd
        wait = WebDriverWait(wd, 5)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        return element

    def menu_element_number(self, index):
        wd = self.wd
        menu_element_user = wd.find_elements_by_xpath("//*[contains(@class,'app-menu')]//a")
        return menu_element_user[index]

    def destroy(self):
        wd = self.wd
        wd.quit()