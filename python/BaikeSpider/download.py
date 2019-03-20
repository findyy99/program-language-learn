# -*- coding: UTF-8 -*-
import requests
class Downloader():
    def __init__(self,url):
        self.url = url
    def GetHtml(self):
        data = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'}
        try:
            r = requests.get(self.url,headers=data)
            r.encoding = 'utf-8'
        except:
            print('未找到该页面')
        else:
            return r  #返回get的对象
if __name__ == '__main__':
    s = Downloader('https://baike.baidu.com/item/Python/407313')
    with open('1.txt','w+') as f:
        f.write(s.print_3().text)
        f.close()