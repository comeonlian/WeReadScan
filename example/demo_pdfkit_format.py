#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2022/11/19 18:35
# @Author  : lianliang
# @File    : demo_pdfkit.py

import pdfkit

options = {
    'page-size': 'A4',
    'margin-top': '0.5in',
    'margin-bottom': '0.5in',
    'margin-right': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
}

save_path = 'E:/Java/Project/WeReadScan/example/Python量化投资：技术、模型与策略.html'

print('Save real path: ', save_path)
book_name = save_path[save_path.rfind('/') + 1:save_path.find('.html')]

print('Start convert html to pdf, book_name: ', book_name)
pdfkit.from_file(save_path, f'{book_name}.pdf', options=options)
