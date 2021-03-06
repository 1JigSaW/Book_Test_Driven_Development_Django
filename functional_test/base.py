from selenium import webdriver
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest
import sys


class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                cls.live_server_url = ''
                cls.against_staging = True
                return
        super().setUpClass()
        cls.against_staging = False
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        # if cls.server_url == cls.live_server_url:
        #     super().tearDownClass()
        if not cls.against_staging:
            super().tearDownClass()

    def setUp(self):
        if self.against_staging:
            reset_database(self.server_host)
        self.browser = webdriver.Firefox(executable_path=r'e:\workspace\tdd_python\geckodriver.exe')
        self.browser.implicitly_wait(3)

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=3).until(
            lambda b: b.find_element_by_id(element_id),
            'Could not find element with id {}. Page text was {}'.format(element_id, self.browser.find_element_by_tag_name('body').text)
        )
        
    def wait_to_be_logged_in(self, email):
        self.wait_for_element_with_id('id_logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(email, navbar.text)

    def wait_to_be_logged_out(self, email):
        self.wait_for_element_with_id('id_login')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn(email, navbar.text)


    def tearDown(self):
        self.browser.quit()