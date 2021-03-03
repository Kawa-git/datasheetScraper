import sys
from selenium import webdriver

url = 'https://www.alldatasheet.com/'
browser = webdriver.Chrome()

button = '//*[@id="frmSubmit"]'

browser.get(url)

browser.find_element_by_xpath('//*[@id="sSearchword"]').send_keys(sys.argv[1])
browser.find_element_by_xpath(button).click()
browser.find_element_by_xpath('//*[@id="cell10"]/td[2]/a').click()