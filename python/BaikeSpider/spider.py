# -*- coding: UTF-8 -*-
from manage import UrlManager           #从其他.py引入函数
from download import Downloader
from parse import Parser
class SpiderMain():
    def __init__(self,url):
        self.url = url
    def main(self):
        n=0                             #初始化，第一次运行函数
        dw = Downloader(self.url)
        dw.GetHtml()
        parser = Parser(dw.GetHtml())
        self.list = parser.ReturnUrl()
        urlMa = UrlManager(parser.ReturnUrl())
        while n<100:                    #此处开始循环
            crawingurl = urlMa.print_2()[0]
            print(crawingurl)
            dw = Downloader(crawingurl)
            dw.GetHtml()
            parser = Parser(dw.GetHtml())
            print(parser.ReturnTitle())
            urlMa = UrlManager(parser.ReturnUrl())
            n=n+1
url = 'https://baike.baidu.com/item/Python/407313'
my = SpiderMain(url)
my.main()
