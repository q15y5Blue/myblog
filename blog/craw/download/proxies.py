# coding:utf8
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from blog.craw.download.constants import headers


# url =http://www.goubanjia.com/free/index.shtml
def get_proxies():
    pass


def parse_html(url):
    t = requests.get(url, headers=headers)
    content = t.text
    if content is not None:
        soup = BeautifulSoup(content, "html.parser")
        td_list = soup.find_all('td', 'ip')
        for td_li in td_list:
            for li in td_li:
                new_tag = BeautifulSoup('')
                if type(li) == Tag:
                    if li.prettify().__contains__('none') is False:
                        new_tag.append(li)
                else:
                    if li.__contains__('none') is False:
                        new_tag.append(li)
                print(new_tag.text)
            # print(td_li.prettify())
if __name__ == '__main__':
    parse_html(r'http://www.goubanjia.com/free/index.shtml')