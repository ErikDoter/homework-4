import os

import unittest
from selenium import webdriver
import urllib.parse as urlparse
import time

from Pages.auth_page import AuthPage
from Pages.settings_page import SettingPage


class SettingsTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_change_password(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        setting_page = SettingPage(self.driver)
        setting_page.open()
        time.sleep(10)
