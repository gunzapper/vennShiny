import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class NewVennDia(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.actionChains = ActionChains(self.browser)
        # - I need to wait sometime,      -
        # - otherwise the tests are break -
        self.browser.implicitly_wait(9)

    def tearDown(self):
        self.browser.quit()

    def looking_for_choices(self, res, element):
        """ This function tests the results of selcting venn diagram type"""
        choice_text = self.browser.find_element_by_id("choice").text
        self.assertEqual(choice_text, '[1] "{}"'.format(res))

        item = element.find_element_by_class_name("item")
        self.assertEqual(item.text, res)
        self.assertEqual(item.get_attribute("data-value"), res)

    def test_can_start_a_new_venn(self):
        # My work mate Valentina has heard about a new online
        # Venn's diagram application.
        # She goes to check out its home page
        self.browser.get('http://localhost:7606')

        # She notices the page title and header mention Venn's Diagram
        self.assertIn("Venn's", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn("Venn's", header_text)

        # By default the choice is "simple"
        self.typeselect = self.browser.find_element_by_class_name(
            "selectize-control"
        )

        self.looking_for_choices("simple", self.typeselect)

        # She is invited to choose the kind of venn's diagram.
        self.labels = self.browser.find_elements_by_tag_name("label")
        self.assertTrue(
            any(lab.text == "Choose a type of graph:" for lab in self.labels)
        )

        self.typeinput = self.typeselect.find_element_by_tag_name("input")
        self.typeinput.send_keys(Keys.ARROW_DOWN)
        self.typeinput.send_keys(Keys.ENTER)

        # She looks that the page update its text with the choice done
        self.looking_for_choices("proportional", self.typeselect)

        # Now she is invited to enter two or three excell files
        self.assertTrue(
            any(lab.text == "Choose a file" for lab in self.labels)
        )

        # Now she inserts a file
        self.choosefile1input = self.browser.find_element_by_id("file1")
        self.actionChains.context_click(self.choosefile1input).perform()

        # She looks that the page charges the data of first excell

        # of the second

        # She looks that the app shows a plot

        # she introduces the third excell

        # the page change with the new info

        # and updates the plots

        # at the end she close the browser
        self.fail('Finish the tests!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
