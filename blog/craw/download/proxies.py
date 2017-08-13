# coding:utf8
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import time
from blog.craw.download.constants import headers
import json
import socket

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
        print('初始ip_list 长度:', len(final_ip))
        final_ip = get_ping(ip_list=final_ip)
        print('处理过后的ip_list 长度:', len(final_ip))

        json_obj = json.dumps(final_ip)
        print('json', json_obj)
        file = open('./proxies_list.json', 'w+')
        file.write(json_obj)
        file.close()
        return final_ip

def get_ping(ip_list):

    for ip in ip_list:
        index = ip.index(':')
        print('正在读取ip地址：', ip[0:index])
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            data = s.connect((ip[0:index], 80))
            if data is None:
                print('这应该是个正常的ip', ip)
            else:print(data)
        except ConnectionRefusedError:
            ip_list.remove(ip)
            print('连接有问题,有问题的ip是', ip)
        except socket.timeout:
            ip_list.remove(ip)
            print('连接超时,超时的ip是', ip)
    return ip_list


if __name__ == '__main__':
    get_proxies_ip(r'http://www.goubanjia.com/free/index.shtml')
    # get_ping()