#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @FileName  : html_util.py
# @Time      : 2022/11/22 19:21
# @Author    : liang.lian
import re

pat = re.compile(r'<span data-wr-id="layout" data-wr-co="(\d+)">')


def my_read_lines(file, newline):
    '''
	f 文件对象
	newline 分隔符
	'''
    buf = ""
    while True:
        while newline in buf:  # 读取的内容包含了 分隔符
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]  # yield出去的数据 要从buf中删除
        chunk = file.read(4096)  # 每次读取4096长度的数据

        # 边界条件处理，当读取不到内容的时候，表示文件已经全部读完了
        if not chunk:
            yield buf
            break

        # 将每次读取的内容拼接到 buf字符串中
        buf = buf + chunk


def format_html(from_path, save_path):
    with open(from_path, 'r', encoding='utf-8') as f1, open(save_path, 'w', encoding='utf-8') as f2:
        for line in my_read_lines(f1, '\n'):
            result = pat.sub(r'', line).replace('</span>', r'')
            f2.write(result)
            f2.write('\r\n')
