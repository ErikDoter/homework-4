from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class AuthPage(Page):
    USERNAME_INPUT = os.environ['LOGIN']
    PASSWORD_INPUT = os.environ['PASSWORD']
    PATH = '/login'
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//button[@class="name__button--2Ten8 name__buttons__marginForFilmCard--29k8-"]'
    ICON = '//img[@class="name__round--21Oxj"]'
    LOGOUT = '//button[text()="Выйти"]'
    ENTRY = '//button[text()="Войти"]'
    ERROR_MSG = '//div[@class="name__error--FQ9hR"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.LOGOUT).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.ENTRY)))


    def auth(self):
        self.open()
        self.set_login(self.USERNAME_INPUT)
        self.set_password(self.PASSWORD_INPUT)
        self.submit()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.ICON)))

    def auth_wrong(self, login, password):
        self.open()
        self.set_login(login)
        self.set_password(password)
        self.submit()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.ERROR_MSG)))