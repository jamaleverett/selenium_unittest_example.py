import unittest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_search_in_python_org(self):
        browser = self.browser
        browser.get("https://python.org")
        self.assertIn("Python", browser.title)
        elem = browser.find_element_by_name("q")
        elem.send_keys("getting started with python")
        elem.send_keys(Keys.RETURN)
        assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == browser.current_url

    def tearDown(self):
        self.browser.close()

    if __name__ == "__main__":
        unittest.main()
