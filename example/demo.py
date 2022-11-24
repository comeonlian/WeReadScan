# -*- coding: utf-8 -*-

"""
demo.py
The demo of WeReadScan.py
Copyright 2020 by Algebra-FUN
ALL RIGHTS RESERVED.
"""

from selenium.webdriver import Chrome, ChromeOptions

from WeReadScan import WeRead

if __name__ == '__main__':
    pdfkit_options = {
        'page-size': 'A4',
        'margin-top': '0.5in',
        'margin-bottom': '0.5in',
        'margin-right': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
    }
    
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
    
    book_name = 'Python量化交易实战'
    with WeRead(driver) as weread:
        weread.login()  # ? login for grab the whole book
        # weread.scan2html('https://weread.qq.com/web/reader/2c632ef071a486a92c60226kc81322c012c81e728d9d180')
        save_path = weread.scan2html(book_url='https://weread.qq.com/web/reader/821327f0813ab6ea4g0167afkecc32f3013eccbc87e4b62e',
                                     book_name=book_name+'_1', 
                                     show_output=False)

    print('Download html file finish.', save_path)

    