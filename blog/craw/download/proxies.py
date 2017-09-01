# coding:utf8
import requests
from bs4 import BeautifulSoup
from blog.craw.download.constants import get_headers
import time
import json
import random
import re
from bs4 import Tag


# url = url = 'http://www.66ip.cn/'
# 写proxies 到文件中
def get_proxies_ip():
    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2; pt-br) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13',}
    final_ip = []
    for x in range(1, 1000):
        url_s = 'http://www.66ip.cn/%s.html' % x
        t = requests.get(url_s, headers=headers)
        t.encoding = 'gb2312'
        content = t.text
        if content is not None:
            soup = BeautifulSoup(content, "html.parser")
            ip_table = soup.find('table', width='100%')
            if ip_table is not None:
                for ip_tr in ip_table:
                    if ip_tr is not None and type(ip_tr) == Tag:
                        ip_pos = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip_tr.prettify())
                        ip_port = re.search('(?<=  )\d+(?=\n)', ip_tr.prettify())
                        if ip_pos is not None and ip_port is not None:
                            li_ip = ip_pos.group(0) + ':' + ip_port.group(0)
                            print(li_ip)
                            final_ip.append(li_ip)
                            # print(ip_tr)

    # 将list对象序列化为json文件
    json_obj = json.dumps(final_ip)
    print('json', json_obj)
    file = open('./proxies_list.json', 'w+')
    file.write(json_obj)
    file.close()
    return final_ip


# 测试连通性
def get_ping():
    file = open('./proxies_list.json', 'r+')
    json_obj = json.loads(file.read())
    print("原始ip地址长度", len(json_obj))
    for li_ip in json_obj:
        dic = {'http': li_ip}
        try:
            req = requests.get('https://www.sogou.com/', headers=get_headers, proxies=dic)
            print('正在测试代理',dic)
        except Exception:
            print('连接出错了')
            json_obj.remove(li_ip)
    print(len(json_obj))
    print(json_obj)


class Proxies(object):
    def get_random_proxie(self):
        file = open('./proxies_list.json', 'r')
        rt = file.read()
        js_list = json.loads(rt)
        js = js_list.__getitem__(random.randint(0, len(js_list) - 1))
        return js


if __name__ == '__main__':
    # url = 'http://www.66ip.cn/'
    # get_proxies_ip()
    # pro = Proxies()
    # print(pro.get_random_proxie())
    get_ping()
