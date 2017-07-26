# coding : utf8
import urllib.request as urllib2
import requests

class Downloader:

    def download_html_by_url(self, url):
        request = urllib2.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response = urllib2.urlopen(request)
        if (response.getcode()==200):
            return response.read().decode('utf-8')
        else:
            return None

    def download_json_by_url(self, url):
        req = requests.get(url)
        if req.status_code == 200:
            return req.json()
        else:
            return None
