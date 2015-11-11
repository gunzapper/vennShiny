from selenium import webdriver
import unittest

class NewVennDia(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_new_venn(self):
        # My work mate Valentina has heard about a new online
        # Venn's diagram application.
        # She goes to check out its home page
        self.browser.get('http://localhost:7606')

        # She notices the page title and header mention Venn's Diagram
        self.assertIn("Venn's", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn("Venn's", header_text)
        self.fail('Finish the tests!')

        # She is invited to choose the kind of venn's diagram.

        # She looks that the page update its text with the choice done

        # Now she is invited to enter two or three excell files

        # She looks that the page charges the data of first excell

        # of the second

        # She looks that the app shows a plot

        # she introduces the third excell

        # the page change with the new info

        # and updates the plots

        # at the end she close the browser

if __name__ == '__main__':
    unittest.main(warnings='ignore')
