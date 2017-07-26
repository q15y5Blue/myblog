# coding:utf8
# 解析travel .ddddddddd
# url = http://travel.qunar.com/space/158928832@qunar
from blog.craw.downloader import Downloader
from bs4 import BeautifulSoup


# http://travel.qunar.com/space/notes?page=1&pageSize=57&userId=158928832
def get_travel_by_url(url):
    dt = Downloader()
    js = dt.download_json_by_url(url)
    count = js['data']['count']

    url_new = r'http://travel.qunar.com/space/notes?page=1&pageSize=%s&userId=158928832' % count
    jso = dt.download_json_by_url(url_new)
    list_data = jso['data']
    print(list_data)

# http://travel.qunar.com/space/notes?page=1&pageSize=57&userId=158928832
if __name__ == '__main__':
    url = r'http://travel.qunar.com/space/notes?page=1&pageSize=1&userId=158928832'
    get_travel_by_url(url)
