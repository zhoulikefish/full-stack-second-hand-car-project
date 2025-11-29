# Scrapy settings for Icauto project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import logging

BOT_NAME = 'Icauto'

SPIDER_MODULES = ['Icauto.spiders']
NEWSPIDER_MODULE = 'Icauto.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 ' \
             'Safari/537.36 Edg/114.0.1823.51 '

RETRY_ENABLED = True  # 启用重试组件
RETRY_HTTP_CODES = [302, 500, 502, 503, 504, 522, 524, 408, 404]  # 指定需要重试的HTTP响应状态码
DUPEFILTER_DEBUG = True

RETRY_ENABLE = True
RETRY_TIMES = 200
HTTPERROR_ALLOWED_CODES = [302, 500, 502, 503, 504, 522, 524, 408, 404] #当遇到403的时候爬虫脚本不退出

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# LOG_ENABLED = True
# LOG_FILE = 'scrapy.log'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2
OUTPUT_FILE = 'output'
OUTPUT_FORMAT = 'csv'

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'Icauto.middlewares.AutohomeSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html


DOWNLOADER_MIDDLEWARES = {
    'Icauto.middlewares.AutohomeDownloaderMiddleware': 543,
    'Icauto.middlewares.RandomUserAgentMiddleware': 200,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Icauto.pipelines.IcautoPipeline': 300,
    'Icauto.pipelines.ImgproPipeline': 299
}
# MONGODB 主机环回地址127.0.0.1
MONGODB_HOST = '127.0.0.1'
# 端口号，默认是27017
MONGODB_PORT = 27017
# 设置数据库名称
MONGODB_DBNAME = "Icauto"
# 存放本次数据的表名称
MONGODB_SHEETNAME = "Icauto"

