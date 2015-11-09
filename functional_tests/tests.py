from selenium import webdriver

browser = webdriver.Firefox()

# My work mate Valentina has heard about a new online
# Venn's diagram application.
# She goes to check out its home page
browser.get('http://localhost:3698')

# She notices the page title and header mention Venn's Diagram
assert "Venn's" in browser.title

# She is invited to choose the kind of venn's diagram.

# She looks that the page update its text with the choice done

# Now she is invited to enter two or three excell files

# She looks that the page charges the data of first excell

# of the second

# She looks that the app shows a plot

# she introduces the third excell

# the page change with the new info

# and updates the plots
