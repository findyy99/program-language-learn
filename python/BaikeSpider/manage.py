# -*- coding: UTF-8 -*-
import random
class UrlManager():
    def __init__(self,urls,list_1=[]):      #定义两个变量，urls是页面上刚爬取的。list_1是已存入的
        self.urls = urls
        self.nlist = list_1
    def print_2(self):                      #判断urls的URL是否已经存在
        for url in self.urls:
            if url in self.nlist:
                pass
            else:
                self.nlist.append(url)
        n = self.nlist.pop(random.randint(0,len(self.nlist)))    #随机取出某一个URL
        return [n,self.nlist]