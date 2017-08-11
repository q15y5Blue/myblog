# coding:utf8
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import time
from blog.craw.download.constants import headers


# url =http://www.goubanjia.com/free/index.shtml
def get_proxies():
    pass

# 抓取proxies 代理同时写入proxies_list 文件、
def get_proxies_ip(url):
    t = requests.get(url, headers=headers)
    content = t.text
    if content is not None:
        soup = BeautifulSoup(content, "html.parser")
        td_list = soup.find_all('td', 'ip')
        final_ip = []
        for td_li in td_list:  # 对td单元格进行处理
            list_before_done = [] # 处理之前的数
            list_new = []         # 处理之后的IP

            for li in td_li:
                if type(li) == Tag:
                    if li.prettify().__contains__('none') is False:
                        list_before_done.append(li)
                else:
                    list_before_done.append(li)
            for li in list_before_done:
                if type(li) == Tag:
                    list_new.append(li.text)
                else:
                    list_new.append(li)
            final_ip.append(''.join(list_new))
        time.sleep(1)
        print(final_ip)
        return final_ip

if __name__ == '__main__':
    get_proxies_ip(r'http://www.goubanjia.com/free/index.shtml')