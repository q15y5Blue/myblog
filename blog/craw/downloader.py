# coding : utf8
import urllib.request as urllib2


class Downloader:
    def download_html_by_url(self, url):
        request = urllib2.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response = urllib2.urlopen(request)
        if (response.getcode()==200):
            return response.read().decode('utf-8')
        else :
            return None