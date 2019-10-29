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




