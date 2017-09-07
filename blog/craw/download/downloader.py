# coding : utf8
import requests
import random


from blog.craw.download.constants import get_proxies_dic
from blog.craw.download.proxies import Proxies
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
        request = requests.get(url, headers=headers, proxies=proxies_dic)  # , proxies=proxies
        return request


if __name__ == '__main__':
    # url = "http://travel.qunar.com/space/follow/list?userId=158928832" # 待连接的url
    url = 'http://www.sogou.com'
    proxies_dic = get_proxies_dic()
    headers = get_headers
    down = Downloader()
    req = down.download_using_requests(url)
    print(req.text)