# coding:utf8
from blog.craw.url_manage import UrlManage
from blog.craw.downloader import Downloader
from blog.craw.parser.parser import Parser


class Execute:
    def __init__(self):
        self.urlObj = UrlManage()
        self.downloaderObj = Downloader()
        self.parserObj = Parser()
        # self.daoObj = daoMode()

# http://travel.qunar.com/space/follow/list?userId=158928832@qunar
    def execute(self, rootUrl):
        self.urlObj.add_new_url(rootUrl)
        count = 0
        while (self.urlObj.has_new_url()):
            new_url = self.urlObj.get_new_url()
            self.parserObj.parse_data_followings(new_url)

if __name__ == '__main__':
    root_url = """http://travel.qunar.com/space/follow/list?userId=158928832@qunar"""
    spider = Execute()
    spider.execute(root_url)