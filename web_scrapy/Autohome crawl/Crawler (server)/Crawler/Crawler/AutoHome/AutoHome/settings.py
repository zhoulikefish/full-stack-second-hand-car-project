# Scrapy settings for AutoHome project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


# ------------ 导入package -------------#
import logging

# ------------ 项目设置 -------------#
BOT_NAME = 'AutoHome'
SPIDER_MODULES = ['AutoHome.spiders']
NEWSPIDER_MODULE = 'AutoHome.spiders'

# User-agent设置
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 ' \
             'Safari/537.36 Edg/114.0.1823.51 '

# Retry、异常码设置
RETRY_ENABLE = True
DUPEFILTER_DEBUG = True
RETRY_TIMES = 200
HTTPERROR_ALLOWED_CODES = [302, 500, 502, 503, 504, 522, 524, 408, 404] #当遇到403的时候爬虫脚本不退出

# 不遵守 robots.txt
ROBOTSTXT_OBEY = False

# 日志单独输出进入Log文件
LOG_ENABLED = True
# LOG_FILE = 'scrapy.log'

# 配置Scrapy执行的最大并发请求数（默认：16）
CONCURRENT_REQUESTS = 5

# 禁用cookies（默认启用）
COOKIES_ENABLED = False

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# 爬取中间件配置
SPIDER_MIDDLEWARES = {
    'AutoHome.middlewares.AutohomeSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# 下载中间件配置
DOWNLOADER_MIDDLEWARES = {
    'AutoHome.middlewares.AutohomeDownloaderMiddleware': 543,
    'AutoHome.middlewares.RandomUserAgentMiddleware': 200,
    'AutoHome.middlewares.ProxyDownloaderMiddleware': 100,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# Pipeline中间件、MongoDB接口配置
ITEM_PIPELINES = {
    'AutoHome.pipelines.AutohomePipeline': 300
}
# MONGODB 主机环回地址127.0.0.1
MONGODB_HOST = '127.0.0.1'
# 端口号，默认是27017
MONGODB_PORT = 27017
# 设置数据库名称
MONGODB_DBNAME = "AutoHome"
# 存放本次数据的表名称
MONGODB_SHEETNAME = "AutoHomeCarItem_0708"

# ------------ Scrapy自带默认配置 -------------#
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16



# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#     #'AutoHome.myextend.MyExtend': 300,
#     #'scrapy.extensions.corestats.CoreStats': None,
#     #'AutoHome.extensions.corestats.MyCoreStats': 500,
# }
