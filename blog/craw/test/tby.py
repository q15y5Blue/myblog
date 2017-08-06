# -*- coding: utf-8 -*-
# 这是个有BUG 的代码
import string
import urllib.request as urllib2


def baidu_tieba(url, begin_page, end_page):
    for i in range(begin_page, end_page + 1):
        sName = string.zfill(i, 5) + '.html'
        print('正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......')
        f = open(sName, 'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()

        # bdurl = 'http://tieba.baidu.com/p/2296017831?pn='


# iPostBegin = 1
# iPostEnd = 10

bdurl = u'http://tieba.baidu.com/p/5255364133?pn='
begin_page = 1
end_page = 2

baidu_tieba(bdurl, begin_page, end_page)