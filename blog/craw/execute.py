# coding:utf8
from blog.craw.url_manage import UrlManage
from blog.craw.downloader import Downloader
from blog.craw.parser.parser import Parser
import threading

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
            count += 1
            new_url = self.urlObj.get_new_url()

            per = self.parserObj.parse_data_followings(new_url)   # 获取个人信息
            # AttributeError: 'NoneType' object has no attribute 'get_following_str_to_list'
            # get a question 有的None url 会添加到这里
            if per is not None:
                self.urlObj.add_new_url_list(per.get_following_str_to_list)
                self.urlObj.add_new_url_list(per.get_fans_str_to_list)
            print("次数呢:", count)

if __name__ == '__main__':
    root_url = """http://travel.qunar.com/space/follow/list?userId=158928832"""
    spider = Execute()
    spider.execute(root_url)

