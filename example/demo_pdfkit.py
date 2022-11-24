#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2022/11/19 18:35
# @Author  : lianliang
# @File    : demo_pdfkit.py
import os

import pdfkit

from WeReadScan.script.html_util import format_html

options = {
    'page-size': 'A4',
    'margin-top': '0.5in',
    'margin-bottom': '0.5in',
    'margin-right': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
}

save_path = 'E:/Java/Project/WeReadScan/example/Python量化交易实战_1.html'
save_path_real = save_path.replace('_1', r'')

print('Save real path: ', save_path_real)
format_html(save_path, save_path_real)

os.remove(save_path)

book_name = save_path_real[save_path_real.rfind('/') + 1:save_path_real.find('.html')]

print('Start convert html to pdf, book_name: ', book_name)
pdfkit.from_file(save_path_real, f'{book_name}.pdf', options=options)
