# coding:utf8
from blog.craw.url_manage import UrlManage
from blog.craw.downloader import Downloader
from blog.craw.parser import Parser
from blog.craw.daoMode import daoMode



class Execute:
    def __init__(self):
        self.urlObj = UrlManage()
        self.downloaderObj = Downloader()
        self.parserObj = Parser()
        self.daoObj = daoMode()

# http://travel.qunar.com/space/follow/list?userId=158928832@qunar
    def execute(self, rootUrl):
        self.urlObj.add_new_url(rootUrl)
        count = 0
        while (self.urlObj.has_new_url()):
            new_url = self.urlObj.get_new_url()
            # html_data = self.downloaderObj.download_html_by_url(new_url)
            # url_list = self.parserObj.parse_data_followings(html_data)
            url_list, url_data = self.parserObj.parse_data_followings(new_url,1)

if __name__ == '__main__':
    root_url = """http://travel.qunar.com/space/follow/list?userId=158928832@qunar"""
    spider = Execute()
    spider.execute(root_url)