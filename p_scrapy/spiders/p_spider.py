import scrapy

from p_scrapy.items import PScrapyItem
import json

class firstSpider(scrapy.Spider):
    
    name = "p_spider"
    allowed_domains = ["pixiv.net"]
    base_url = "https://www.pixiv.net/ranking.php?p="
    start_urls = (
        base_url + str(1) + '&format=json',
        base_url + str(2) + '&format=json',
        base_url + str(3) + '&format=json',
        base_url + str(4) + '&format=json',
        base_url + str(5) + '&format=json',
        base_url + str(6) + '&format=json',
        base_url + str(7) + '&format=json',
        base_url + str(8) + '&format=json',
        base_url + str(9) + '&format=json',
        base_url + str(10) + '&format=json',
        
    )
    
    def parse(self, response):
        # 获取webItem对象
        item = PScrapyItem()
        objs = json.loads(response.body_as_unicode())
        for obj in objs['contents']:
            # 传入到item中
            item['img_name'] = obj['title']
            item['img_author'] = obj['user_name']
            item['img_id'] = obj['illust_id']
            item['img_page'] = obj['illust_page_count']
            item['img_rank'] = obj['rank']
            
            yield item