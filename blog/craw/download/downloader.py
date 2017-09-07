# coding : utf8
import requests
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
        request = requests.get(url=url, headers=get_headers, proxies=proxies_dic)  # , proxies=proxies
        return request


if __name__ == '__main__':
    url = 'https://travel.qunar.com/space/follow/list?userId=158928832'
    down = Downloader()
    req = down.download_using_requests(url)
    print(req.text)