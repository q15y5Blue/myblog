# coding : utf8
import urllib.request as urllib2
import requests
from .user_agent import user_agent

class Downloader:

    def download_html_by_url(self,url):
        return self.dowload_using_requests(url)

    def download_json_by_url(self, url):
        req = requests.get(url)
        if req.status_code == 200:
            return req.json()
        else:
            return None


    def download_using_urllib(self, url ):
        request = urllib2.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response = urllib2.urlopen(request)
        if (response.getcode() == 200):
            return response.read().decode('utf-8')
        else:
            return None

    def dowload_using_requests(self, url):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Host": "travel.qunar.com",
            "Upgrade-Insecure-Requests:": 1,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        }
        req = requests.get(url, headers)
        if req.status_code == 200:
            return requests.get(url, headers).text
        else:
            return None

if __name__ == '__main__':
    url = "http://travel.qunar.com/space/follow/list?userId=158928832"
    proxie = {
        'http': 'http://160.16.94.228:80'
    }
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Host": "travel.qunar.com",
        "Upgrade-Insecure-Requests:": 1,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    }
    request = requests.get(url,header)
    print(request.text)
    print(request.headers)