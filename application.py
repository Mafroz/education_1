import os
os.environ["PATH"] += os.pathsep + r'C:\Users\Администратор'
from selenium import webdriver


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://10.201.48.25:8080/inrights")

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_name("login").click()
        wd.find_element_by_name("login").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//a[@class='x-btn btn-login btn-radius-3 x-unselectable x-box-item x-btn-default-medium']and[@role='button']").click()
