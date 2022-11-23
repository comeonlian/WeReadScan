# -*- coding: utf-8 -*-

"""
demo.py
The demo of WeReadScan.py
Copyright 2020 by Algebra-FUN
ALL RIGHTS RESERVED.
"""

from selenium.webdriver import Chrome, ChromeOptions

from WeReadScan import WeRead

# options
chrome_options = ChromeOptions()

# now you can choose headless or not
chrome_options.add_argument('--headless')

chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('log-level=3')

# launch Webdriver
print('Webdriver launching...')
driver = Chrome(options=chrome_options)
print('Webdriver launched.')

with WeRead(driver) as weread:
    weread.login()  # ? login for grab the whole book
    # weread.scan2html('https://weread.qq.com/web/reader/2c632ef071a486a92c60226kc81322c012c81e728d9d180')
    weread.scan2html('https://weread.qq.com/web/reader/c6332ff07191463ac6344e4kecc32f3013eccbc87e4b62e')
    # weread.scan2html2pdf('量化交易之路：用Python做股票量化分析',
    #                     'https://weread.qq.com/web/reader/97c320a05e4e5c97c71df82kecc32f3013eccbc87e4b62e')
