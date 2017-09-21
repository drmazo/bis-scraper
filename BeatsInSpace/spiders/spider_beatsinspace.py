import scrapy
from BeatsInSpace.items import PodcastItem
from datetime import datetime


class BeatsSpider(scrapy.Spider):
    name = "beats"
    start_urls = ['http://www.beatsinspace.net/playlists']

    def parse(self, response):
        for href in response.xpath('//a[@class="show-link"]//@href').extract():
            link = 'http://www.beatsinspace.net' + href
            yield response.follow(link, self.parse_mixes)

    def parse_mixes(self, response):
        artist1 = response.xpath('(//span[@class="artist-name"])[1]//text()').extract()
        artist2 = response.xpath('(//span[@class="artist-name"])[2]//text()').extract()
        download1 = u''.join(response.xpath('(//a[@class="button download"])[1]/@href').extract())
        download2 = u''.join(response.xpath('(//a[@class="button download"])[2]/@href').extract())
        name = response.xpath('(//span[@class="show-number"])[1]//text()').extract()
        date = response.xpath('(//span[@class="date-display-single"])[1]//text()').extract_first()

        datetime_object = datetime.strptime(date, '%B %d  %Y')

        dateitem = datetime_object.strftime('%d-%m-%Y')

        yield PodcastItem(name=name, date=dateitem, artist=artist1, part='part 1', file_urls=[download1], )
        yield PodcastItem(name=name, date=dateitem, artist=artist2, file_urls=[download2], part='part 2')
