import os
import urllib2
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item



class NipsSpider(CrawlSpider):
    name = "nips"
    allowed_domains = ['books.nips.cc']
    start_urls = [ 'http://books.nips.cc/' ]
    # Extract links on top-level index page and parse them with the spider's method parse_item
    rules = [
        Rule(SgmlLinkExtractor(allow=()), callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=()), follow=True)
    ]
    
    def download(self, url, file_name):
        print( "downloading " + file_name + " ...")
        req = urllib2.Request(url)
        f = urllib2.urlopen(req)
                    
        local_file = open(file_name, "w")
        local_file.write(f.read())
        local_file.close()

        print "done."
        
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        papers = hxs.select('//a[text()="[pdf]"]/@href').extract()
        count = 0
        for paper in papers:
            filename_long = str(paper.split("/")[-1])
            filename = "../pdfs/" + os.path.splitext(filename_long)[0]
            self.download(paper, filename)
            count = count + 1
        print "count:" + str(count)
        
        
        
    