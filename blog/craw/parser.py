# coding:utf8
from urllib.request import urlopen
from bs4 import BeautifulSoup
from blog.models import Persons
from .downloader import Downloader
import re


class Parser:
    # 公用解析方法,使用BeautifulSoup模块，返回soup对象
    def parse_url(self,url):
        dt = Downloader()
        html_data = dt.download_html_by_url(url)
        soup = BeautifulSoup(html_data, "html.parser")
        return soup

    # http://travel.qunar.com/space/follow/list?userId=158928832@qunar?page=1
    # 根据url下载 文档同时解析
    def parse_data_followings(self, url):
        soup = self.parse_url(url)
        page = soup.find('ul', class_='fans-list')
        if page is None:
            return
        li = page.find_all('li')
        per = Persons()
        per.name = soup.h3.span['title']
        per.describe = soup.find("span", class_='view-text').text

        # 获取关注的人数
        follows_li = self.get_relation_data(url)
        follow_list = []
        for lis in follows_li:
            for li in lis:
                follow_list.append(li['data-id'])
        per.set_following_list_to_str(follow_list)
        per.followings_number = per.set_followings_number()
        print(per.name, "关注的人数：", per.followings_number)

        # 获取粉丝信息
        url = url[:36] + "/fans" + url[36:]
        fans_li = self.get_relation_data(url)
        fans_list = []
        for lis in fans_li:
            for li in lis:
                fans_list.append(li['data-id'])
        per.set_fans_list_to_str(fans_list)
        per.fans_number = per.set_fans_number()
        print(per.name,"粉丝人数：",per.fans_number)
        return '123', "123123456"


    # 循环获取分页关注的人数
    # http://travel.qunar.com/space/follow/list?userId=158928832@qunar&page=4
    def get_relation_data(self, url):
        li_list = []
        for pageNo in range(1, 10000):
            new_url = url+"&page=%s"%(pageNo)
            print("获取分页关注人：", new_url)
            pageNo += 1
            soup = self.parse_url(new_url)
            ul = soup.find('ul', class_='fans-list')
            if ul is None:
                break
            li = ul.find_all('li')
            if li is None or len(li) == 0:
                break
            li_list.append(li)
        return li_list

    # def get_fans_data(self, url):
    #
    #     li_list = []
    #     for pageNo in range(1, 10000):
    #         new_url = url+"&page=%s"%(pageNo)
    #         print("获取分页粉丝:", new_url)
    #         pageNo += 1
    #         soup = self.parse_url(new_url)
    #         ul = soup.find('ul', class_='fans-list')
    #         if ul is None:
    #             break
    #         li = ul.find_all('li')
    #         if li is None or len(li) == 0:
    #             break
    #         li_list.append(li)
    #     return li_list


