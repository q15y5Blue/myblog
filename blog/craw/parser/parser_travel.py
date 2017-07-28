# coding:utf8
# url = http://travel.qunar.com/space/158928832@qunar
from blog.craw.downloader import Downloader
from bs4 import BeautifulSoup
from blog.models import Travels
from blog.models import TravelsCatalog
from blog.models import TravelsCatalogContent
from datetime import datetime
import re



def get_beautifulsoup_obj(url):
    dt = Downloader()
    html_data = dt.download_html_by_url(url)
    soup = BeautifulSoup(html_data, "html.parser")
    return soup

# http://travel.qunar.com/space/notes?page=1&pageSize=57&userId=158928832
def get_travel_urls_by_one_person(url):
    dt = Downloader()
    js = dt.download_json_by_url(url)
    count = js['data']['count']
    # 获取当前用户下所有列表
    if count > 1000:
        url = url.replace('pageSize=1', 'pageSize=%s' % count)
        js = dt.download_json_by_url(url)
    list_data = js['data']  # 所有list
    url_list = re.findall('(?<=<a href=\"//).*?(?=\")', list_data['html'])
    return url_list

def get_travel_by_urls(url_list):
    for url in url_list:
        print(url)
        travel = Travels()

        soup = get_beautifulsoup_obj("http://"+url)
        travel.travel_title = soup.title.string                       # title

        test= soup.find('li', class_='head').prettify()
        user_id = re.search('(?<=space/)(\d+)', test).group(0)
        travel.travel_user_id = int(user_id)

        test = re.search('\d{4}/\d{2}/\d{2}', soup.find('li', class_='date').prettify()).group(0).__str__()
        travel.travel_create_date = datetime.strptime(test, '%Y/%m/%d').date()  # 创建日期get

        test = soup.find('span', class_='view_count').string
        travel.travel_view_number = int(test)                           # 浏览数量get

        test = soup.find('li', class_='flag')
        if test is not None:
            travel.travel_commended = True

        travel_ul = soup.find('ul', class_='foreword_list')         # 获取travel 信息
        when_li = travel_ul.find('li', class_='when').prettify()        # 获取travel时间
        test = re.search('\d{4}/\d{2}/\d{2}', when_li).group(0).__str__()
        dt = datetime.strptime(test, '%Y/%m/%d')
        travel.travel_when = dt.date()

        howlong_li = travel_ul.find('li', class_='howlong')
        test = howlong_li.find('span', class_='data')
        travel.travel_how_long = int(test.string)                   # 去了多久

        howmuch_li = travel_ul.find('li', class_='howmuch')
        test = howmuch_li.find('span', class_='data')
        travel.travel_how_much = int(test.string)                   # 花了多少钱

        who_li = travel_ul.find('li', class_='who')
        test = who_li.find('span', class_='data')
        travel.travel_who = test.string                             # 和谁一起去的

        how_li = travel_ul.find('li', class_='how')
        test = how_li.find('span', class_='data')
        print(test.string)
        travel.travel_how = test.string.split('\xa0')      # 咋去的
        print(travel.travel_how)
        print("谁", travel.travel_who)
        print("钱", travel.travel_how_much)
        print("长", travel.travel_how_long)
        print("啥时候", travel.travel_when)
        # print(travel.travel_user)
        # get travel
        #travel id
        test =re.search('\d+', url).group(0)
        print(test)
        travel.travel_id = int(test)

        test = soup.find('div', class_='e_main').prettify() # 简单粗暴
        travel.travel_text = test
        travel.save()
        break

# 放弃了
def parser_catalog(soup, travel_id):
    cata_title = soup.find_all('h4', class_='period_hd')
    for cata in cata_title:
        travel_cata = TravelsCatalog()
        travel_cata.catalog_title = cata.find('div', class_='text').string
        travel_cata.catalog_travel_id = travel_id
        travel_cata.catalog_identify = travel_id

# http://travel.qunar.com/space/notes?page=1&pageSize=57&userId=158928832
if __name__ == '__main__':
    url = r'http://travel.qunar.com/space/notes?page=1&pageSize=1000&userId=158928832'
    list = get_travel_urls_by_one_person(url)
    get_travel_by_urls(list)
