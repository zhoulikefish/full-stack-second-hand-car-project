# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time
import csv
import json
import pymongo
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings

class IcautoPipeline(object):
    def __init__(self, output_file, output_format):
        self.output_file = output_file
        self.output_format = output_format
        self.file = None
        self.writer = None

    @classmethod
    def from_crawler(cls, crawler):
        current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        output_file = crawler.settings.get('OUTPUT_FILE', 'output') + '_{}'.format(current_time)
        output_format = crawler.settings.get('OUTPUT_FORMAT', 'csv')
        return cls(output_file, output_format)

    def open_spider(self, spider):
        field_names = [
            'car_name',
            'car_img',
            'image_paths',
            'price_field',
            'model',
            'city_name',
            'year1',
            'year2',
            'year3',
            'year4',
            'year5',
        ]
        if self.output_format == 'csv':
            self.file = open(f'{self.output_file}.csv', 'w', newline='', encoding='utf-8')
            self.writer = csv.DictWriter(self.file, fieldnames=field_names)
            self.writer.writeheader()
        elif self.output_format == 'json':
            self.file = open(f'{self.output_file}.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        if self.file:
            self.file.close()

    def process_item(self, item, spider):
        if self.output_format == 'csv':
            self.writer.writerow(item)
        elif self.output_format == 'json':
            item_json = json.dumps(dict(item), ensure_ascii=False)
            self.file.write(item_json + '\n')
        return item


from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request

class ImgproPipeline(ImagesPipeline):
    default_headers = {
        'referer': 'https://www.icauto.com.cn/usedcar/s1880/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def get_media_requests(self, item, info):
        image_url = item['car_img']
        self.default_headers['referer'] = image_url
        yield Request(image_url, headers=self.default_headers)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
