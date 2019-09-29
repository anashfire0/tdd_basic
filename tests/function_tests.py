import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_a_list(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    def insert_a_to_do_item(self, to_do_text):
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(to_do_text)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)


        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Basava goes to the url of the website
        self.browser.get('http://localhost:8000')

        #Basava notices page title and headers of the main page
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To Do', header_text)
    
        #He sees a placeholder
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual('Enter a to-do item', 
                        inputbox.get_attribute('placeholder')
                        )
        
        #he enters 1st to do item
        self.insert_a_to_do_item('Buy a Beer')
        #he enters 2nd to do item
        self.insert_a_to_do_item('Buy a Peacock')
        
        #he sees the 1st table field
        self.check_for_row_in_a_list('1. Buy a Beer')
        #he sees the 2nd table field
        self.check_for_row_in_a_list('2. Buy a Peacock')



        #there's still text inviting her to add more to-dos
        self.fail('Finish the test.')

if __name__ == '__main__':
    unittest.main()