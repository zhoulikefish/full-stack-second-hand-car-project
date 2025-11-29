# -*- coding: utf-8 -*-
# @Time    : 2023/6/21 1:07
# @Author  : Zhang Shiqing
# @File    : start.py
# @Software: PyCharm

# ------------ 导入package -------------#
from scrapy import cmdline

# ------------ 运行爬虫程序 -------------#
# 使用 cmdline.execute() 方法执行命令行命令: 'scrapy crawl AutoHome'
# 开始爬虫
cmdline.execute('scrapy crawl AutoHome'.split())

