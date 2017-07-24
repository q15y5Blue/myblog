# coding:utf8
from urllib.request import urlopen
from bs4 import BeautifulSoup
from blog.models import Persons
from .downloader import Downloader
import re
class Parser:

    # 公用解析方法，返回soup对象
    def parse_url(self,url):
        html_data = Downloader().download_html_by_url(url)
        soup = BeautifulSoup(html_data, "html.parser")
        return soup

    # http://travel.qunar.com/space/follow/list?userId=158928832@qunar?page=1
    # 根据url下载 文档同时解析
    def parse_data_followings(self, url, pageNo):
        print(url)
        soup = self.parse_url(url)
        page = soup.find('ul', class_='fans-list')
        if page is None:
            return
        li = page.find_all('li')
        per = Persons()
        per.name = soup.h3.span['title']
        per.describe = soup.find("span", class_='view-text').text
        if(len(li)) > 0:
            new_url = url+"?page=%s"%(pageNo)
            pageNo=pageNo+1
            self.parse_data_followings(new_url,pageNo)
        return '123',"123123456"
