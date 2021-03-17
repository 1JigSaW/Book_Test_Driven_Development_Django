from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
    '''test new visitor'''
    def setUp(self):
        '''install'''
        self.browser = webdriver.Firefox()

    def TearDown(self):
        '''dismantling'''
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        '''The confirmation row in list table'''
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        """docstring for test_can_start_a_list_and_retrieve_it_later"""
        self.browser.get(self.live_server_url)
        


        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')


        inputbox.send_keys(Keys.ENTER)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
 #       self.assertTrue(
 #           any(row.text == '1: Buy peackock feathers' for row in rows)#,
 #           "New to-do item did not appear in table -- it was %s" %\
 #               (table.text,),
 #       )

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')