# coding:utf8
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import time
import json
import socket
import random

from blog.craw.download.constants import get_headers


# url =http://www.goubanjia.com/free/index.shtml
# 写proxies 到文件中
def get_proxies_ip(url):
    t = requests.get(url, headers=get_headers)
    content = t.text
    if content is not None:
        soup = BeautifulSoup(content, "html.parser")
        td_list = soup.find_all('td', 'ip')
        final_ip = []
        print(td_list)
        for td_li in td_list:  # 对td单元格进行处理
            list_before_done = []  # 处理之前的数
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

        print('初始ip_list 长度:', len(final_ip))
        final_ip = get_ping(ip_list=final_ip)
        print('处理过后的ip_list 长度:', len(final_ip))

        json_obj = json.dumps(final_ip)
        print('json', json_obj)
        file = open('./proxies_list.json', 'w+')
        file.write(json_obj)
        file.close()

        return final_ip

# 测试连通性
def get_ping(ip_list):
    # 这一步待解决
    return ip_list


class Proxies(object):
    def get_random_proxie(self):
        file = open('./proxies_list.json', 'r')
        rt = file.read()
        js_list = json.loads(rt)
        js = js_list.__getitem__(random.randint(0, len(js_list) - 1))
        return js


if __name__ == '__main__':
    pass
    # pro = Proxies()
    # print(pro.get_random_proxie())
