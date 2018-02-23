from selenium import webdriver

browser = webdriver.Firefox()
browser.get(url="http://127.0.0.1:8000/")

assert 'Page not found at /' in browser.title
