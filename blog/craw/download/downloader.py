# coding : utf8
import requests
import random


from blog.craw.download.constants import get_file_proxies

from blog.craw.download.constants import headers

class Downloader:
    # using

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
    def download_using_requests(self, url):
        # proxies_url = 'http://www.goubanjia.com/free/index.shtml'
        # proxies_list = get_proxies_ip(proxies_url)
        proxies_list = get_file_proxies()
        # 使用代理连接
        proxies_http = {
            'http': proxies_list.__getitem__(random.randint(0, len(proxies_list) - 1))
        }
        # 使用代理连接
        proxies_https = {
            'https': proxies_list.__getitem__(random.randint(0, len(proxies_list) - 1))
        }
        try:
            request = requests.get(url, headers=headers, proxies=proxies_http)  # , proxies=proxies
        except requests.exceptions.ProxyError:
            request = requests.get(url, headers=headers, proxies=proxies_https)  # , proxies=proxies
        if request.status_code == 200:
            print(request.headers)
            return request.text
        else:
            return None

if __name__ == '__main__':
    url = "http://travel.qunar.com/space/follow/list?userId=158928832" # 待连接的url
    proxies_url = 'http://www.goubanjia.com/free/index.shtml' # 代理url
    proxies_list = get_file_proxies()
    proxies_http = {
        'http': proxies_list.__getitem__(random.randint(0, len(proxies_list)-1))
    }
    proxies_https = {
        'https': proxies_list.__getitem__(random.randint(0, len(proxies_list) - 1))
    }
    headers = headers
    try:
        request = requests.get(url, headers=headers, proxies=proxies_http) # , proxies=proxies
        print(request.status_code)
        print(request.text)
    except ConnectionError:
        pass



# if __name__ == '__main__':
#     url = r'http://travel.qunar.com/space/follow/list?userId=158928832'
#     down = Downloader()
#     html = down.download_html_by_url(url)
#     print(html)