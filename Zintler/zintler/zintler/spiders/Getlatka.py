
import scrapy

class Getlatkaspider(scrapy.Spider):
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

        for i in range(1,len(table)):
            tr=table[i]
            a=tr.xpath(f'td[3]/p/text()').extract()
            b=tr.xpath(f'td[4]/p/text()').extract()
            c=tr.xpath(f'td[5]/p/text()').extract()
            d=tr.xpath(f'td[6]/span/text()').extract()
            if(len(a)!=0):
                fundings.append(a[1] )
            else:
                fundings.append(None)
            if(len(b)!=0):
                revenues.append(b[1] )
            else:
                revenues.append(None)
            if(len(c)!=0):
                valuation.append(c[1])
            else:
                valuation.append(None)
            if(len(d)!=0):
                cashFlow.append(d[1])
            else:
                cashFlow.append(None)
            
            name.append(tr.css("[class*='cells_link'] ::text").get())
            
       
            
            
            FirstName = tr.xpath(f'td[7]/div/a/text()').extract()[0]
            LastName = tr.xpath(f'td[7]/div/a/text()').extract()[2]
            Name=FirstName+" "+LastName
            Founder.append(Name)
            Teamsize.append(tr.xpath(f'td[8]/p/text()').extract()[1])
            age.append(tr.xpath(f'td[9]/p/text()').extract()[1])
            location.append(tr.xpath(f'td[10]/a/text()').extract()[1])
            Industry.append(tr.xpath(f'td[11]/a/text()').extract()[0])
            asof.append(tr.xpath(f'td[12]/p/text()').extract()[1])
           
        yield {"Company Name": name,"Revenue":revenues,"Funding ":fundings,"Valuation":valuation,"CashFlow":cashFlow,"Founder Name":Founder,"TeamSize":Teamsize,"Age":age,"Location":location,"Industry":Industry,"Asof":asof}
        # scrapy crawl getlatka.com -o test.jsonscrapy crawl getlatka.com -o test.json
