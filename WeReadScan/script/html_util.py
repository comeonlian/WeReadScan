#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @FileName  : html_util.py
# @Time      : 2022/11/22 19:21
# @Author    : liang.lian

from bs4 import BeautifulSoup

html_content = '''
<p data-wr-co="813" class="right-info"><span data-wr-id="layout" data-wr-co="835">陈</span><span data-wr-id="layout" data-wr-co="836">晓</span><span data-wr-id="layout" data-wr-co="837">优</span><span data-wr-id="layout" data-wr-co="838">v</span><span data-wr-id="layout" data-wr-co="839">n</span><span data-wr-id="layout" data-wr-co="840">.</span><span data-wr-id="layout" data-wr-co="841">p</span><span data-wr-id="layout" data-wr-co="842">y</span><span data-wr-id="layout" data-wr-co="843">作</span><span data-wr-id="layout" data-wr-co="844">者</span></p>
'''.strip()

soup = BeautifulSoup(html_content, 'html.parser')
print('----- 处理前 -----')
print(soup)

print('----- 删除 -----')
content_div = soup.select('span')
for content in content_div:
    print(content.get_text())
    

print('----- 处理后 -----')
print(soup)