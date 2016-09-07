import scrapy

from imdb.items import ImdbItem

class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["imdb.com"]
    start_urls = []
    with open("/home/aayushgoel92/Documents/cinefy/cinefy.git/imdb/movie_id.txt","r") as f:
        for line in f:
            start_urls.append("http://www.imdb.com/title/"+line.strip()+"/reviews?count=100000&start=0")

    def parse(self, response):
        movie_id = response.url.split("/")[-2]
        for sel in response.xpath('//div[@id="tn15content"]//p'):
            item = ImdbItem()
            item['movie'] = movie_id
            item['review'] = sel.xpath('text()').extract()
            yield item
