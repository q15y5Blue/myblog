# coding : utf8
import requests
import random


from blog.craw.download.constants import get_proxies_dic
from blog.craw.download.constants import get_headers


class Downloader:
    def download_html_by_url(self, url):
        return self.download_using_requests(url)

    # using
    def download_json_by_url(self, url):
        req = requests.get(url)
        if req.status_code == 200:
            return req.json()
        else:
            return None

    # url 是指要获取网页的url
    # http://travel.qunar.com/space/follow/list?userId=158928832
    # proxies_url = 'http://www.goubanjia.com/free/index.shtml'
    def download_using_requests(self, url):
        proxies_dic = get_proxies_dic()
        print(proxies_dic)
        request = requests.get(url, headers=get_headers, proxies=proxies_dic)  # , proxies=proxies
        if request.text is not None or request.text.__contains__('') is not True and request.status_code == 200:
            return request.text

#
# if __name__ == '__main__':
#     url = "https://travel.qunar.com/space/follow/list?userId=158928832" # 待连接的url
#     # url = 'https://www.sogou.com'
#     down = Downloader()
#     req = down.download_using_requests(url)
#     print(req.text)
