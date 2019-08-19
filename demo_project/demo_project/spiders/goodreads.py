import scrapy



class goodread_Spider(scrapy.Spider):
    """scarpy has a class of spider ,spider inturn has three properties
    1:identity ,2:request ,3:response"""
    # identity
    name="goodread"

    # request
    def start_requests(self):
        urls=[

        'https://www.goodreads.com/quotes?page=1',
        'https://www.goodreads.com/quotes?page=2',
        'https://www.goodreads.com/quotes?page=3',
        'https://www.goodreads.com/quotes?page=4',
        'https://www.goodreads.com/quotes?page=5',
        'https://www.goodreads.com/quotes?page=6',
        'https://www.goodreads.com/quotes?page=7',
        'https://www.goodreads.com/quotes?page=8',
        'https://www.goodreads.com/quotes?page=9',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)   #sending a get request to each of the url
# callback is for response that was sent back
    def parse(self,response):
        page_no=response.url.split("=")[1]
        # this will split the url into two portions ,the first have the left portion on the = ,and the otherone will have the right side of =
        _file="{0}.html".format(page_no) #the first portion is labeled as index 0 and the second as index 1
        with open(_file,'wb')as f:
            f.write(response.body) #the page we request the response will come in the form of same request that we did
