from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    '''Klasa testujaca witryne z poziomu uzytkownika'''

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_add_flight_data_to_see_chart(self):
        #User decide to check out app homepage
        self.browser.get('http://localhost:8000')

        #User notices the page title and header mention about frs
        self.assertIn('FRS', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Flight recorder simulator', header_text)

        #User is invited to enter a link do flight data
        inputbox = self.browser.find_element_by_id('id_url_data')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Insert address to flight logs from flightaware.com'
        )

        #Next user decide to add url into text box
        urlToPage = 'http://flightaware.com/live/flight/LOT3908/history/20160323/1110Z/EPKK/EPWA/tracklog'
        inputbox.send_keys(urlToPage)

        #And he hits 'Enter'
        inputbox.send_keys(Keys.ENTER)

        import time
        time.sleep(10)
        #After that on homepage user cab see first data of flight
        h2_info = self.browser.find_element_by_id('flight_info')
        info = 'Flight ✈ LOT3908 ✈ 23. III 2016 ✈ KRK / EPKK - WAW / EPWA'
        self.assertIn(info, h2_info.text)


if __name__=='__main__':
    unittest.main(warnings='ignore')