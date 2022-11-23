#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2022/11/19 18:35
# @Author  : lianliang
# @File    : demo_pdfkit.py
import pdfkit

options = {
    'encoding': "UTF-8",
    'print-media-type': ''
}

# config = pdfkit.configuration(wkhtmltopdf='E:/Python/PyTool/wkhtmltopdf/')
# pdfkit.from_url('https://www.baidu.com', 'baidu.pdf')

pdfkit.from_file('D:/Java/Project/WeReadScan/example/Python量化交易.html',
                 'Python量化交易.pdf',
                 options=options,
                 css='print_pdf.css')
