import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'getlatka.com'
    allowed_domains = ['getlatka.com']
    start_urls = ['https://getlatka.com/saas-companies']

    def parse(self, response):
        name = []
        revenues =[]
        fundings = []
        valuation =[]
        cashFlow=[]
        Founder = []
        Teamsize=[]
        age=[]
        location=[]
        Industry=[]
        asof=[]
        table = response.css("[class*='data-table_table'] tr")
        tr=table[2]
        i= 0
        for tr in table:
            name.append(tr.css("[class*='cells_link'] ::text").get())
            revenues.append(tr.xpath(f'//tr[{i}]/td[3]/p/text()').extract()[1])
            fundings.append(tr.xpath(f'//tr[{i}]/td[4]/p/text()').extract()[1])
            valuation.append(tr.xpath(f'//tr[{i}]/td[5]/p/text()').extract()[1])
            cashFlow.append(tr.xpath(f'//tr[{i}]/td[6]/span/text()').extract()[1])
            FirstName = tr.xpath(f'//tr[{i}]/td[7]/div/a/text()').extract()[0]
            LastName = tr.xpath(f'//tr[{i}]/td[7]/div/a/text()').extract()[2]
            Name=FirstName+" "+LastName
            Founder.append(Name)
            Teamsize.append(tr.xpath(f'//tr[{i}]/td[8]/p/text()').extract()[1])
            age.append(tr.xpath(f'//tr[{i}]/td[9]/p/text()').extract()[1])
            location.append(tr.xpath(f'//tr[{i}]/td[10]/a/text()').extract()[1])
            Industry.append(tr.xpath(f'//tr[{i}]/td[11]/a/text()').extract()[0])
            asof.append(tr.xpath(f'//tr[{i}]/td[12]/p/text()').extract()[1])
            i=i+1
        
        yield {"Company Name": name,"Revenue":revenues,"Funding ":fundings,"Valuation":valuation,"CashFlow":cashFlow,"Founder Name":Founder,"TeamSize":Teamsize,"Age":age,"Location":location,"Industry":Industry,"Asof":asof}
        # scrapy crawl getlatka.com -o test.jsonscrapy crawl getlatka.com -o test.json