# coding:utf8
class UrlManage:
    def __init__(self):
        self.oldUrls = set()
        self.newUrls = set()

    # ！=0的时候返回true
    def has_new_url(self):
        return len(self.newUrls) != 0

    # 获取新的url
    def get_new_url(self):
        new_url = self.newUrls.pop()
        self.oldUrls.add(new_url)
        return new_url

    # 添加新url
    def add_new_url(self,url):
        if url is None :
            return
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)

    # url list added
    def add_new_url_list(self, url_list):
        if len(url_list) == 0 or url_list is None:
            return
        for url in url_list:
            # http://travel.qunar.com/space/follow/list?userId=158928832
            strs = "http://travel.qunar.com/space/follow/list?userId=%s" % url
            self.add_new_url(strs)
