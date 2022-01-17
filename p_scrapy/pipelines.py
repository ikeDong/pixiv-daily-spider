# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import pymysql


class MySQLPipeline():
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
    
    @classmethod   # 无需实例化，使用cls来访问变量
    def from_crawler(cls, crawler):
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            database = crawler.settings.get('MYSQL_DATABASE'),
            user = crawler.settings.get('MYSQL_USER'),
            password = crawler.settings.get('MYSQL_PASSWORD'),
            port = crawler.settings.get('MYSQL_PORT')
        )
        
    def open_spider(self, spider):
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()
        sql = "TRUNCATE TABLE pixiv"
        self.cursor.execute(sql)
        
    def close_spider(self, spider):
        self.db.close()
        
    def process_item(self, item, spider):
        data = dict(item) # 将item变为字典形式
        keys = ",".join(data.keys()) # 将字典的键值变成用,分割的字符串
        values = ",".join(['%s']*len(data)) # 根据字典的长度建立对应长数的%s
        sql = "insert into %s (%s) values (%s)" % ('pixiv', keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item