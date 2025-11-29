# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# ------------ 导入package -------------#
from pymongo import MongoClient

# ------------ 爬取结果输出：Pipeline类 -------------#
class AutohomePipeline(object):
    """
    AutohomePipeline类用于输出二手车之家网站的信息。
    """
    def __init__(self, host, port, db_name, collection_name):
        """
        初始化Pipeline类
        """
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name

    @classmethod
    def from_crawler(cls, crawler):
        """
        获取项目设置
        """
        host = crawler.settings.get('MONGODB_HOST')
        port = crawler.settings.get('MONGODB_PORT')
        db_name = crawler.settings.get('MONGODB_DBNAME')
        collection_name = crawler.settings.get('MONGODB_SHEETNAME')
        return cls(host, port, db_name, collection_name)

    def open_spider(self, spider):
        """
        与开始爬取的信号绑定，连接MongoDB
        """
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[self.db_name]

    def close_spider(self, spider):
        """
        与结束爬取的信号绑定，断开与MongoDB的连接
        """
        self.client.close()

    def process_item(self, item, spider):
        """
        将爬取返回的car_item，写入MongoDB
        """
        data = {
            'url': item['url'],
            'img_url': item['img_url'],
            'title': item['title'],
            'brand': item['brand'],
            'model': item['model'],
            'license_time': item['license_time'],
            'update_time': item['update_time'],
            'mileage': item['mileage'],
            'transmission': item['transmission'],
            'emission_standards': item['emission_standards'],
            'displacement': item['displacement'],
            'num_of_transfer': item['num_of_transfer'],
            'location': item['location'],
            'province_name': item['province_name'],
            'engine': item['engine'],
            'color': item['color'],
            'fuel_standard': item['fuel_standard'],
            'drive_model': item['drive_model'],
            'fuel_type': item['fuel_type'],
            'pure_elec_range': item['pure_elec_range'],
            'fast_charge_time': item['fast_charge_time'],
            'battery_capacity': item['battery_capacity'],
            'slow_charge_time': item['slow_charge_time'],
            'price': item['price']
        }
        self.db[self.collection_name].insert_one(data)
        return item
