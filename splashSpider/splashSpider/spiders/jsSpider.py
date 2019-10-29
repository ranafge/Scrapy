import scrapy
from scrapy.loader import ItemLoader
from ..items import BgmeaItem

class BgmeaSpider(scrapy.Spider):
    name = 'bgmea'

    def start_requests(self):
        urls =['http://www.bgmea.com.bd/member/details/{}#tabs-3'.format(num) for num in range(19950,24793)]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        l = ItemLoader(item=BgmeaItem(), response=response)
        l.add_xpath('Company_Name','//div[@id= "tabs-1"]/table/tr[@class="tr_member"]/td/span/text()')
        l.add_xpath('Name','//*[@id="director_row0"]/td[2]/text()')
        l.add_xpath('Designation','//*[@id="director_row0"]/td[1]/text()')
        l.add_xpath('EmailID','//div[@id= "tabs-3"]/table/tr[@class="tr_member"][7]//td/label[1]/text()')
        l.add_xpath('Phone_Number','//*[@id="director_row0"]/td[3]/text()')
        l.add_xpath('Address','//div[@id= "tabs-3"]/table/tr[@class="tr_member"][5]//tr//td//text()')
        return l.load_item()


class MySpider(scrapy.Spider):
    name = 'promofarma'
    rotate_user_agent = True
    start_urls = ["https://www.promofarma.com/en/neck-and-neckline/c-291"]

    def parse(self, response):
        neckAndneck = dict()
        for item in response.css('div.row.no-gutters.mt-md-2>div >section >div.row.gutter-8 >div'):
            neckAndneck['product_code'] =item.css('::attr(data-id)').extract_first(),
            neckAndneck['product_price'] = item.css('::attr(data-price)').extract_first(),
            neckAndneck['product_name'] =  item.css('a.link.GA_coupon_name >h3::text').extract_first(),
            neckAndneck['category'] = response.css('ol.breadcrumb.ml-1.ml-md-0.my-1 > li > a ::text').extract()[1]
            neckAndneck['subcategory'] =  response.css('ol.breadcrumb.ml-1.ml-md-0.my-1 > li > a ::text').extract()[2]
            yield neckAndneck

        next_page_url = response.css('nav#page-filters-box > ul > li a.page-link ::attr(href)').extract()[1]

        if next_page_url:

            yield response.follow(next_page_url)





