import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
        
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
        
        #he types beer in the list
        inputbox.send_keys('Buy a Beer')

        #he presses Enter, page updates, 1. Buy a beer is reflected
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. Buy a Beer' for row in rows)
        )


        #there's still text inviting her to add more to-dos
        self.fail('Finish the test.')

if __name__ == '__main__':
    unittest.main()