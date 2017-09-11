# coding:utf8
import re

from bs4 import BeautifulSoup

from blog.craw.download.downloader import Downloader
from blog.craw.parser.parser_travel import get_travel_by_urls, get_travel_urls_by_one_person
from blog.models import Persons


class Parser:
    # 公用解析方法,使用BeautifulSoup模块，返回soup对象
    def parse_url(self, url):
        dt = Downloader()
        html_data = dt.download_html_by_url(url)
        soup = BeautifulSoup(html_data, "html.parser")
        return soup

    # http://travel.qunar.com/space/follow/list?userId=158928832@qunar?page=1
    # 根据url下载 文档同时解析
    def parse_data_followings(self, url):
        soup = self.parse_url(url)
        page = soup.find('ul', class_='fans-list')
        print("正在获取个人信息…………")
        if page is None:
            return None
        li = page.find_all('li')

        per = Persons()
        per.name = soup.h3.span['title']
        if soup.find("span", class_='view-text') is not None:
            per.describe = soup.find("span", class_='view-text').text

        # portrait 头像get
        str = soup.find('dt', class_='pic').prettify()
        portrait = re.search('(?<=src=\").*?(?=\")', str).group(0)
        per.portrait = portrait

        # 获取关注的人数
        follow_list = self.get_relation_data(url, 0)
        per.set_following_list_to_str(follow_list)
        per.followings_number = per.set_followings_number()
        print(per.name, "所关注的人数：", per.followings_number)

        # 获取粉丝信息
        fans_list = self.get_relation_data(url, fans=1)
        per.set_fans_list_to_str(fans_list)
        per.fans_number = per.set_fans_number()
        print(per.name, "的粉丝人数：", per.fans_number)

        # identity
        t = re.search('(?<=userId\=)\d+', url).group(0)
        per.identify = t
        try:
            if Persons.objects.get(pk=per.identify) is not None:
                print("这个人数据库中已经存在了")
                return per
        except Persons.DoesNotExist:
            print("这个人还未收录")
            per.save()
            new_url = r'http://travel.qunar.com/space/notes?page=1&pageSize=1000&userId=%s' % per.identify
            url_list = get_travel_urls_by_one_person(new_url)
            get_travel_by_urls(url_list)
            return per

    # 循环获取分页关注的人数
    # http://travel.qunar.com/space/follow/list?userId=158928832@qunar&page=4
    def get_relation_data(self, url, fans):
        if fans == 1:
            url = url[:36] + "/fans" + url[36:]
        rs_list = []
        li_list = []
        for pageNo in range(1, 10000):
            new_url = url+"&page=%s" % pageNo
            pageNo += 1
            soup = self.parse_url(new_url)
            ul = soup.find('ul', class_='fans-list')
            if ul is None:
                break
            li = ul.find_all('li')
            if li is None or len(li) == 0:
                break
            li_list.append(li)

        for lis in li_list:
            for li in lis:
                rs_list.append(li['data-id'])
        return rs_list

if __name__ == '__main__':
    par = Parser()
    par.parse_data_followings('https://travel.qunar.com/space/follow/list?userId=158928832')