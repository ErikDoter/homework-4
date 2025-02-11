from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class FilmPage(Page):
    PATH = '/film/2'
    ADD_BUTTON = '//button[@id="adding"]'
    NOTIFICATION_SUCCESS = '//div[@class="name__notificationSuccess--2LyUD"]'
    NOTIFICATION_EXIST = '//div[@class="name__notificationFail--15d1Q"]'
    NOTIFICATION = '//span[@id="notification"]'
    STAR = '//label[@for="star-5"]'
    SELECT = '//select'
    RATE = '//button[text()="Оценить"]'
    COMMENT_AREA = '//textarea[@id="msg"]'
    SUBMIT_COMMENT = '//button[@id="msg_button"]'
    COMMENTS_NAME = '//a[@class="name__comment__login--3E4k1"]'
    COMMENTS_BODY = '//div[@class="name__comment__content--3-Ipy"]'
    COMMENT = '//div[@class ="name__comments__underground--Zy1hx"]'
    ERROR_EMPTY = '//div[@class="name__error--FQ9hR"]'

    def select_playlist(self, playlist):
        select = Select(self.driver.find_element_by_xpath(self.SELECT))
        select.select_by_visible_text(playlist)

    def submit_to_add_in_playlist(self):
        self.driver.find_element_by_xpath(self.ADD_BUTTON).click()

    def add_film_in_playlist(self, playlist):
        self.open()
        self.select_playlist(playlist)
        self.submit_to_add_in_playlist()
        self.driver.find_element_by_xpath(self.NOTIFICATION)
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, self.NOTIFICATION)))

    def select_star(self):
        self.driver.find_element_by_xpath(self.STAR).click()

    def submit_star(self):
        self.driver.find_element_by_xpath(self.RATE).click()

    def get_notification_text(self):
        return self.driver.find_element_by_xpath(self.NOTIFICATION).text

    def set_comment(self, comment):
        self.driver.find_element_by_xpath(self.COMMENT_AREA).send_keys(comment)

    def submit_comment(self):
        self.driver.find_element_by_xpath(self.SUBMIT_COMMENT).click()

    def wait_comment(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.COMMENTS_NAME)))

    def get_last_comment(self):
        return self.driver.find_elements_by_xpath(self.COMMENTS_BODY)[-1].text

    def get_last_comment_author(self):
        return self.driver.find_elements_by_xpath(self.COMMENTS_NAME)[-1].text

    def get_count_comments(self):
        self.wait_comment()
        try:
            elements = self.driver.find_elements_by_xpath(self.COMMENTS_NAME)
            n = len(elements)
        except NoSuchElementException:
            return 0
        else:
            return n
