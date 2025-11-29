"""
爬虫主程序，重写Scrapy的方法，用于访问和解析项目具体的网站。
"""

# ------------ 导入package -------------#
from urllib.request import Request
import scrapy
from scrapy.downloadermiddlewares.retry import get_retry_request
import pandas as pd
from ..items import AutohomeItem

# ------------ 爬取汽车之家：继承Spider类 -------------#
class AutoHomeSpider(scrapy.Spider):
    """
    AutoHomeSpider类是一个Scrapy的Spider类，用于爬取、解析二手车之家网站的信息。
    """
    # 类变量
    name = 'AutoHome'  # 项目名称
    allowed_domains = ['che168.com']  # 可以爬取的域名
    prefixes = []  # 网页前缀
    suffix = 'exx0/'  # 网页后缀
    # 价格列表（用于分类爬取）
    price_field = ['0-3', '3-5', '5-8', '8-10', '10-15', '15-20', '20-30', '30-50', '50-100', '100-0']
    # 城市列表（用于选取城市）
    city_list = pd.read_csv('./spiders/city.csv')['city_url']
    # 获取各城市、各价位对应的一级链接前缀放入prefixes
    for city in city_list:
        for price in price_field:
            prefixes.append('https://www.che168.com{}{}/a0_0msdgscncgpi1ltocsp'.format(city, price))
    province_df = pd.read_csv('./spiders/province.csv')
    province_city_mapping_dict = dict(zip(province_df['location'], province_df['province_name']))
    def start_requests(self):
        """
        发出初始请求，爬取每个城市、价位对应网页池的第一页，并指定回调函数和错误回调函数。
        """
        for prefix in self.prefixes:
            # 访问目标网页池的第一页并调用Parse解析
            yield scrapy.Request(prefix + '1' + self.suffix, callback=self.parse, errback=self.errback_parse,
                                 priority=1)

    def parse(self, response):
        """
        解析一级链接的页面，获取下一页的链接和二级链接。
        """
        # 通过Xpath获取下一页的链接（链式爬取）
        next_page_urls = response.xpath('//div[@class="page fn-clear"]/a[position()=last()]/@href').extract()
        if len(next_page_urls) != 0:
            next_page_url = 'https://www.che168.com' + next_page_urls[0]
            yield scrapy.Request(url=next_page_url, callback=self.parse, errback=self.errback_parse, priority=1)
        # 通过Xpath获取第一页的二级链接
        second_urls = response.xpath('//li[@class="cards-li list-photo-li " and @name="lazyloadcpc"]/a/@href').extract()
        # 利用for循环访问第一页的二级链接
        if len(second_urls) != 0:
            for second_url in second_urls:
                if second_url.startswith("/deal"):
                    second_url = 'https://www.che168.com' + second_url
                elif second_url.startswith("//www.che168.com/"):
                    second_url = 'https:' + second_url
                car_item = AutohomeItem()
                car_item['url'] = second_url
                # 返回二级链接页面的解析迭代器，进入Scrapy的调度器
                yield scrapy.Request(url=second_url, callback=self.sec_handler, errback=self.errback_parse,
                                     meta={'item': car_item})

    def errback_parse(self, fail):
        """
        处理请求失败的情况，生成新的请求并重试。
        """
        # 根据预设的Retry次数进行Retry
        new_request = Request(url=fail.request.url, method="GET")
        new_request_or_none = get_retry_request(
            new_request,
            spider=self,
            reason='retry',
        )
        return new_request_or_none

    def sec_handler(self, response):
        """
        处理二级链接的页面，提取所需的信息。
        """

        # 获取之前已经创建好的car_item（已经包括URL这一属性了）
        car_item = response.meta['item']

        # Xpath解析二级页面
        if len(response.xpath('//span[contains(@id, "overlayPrice")]/text()').extract()) != 0:
            price = response.xpath('//span[contains(@id, "overlayPrice")]/text()').extract()
        else:
            price = response.xpath('//div[contains(@class, "goodstartmoney")]/text()').extract()
        title = response.xpath('//h3[@class="car-brand-name"]/text()').extract()
        update_time = response.xpath('//li[span[text()="发布时间"]]/text()').extract()
        brand = response.xpath('//div[contains(@class, "bread-crumbs content")]/a[last()-2]/text()').extract()
        model = response.xpath('//div[contains(@class, "bread-crumbs content")]/a[last()-1]/text()').extract()
        img_url = response.xpath('//a[@class="jiaodianphotoclick"]/img/@src').extract()
        license_time = response.xpath('//li[span[text()="上牌时间"]]/text()').extract()
        mileage = response.xpath('//li[span[text()="表显里程"]]/text()').extract()
        transmission = response.xpath('//li[span[text()="变\xa0\xa0速\xa0\xa0箱"]]/text()').extract()

        emission_standards = response.xpath('//li[span[text()="排放标准"]]/text()').extract()
        displacement = response.xpath('//li[span[text()="排\xa0\xa0\xa0\xa0\xa0\xa0\xa0量"]]/text()').extract()

        fuel_type = response.xpath('//li[span[text()="燃料类型"]]/text()').extract()
        pure_elec_range = response.xpath(
            '//li[(span[text()="CLTC纯电续航里程"] or span[text()="NEDC纯电续航里程"])]/text()').extract()

        num_of_transfer = response.xpath('//li[span[text()="过户次数"]]/text()').extract()
        location = response.xpath('//li[span[text()="所\xa0\xa0在\xa0\xa0地"]]/text()').extract()
        province_name = self.province_city_mapping_dict[location[0]]
        engine = response.xpath('//li[span[text()="发\xa0\xa0动\xa0\xa0机"]]/text()').extract()
        fast_charge_time = response.xpath('//li[span[text()="标准快充"]]/text()').extract()

        color = response.xpath('//li[span[text()="车身颜色"]]/text()').extract()
        fuel_standard = response.xpath('//li[span[text()="燃油标号"]]/text()').extract()
        drive_model = response.xpath('//li[span[text()="驱动方式"]]/text()').extract()

        battery_capacity = response.xpath('//li[span[text()="标准容量"]]/text()').extract()
        slow_charge_time = response.xpath('//li[span[text()="标准慢充"]]/text()').extract()
        # 设置car_item的键值对
        CarItem.set_car_item(car_item,
                             title=title,
                             update_time=update_time,
                             brand=brand,
                             model=model,
                             price=price,
                             img_url=img_url,
                             license_time=license_time,
                             mileage=mileage,
                             transmission=transmission,
                             fuel_type=fuel_type,
                             pure_elec_range=pure_elec_range,
                             emission_standards=emission_standards,
                             displacement=displacement,
                             num_of_transfer=num_of_transfer,
                             location=location,
                             province_name=province_name,
                             engine=engine,
                             fast_charge_time=fast_charge_time,
                             color=color,
                             fuel_standard=fuel_standard,
                             drive_model=drive_model,
                             battery_capacity=battery_capacity,
                             slow_charge_time=slow_charge_time
                             )
        # 返回解析后获得的一组数据，进入Scrapy的Pipeline
        yield car_item


class CarItem:
    @classmethod
    def set_car_item(cls, car_item, **kwargs):
        """
        用于设置car_item字典中的键值对，并进行数据清洗
        """
        for key, value in kwargs.items():
            if len(value) == 0:
                car_item[key] = 'NaN'
            else:
                if (key == 'brand' or key == 'model'):
                    car_item[key] = value[0].strip()[2:]
                elif key != 'url':
                    if key == 'img_url' or key == 'province_name':
                        car_item[key] = value
                    else:
                        car_item[key] = value[0].strip()
                        if key == 'price':
                            if value[0].strip().endswith('万'):
                                car_item[key] = value[0].strip().replace('￥', '').replace('万', '')
                            else:
                                car_item[key] = value[0].strip()[1:]
                        if key == 'num_of_transfer':
                            car_item[key] = value[0].strip().replace('次（以车辆登记证为准）', '')
                else:
                    car_item[key] = value
