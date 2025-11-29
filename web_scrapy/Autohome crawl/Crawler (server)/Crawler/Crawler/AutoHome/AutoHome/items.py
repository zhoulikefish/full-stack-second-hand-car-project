# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutohomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 二级链接
    url = scrapy.Field()
    #page = scrapy.Field()
    img_url = scrapy.Field()
    # 车标题
    title = scrapy.Field()
    # 车品牌
    brand = scrapy.Field()
    # 车型
    model = scrapy.Field()
    # 上牌时间
    license_time = scrapy.Field()
    # 发布时间
    update_time = scrapy.Field()
    # 里程
    mileage = scrapy.Field()
    # 变速箱
    transmission = scrapy.Field()
    # 排放标准
    emission_standards = scrapy.Field()
    # 排量
    displacement = scrapy.Field()
    # 年检到期
    inspection_due = scrapy.Field()
    # 保险到期
    insurance_due = scrapy.Field()
    # 过户次数
    num_of_transfer = scrapy.Field()
    # 所在地
    location = scrapy.Field()
    province_name = scrapy.Field()
    # 发动机
    engine = scrapy.Field()
    # 颜色
    color = scrapy.Field()
    # 燃油标号
    fuel_standard = scrapy.Field()
    # 驱动方式
    drive_model = scrapy.Field()
    # 亮点
    highlight = scrapy.Field()
    # 文字描述
    description = scrapy.Field()
    # 图片
    image = scrapy.Field()

    # 以下属性为电动车独有
    # 燃料类型
    fuel_type = scrapy.Field()
    # 纯电续航里程
    pure_elec_range = scrapy.Field()
    # 标准快充
    fast_charge_time = scrapy.Field()
    # 标准容量
    battery_capacity = scrapy.Field()
    # 标准慢充
    slow_charge_time = scrapy.Field()
    # 价格
    price = scrapy.Field()



