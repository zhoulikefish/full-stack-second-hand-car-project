# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# useful for handling different item types with a single interface

# ------------ 导入package -------------#
from scrapy import signals
import random
import time
import logging


# ------------ 配置中间件 -------------#
# 设置随机UA
class RandomUserAgentMiddleware:
    """
    RandomUserAgentMiddleware类用于随机获取UA
    """
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 "
            "Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 "
            "Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 "
            "Safari/535.24",
            "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 "
        ]

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)


# 设置随机延时
class RandomDelayMiddleware(object):
    """
    RandomUserAgentMiddleware类用于设置随机延时
    """
    def __init__(self, delay):
        self.delay = delay
    @classmethod
    def from_crawler(cls, crawler):
        delay = crawler.spider.settings.get("DOWNLOAD_DELAY", 2)  # setting里设置的时间，注释默认为1s
        if not isinstance(delay, int):
            raise ValueError("RANDOM_DELAY need a int")
        return cls(delay)

    def process_request(self, request, spider):
        # delay = random.randint(0, self.delay)
        delay = random.uniform(1, self.delay)
        delay = float("%.1f" % delay)
        logging.debug("### Time is random delay: %s s ###" % delay)
        time.sleep(delay)


# 设置随机私密代理IP1：手动获取
class ProxyMiddleWare(object):
    """
    ProxyMiddleWare类用于获取私密代理
    """
    def process_request(self, request, spider):
        '''对request对象加上proxy'''
        proxy = self.get_random_proxy()
        request.meta['proxy'] = proxy
        return None

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200,重新生成当前request对象
        if response.status != 200:
            proxy = self.get_random_proxy()
            print("更换代理IP……" )
            # 对当前request加上代理
            request.meta['proxy'] = proxy
            return request
        return response

    def get_random_proxy(self):
        """
        随机从文件中读取proxy
        """
        # 隧道域名:端口号
        tunnel = "m730.kdltps.com:15818"
        # 用户名密码方式
        username = "t18810078157698"
        password = "mi37k5cv"
        proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
            "https": "https://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
        }
        return proxies



# 设置隧道代理IP2：API获取
class ProxyDownloaderMiddleware:
    """
    ProxyDownloaderMiddleware类用于获取隧道代理
    """
    _proxy = ('e282.kdltps.com', '15818')

    def process_request(self, request, spider):

        # 用户名密码认证
        username = "t18819638161432"
        password = "nvhahssn"
        request.meta['proxy'] = "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": ':'.join(ProxyDownloaderMiddleware._proxy)}

        # 白名单认证
        # request.meta['proxy'] = "http://%(proxy)s/" % {"proxy": proxy}

        request.headers["Connection"] = "close"
        return None

    def process_exception(self, request, exception, spider):
        """捕获407异常"""
        if "'status': 407" in exception.__str__():  # 不同版本的exception的写法可能不一样，可以debug出当前版本的exception再修改条件
            from scrapy.resolver import dnscache
            dnscache.__delitem__(ProxyDownloaderMiddleware._proxy[0])  # 删除proxy host的dns缓存
        return exception



# 处理响应异常的请求
class FailedRequestsMiddleware:
    """
    FailedRequestsMiddleware类用于处理异常请求
    """
    def __init__(self):
        self.failed_requests_file = 'failed_requests.txt'  # 失败请求记录文件的路径
        current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())  # 获取当前时间，格式为年月日时分秒
        self.failed_requests_file = f'failed_requests_{current_time}.txt'  # 根据当前时间生成文件名

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        # 绑定 spider_closed 信号到 spider_closed 方法
        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def process_response(self, request, response, spider):
        if response.status > 300:  # 如果响应状态码大于300
            with open(self.failed_requests_file, 'a') as file:  # 打开失败请求记录文件
                file.write(f"Failed Request: {response.url}\n")  # 将失败请求的 URL 写入文件
        return response

    def spider_closed(self, spider):
        spider.logger.info(f"Failed requests have been written to {self.failed_requests_file}")  # 在日志中记录失败请求已被写入文件的消息

# 让爬虫程序处理异常后记录到日志里但继续运行
class IgnoreErrorsMiddleware:
    def process_spider_exception(self, response, exception, spider):
        spider.logger.error(f"An error occurred while processing {response.url}: {str(exception)}")  # 记录异常信息到日志中
        return None  # 返回 None，忽略异常，继续处理其他请求

# ------------ Scrapy默认中间件 -------------#
class AutohomeSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AutohomeDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
