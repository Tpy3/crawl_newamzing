# -*- coding: utf-8 -*-
import scrapy
from ..items import CrawlNewamazingItem

class NewamazingSpider(scrapy.Spider):
    name = 'newamazing'

    def payload_data(self,pag):
        data = {'displayType': "G", 'subCd': "GO", 'orderCd': '1', 'pageALL': '1', 'pageGO': str(pag), 'pagePGO': '1',
                'waitData': "true", 'waitPage': "true", 'mGrupCd': "", 'SrcCls': "", 'tabList': "GO", 'regmCd': "",
                'regsCd': "",
                'beginDt': "2019/03/08", 'endDt': "2019/09/07", 'portCd': "", 'tdays': "", 'bjt': "", 'carr': "",
                'allowJoin': '1', 'allowWait': '1', 'ikeyword': ""}
        return data

    def start_requests(self):
        start_urls ='https://www.newamazing.com.tw/EW/GO/GroupList.asp?tabList=GO'
        for page in range(1,201):
            data = self.payload_data(page)
            yield scrapy.FormRequest(url=start_urls, method='POST', encoding='utf-8', formdata=data,meta={'page':page})

    def parse(self, response):
        first = CrawlNewamazingItem()
        page = response.meta['page']
        print(page)
        print('---'*50)
        for get_title in range(2,22):
            titlelist = response.xpath('//*[@id="listDataGO"]/div[%s]//text()'%(get_title)).extract()
            titlelist_url =response.xpath('//*[@id="listDataGO"]/div[%s]/div/div[3]/a/@href'%(get_title)).extract()
            titlelistlen = len(titlelist)
            if titlelistlen == 58:
                print(titlelist)
                first['pageid'] = 'P001'
                first['titleid'] = titlelist[7]
                first['titleurl'] = 'https://www.newamazing.com.tw'+titlelist_url[0]
                first['title'] = titlelist[8].lstrip().replace(' ','').replace('\n','').replace('\r','')
                first['days'] = titlelist[32].split('天')[0]
                first['departure_date'] = titlelist[34].replace('/','-')
                first['price'] = titlelist[42].replace(',','')
                first['total'] = titlelist[46]
                first['now'] = titlelist[49]
            elif titlelistlen == 59:
                print(titlelist)
                first['pageid'] = 'P001'
                first['titleid'] = titlelist[9]
                first['titleurl'] = 'https://www.newamazing.com.tw'+titlelist_url[0]
                first['title'] = titlelist[10].lstrip().replace(' ','').replace('\n','').replace('\r','')
                first['days'] = titlelist[32].split('天')[0]
                first['departure_date'] = titlelist[34].replace('/','-')
                first['price'] = titlelist[42].replace(',','')
                first['total'] = titlelist[46]
                first['now'] = titlelist[49]
            elif titlelistlen == 60:
                print(titlelist)
                if '\r\n' in titlelist[9]:
                    first['pageid'] = 'P001'
                    first['titleid'] = titlelist[10]
                    first['titleurl'] = 'https://www.newamazing.com.tw'+titlelist_url[0]
                    first['title'] = titlelist[11].lstrip().replace(' ','').replace('\n','').replace('\r','')
                    first['days'] = titlelist[33].split('天')[0]
                    first['departure_date'] = titlelist[35].replace('/','-')
                    first['price'] = titlelist[43].replace(',','')
                    first['total'] = titlelist[47]
                    first['now'] = titlelist[50]
                else:
                    first['pageid'] = 'P001'
                    first['titleid'] = titlelist[9]
                    first['titleurl'] = 'https://www.newamazing.com.tw' + titlelist_url[0]
                    first['title'] = titlelist[10].lstrip().replace(' ', '').replace('\n', '').replace('\r','')
                    first['days'] = titlelist[32].split('天')[0]
                    first['departure_date'] = titlelist[34].replace('/', '-')
                    first['price'] = titlelist[42].replace(',', '')
                    first['total'] = titlelist[46]
                    first['now'] = titlelist[49]
            elif titlelistlen == 61:
                print(titlelist)
                if '\r\n'in titlelist[9]:
                    first['pageid'] = 'P001'
                    first['titleid'] = titlelist[10]
                    first['titleurl'] = 'https://www.newamazing.com.tw'+titlelist_url[0]
                    first['title'] = titlelist[11].lstrip().replace(' ', '').replace('\n', '').replace('\r','')
                    first['days'] = titlelist[33].split('天')[0]
                    first['departure_date'] = titlelist[35].replace('/', '-')
                    first['price'] = titlelist[43].replace(',', '')
                    first['total'] = titlelist[47]
                    first['now'] = titlelist[50]
                else:
                    first['pageid'] = 'P001'
                    first['titleid'] = titlelist[9]
                    first['titleurl'] = 'https://www.newamazing.com.tw'+titlelist_url[0]
                    first['title'] = titlelist[10].lstrip().replace(' ','').replace('\n','').replace('\r','')
                    first['days'] = titlelist[34].split('天')[0]
                    first['departure_date'] = titlelist[36].replace('/', '-')
                    first['price'] = titlelist[44].replace(',','')
                    first['total'] = titlelist[48]
                    first['now'] = titlelist[51]
            elif titlelistlen == 62:
                print(titlelist)
                first['pageid'] = 'P001'
                first['titleid'] = titlelist[9]
                first['titleurl'] = 'https://www.newamazing.com.tw'+titlelist_url[0]
                first['title'] = titlelist[10].lstrip().replace(' ','').replace('\n','').replace('\r','')
                first['days'] = titlelist[34].split('天')[0]
                first['departure_date'] = titlelist[36].replace('/', '-')
                first['price'] = titlelist[44].replace(',','')
                first['total'] = titlelist[48]
                first['now'] = titlelist[51]
            elif titlelistlen == 63:
                print(titlelist)
                first['pageid'] = 'P001'
                first['titleid'] = titlelist[9]
                first['titleurl'] = 'https://www.newamazing.com.tw'+titlelist_url[0]
                first['title'] = titlelist[10].lstrip().replace(' ', '').replace('\n', '').replace('\r','')
                first['days'] = titlelist[36].split('天')[0]
                first['departure_date'] = titlelist[38].replace('/', '-')
                first['price'] = titlelist[46].replace(',', '')
                first['total'] = titlelist[50]
                first['now'] = titlelist[53]

            yield first

