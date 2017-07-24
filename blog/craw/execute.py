# coding:utf8
from .url_manage import UrlManage
from .downloader import Downloader


class Execute:
    def __init__(self):
        self.urlObj = UrlManage()

    def execute(self, rootUrl):
        self.urlObj.add_new_url()
