from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:3698')

assert "Venn's" in browser.title
