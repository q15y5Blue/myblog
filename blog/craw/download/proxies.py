# coding:utf8
import requests
from bs4 import BeautifulSoup
from blog.craw.download.constants import headers


# url =http://www.goubanjia.com/free/index.shtml
def get_proxies():
    pass


def parse_html(url):
    t = requests.get(url, headers=headers)
    content = t.text
    if content is not None:
        soup = BeautifulSoup(content, "html.parser")
        tds = soup.find_all('td', 'ip')
        for ip_str in tds:
            print(ip_str)
            real_ip = ip_str.find('span', 'display:inline-block;')
        print(tds)

if __name__ == '__main__':
    parse_html(r'http://www.goubanjia.com/free/index.shtml')