class ListOutputPipeline(object):

    def open_spider(self, spider):
        self.file = open(spider.settings.get('OUTPUT_FILEPATH'), 'w')
    
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = item['url'] + "\n"
        self.file.write(line)
        return item