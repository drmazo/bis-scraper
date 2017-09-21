# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from scrapy.http import Request


class BeatsinspacePipeline(object):
    def process_item(self, item, spider):
        return item


class MyFilePipeline(FilesPipeline):
    # Name download version
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']  # Like this you can use all from item, not just url.
        name = u''.join(item['name'])
        date = u''.join(item['date'])
        artist = u''.join(item['artist'])
        part = u''.join(item['part'])
        return 'full/%s - %s - %s - %s.mp3' % (name, date, artist, part)

    def get_media_requests(self, item, info):
        # yield Request(item['images']) # Adding meta. Dunno how to put it in one line :-)
        for url in item['file_urls']:
            yield Request(url, meta={'item': item})
