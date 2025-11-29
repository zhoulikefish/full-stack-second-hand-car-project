import random
import time
from urllib.request import Request
import requests
import scrapy
from scrapy.downloadermiddlewares.retry import get_retry_request
import pandas as pd
from ..items import IcautoItem
from bs4 import BeautifulSoup
import numpy as np

# def find_max_page(prefix, suffix, proxies):
#     # self.max_page = int(response.xpath('//div[@class="page fn-clear"]/a[position()=last()-1]/text()').extract()[0])
#     # return None
#     first_page_response = requests.get(prefix + '1' + suffix, headers={
#         'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/"
#                       "20.0.1092.0 Safari/536.6"}, proxies=proxies)
#     base_data = first_page_response.content
#     soup = BeautifulSoup(base_data, 'lxml')
#     # last_page_link = soup.select_one('div.page.fn-clear a:nth-last-child(2)')
#     div = soup.find('div', class_='page fn-clear')
#     if div is None:
#         return None
#     a = div.find_all('a')[-2]
#     if a is None:
#         return None
#     max_page = a.text
#     if max_page is None:
#         return None
#     max_page = int(max_page)
#     return max_page




class AutoHomeSpider(scrapy.Spider):
    # 初始属性
    name = 'Icauto'  # 项目名称
    allowed_domains = ['icauto.com.cn']  # 可以爬取的域名
    base_url = 'https://www.icauto.com.cn/usedcar/s876/'  # 初始链接
    # TODO 收集所有的地点加入city_list改写成
    # price_field = ['0-3', '3-5', '5-8', '8-10', '10-15', '15-20', '20-30', '30-50', '50-100', '100-0']
    # city_list = pd.read_csv('./spiders/city.csv')['city_url']
    # start_time = None
    # prefixes = []
    # for city in city_list:
    #     for price in price_field:
    #         prefixes.append('https://www.che168.com{}{}/a0_0msdgscncgpi1ltocsp'.format(city, price))
    # prefix = ['https://www.che168.com/{}/a0_0msdgscncgpi1ltocsp'.format(i) for i in city_list]
    # prefix = 'https://www.che168.com/china/a0_0msdgscncgpi1ltocsp'
    # suffix = 'exx0/'
    # start_urls = []
    # start_urls = ['https://www.che168.com/china/a0_0msdgscncgpi1ltocsp{}exx0/?pvareaid=102179'.format(i) for i in
    #              range(1, 101)]
    # base_url = 'https://www.che168.com/china/a0_0msdgscncgpi1ltocsp'  # 后续链接
    # page = 1  # 页数
    #max_page = 1  # 最大页数


    # second_url_list = []

    # 启动请求：start_urls的网页
    def start_requests(self):
        # 返回一个迭代器：每迭代一次都会request一个新连接并返回一个response
        print('*******************************')
        print('************ 爬虫启动 ***********')
        print('*******************************')
        yield scrapy.Request(self.base_url, callback=self.parse, errback=self.errback_parse, priority=1)
    # def parse(self, response):
        # self.max_page = int(response.xpath('//div[@class="page fn-clear"]/a[position()=last()-1]/text()').extract()[0])
        # return None
        # 解析第一页
        # self.start_urls = [response.meta['prefix'] + '{}'.format(i) + 'exx0/' for i in range(1, max_page)]

            # print('最大页数:', max_page)

    # def get_max_page(self, response):
    #     # 在这里编写解析网页内容，获取最大页数的逻辑
    #     # 假设最大页数在网页中的某个标签中，使用 XPath 提取
    #     page_list = response.xpath('//div[@class="page fn-clear"]/a[position()=last()-1]/text()').extract()
    #     if len(page_list) != 0:
    #         max_page = int(page_list[0])
    #         return max_page
    #     else:
    #         return None
    # 解析response中一级链接的页面，获取二级链接
    def parse(self, response):
        # 获取所有侧边栏的链接
        next_page_urls =response.xpath('//div[@class="carleftP2"]/ul/li/a/@href').extract()
        next_page_text = response.xpath('//div[@class="carleftP2"]/ul/li/a/text()').extract()
        if len(next_page_urls) != 0 and len(next_page_text) != 0:
            for second_url, car_name in zip(next_page_urls, next_page_text):
                second_url = 'https://www.icauto.com.cn' + second_url
                car_name = car_name.strip()
                yield scrapy.Request(url=second_url, callback=self.sec_handler, errback=self.errback_parse,
                                     meta={'car_name': car_name})

    def errback_parse(self, fail):
        new_request = Request(url=fail.request.url, method="GET")
        new_request_or_none = get_retry_request(
            new_request,
            spider=self,
            reason='retry',
        )
        return new_request_or_none

    def sec_handler(self, response):
        # TODO:处理二级链接
        car_name = response.meta['car_name']
        car_img = ''
        if len(response.xpath('//div[@class="logoimdg"]/img/@src').extract()) != 0:
            car_img = response.xpath('//div[@class="logoimdg"]/img/@src').extract()[0]
        # 获取内容
        if len(response.xpath('//div[@class="carlistP2 bzl"]/table/tr').extract()) != 0:
            #tr_list = response.xpath('//div[@class="carlistP2 bzl"]/table/tr')
            td_list = response.xpath('//div[@class="carlistP2 bzl"]/table/tr/td/text()').extract()
            dd_list = ['']
            a_list = [''] * 3
            if len(response.xpath('//div[@class="carInfo"]/dd/text()').extract()) != 0:
                dd_list = response.xpath('//div[@class="carInfo"]/dd/text()').extract()

            if len(response.xpath('//div[@class="carInfo"]/dd/a/text()').extract()) != 0:
                a_list = response.xpath('//div[@class="carInfo"]/dd/a/text()').extract()
            for i in np.arange(0, len(td_list), 6):
                i = int(i)
                icauto_item = IcautoItem()
                icauto_item['car_name'] = car_name
                icauto_item['car_img'] = car_img
                icauto_item['city_name'] = td_list[i]
                icauto_item['price_field'] = dd_list[0].strip().replace('万元', '').strip()
                icauto_item['model'] = a_list[2].strip()
                icauto_item['year1'] = td_list[i + 1]
                icauto_item['year2'] = td_list[i + 2]
                icauto_item['year3'] = td_list[i + 3]
                icauto_item['year4'] = td_list[i + 4]
                icauto_item['year5'] = td_list[i + 5]
                yield icauto_item
            # for tr in tr_list:
            #     td_list = response.xpath('//div[@class="carlistP2 bzl"]/table/tr/td/text()').extract()
            #     icauto_item = IcautoItem()
            #     for td in td_list:
            #         if td_list.index(td) == 0:
            #             icauto_item['car_name'] = car_name
            #             icauto_item['city_name'] = td
            #             dd_list = response.xpath('//div[@class="carInfo"]/dd/text()').extract()
            #             icauto_item['price_field'] = dd_list[0]
            #         elif td_list.index(td) == 1:
            #             icauto_item['year1'] = td
            #         elif td_list.index(td) == 2:
            #             icauto_item['year2'] = td
            #         elif td_list.index(td) == 3:
            #             icauto_item['year3'] = td
            #         elif td_list.index(td) == 4:
            #             icauto_item['year4'] = td
            #         elif td_list.index(td) == 5:
            #             icauto_item['year5'] = td
            #             #print(icauto_item)
            #             yield icauto_item
            #         elif td_list.index(td) == 6:
            #             icauto_item = IcautoItem()
            #             icauto_item['car_name'] = car_name
            #             icauto_item['city_name'] = td
            #             dd_list = response.xpath('//div[@class="carInfo"]/dd/text()').extract()
            #             icauto_item['price_field'] = dd_list[0]
            #         elif td_list.index(td) == 7:
            #             icauto_item['year1'] = td
            #         elif td_list.index(td) == 8:
            #             icauto_item['year2'] = td
            #         elif td_list.index(td) == 9:
            #             icauto_item['year3'] = td
            #         elif td_list.index(td) == 10:
            #             icauto_item['year4'] = td
            #         elif td_list.index(td) == 11:
            #             icauto_item['year5'] = td
            #             #print(icauto_item)
            #             yield icauto_item
