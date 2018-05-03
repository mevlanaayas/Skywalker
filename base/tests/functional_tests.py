"""
What I call functional tests, some people prefer to call acceptance tests, or end-to-end
tests. The main point is that these kinds of tests look at how the whole application func‐
tions, from the outside. Another term is black box test, because the test doesn’t know
anything about the internals of the system under test.
"""

from selenium import webdriver
import unittest


class BlackBoxTest(unittest.TestCase):

    def setUp(self):
        # get ready for browsing
        # user opens web browser. firefox in this case
        self.browser = webdriver.Firefox()

    def tearDown(self):
        # The only exception is if you have an exception inside setUp, then tearDown does not run
        # clean up ashes
        # user is bored. time to go out
        self.browser.quit()

    def test_page_title_loaded_correctly(self):
        # actions
        # go into our good looking web application
        self.browser.get(url="http://127.0.0.1:8001/")

        assert 'Page not found at /' in self.browser.title, "Browser title was >>" + self.browser.title + "<<"


if __name__ == '__main__':
    unittest.main(warnings='ignore')
