# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import urllib
class Parser():
    def __init__(self,html):
        self.html = html
    def ReturnUrl(self):                        #此函数返回页面的URL
        try:
            soup = BeautifulSoup(self.html.text,'html.parser')
        except:
            print('error')
        l = []
        try:
            titles = soup.find('h1')
            urls = soup.find_all('a',target='_blank')
        except:
            print('not found')
        else:
            for url in urls:                    #判断URL href属性，正则不太会，多个if代替
                if 'item' in url['href']:
                    if 'https:' in url['href'] and 'http:' not in url['href']:
                        l.append(urllib.parse.unquote(url['href']))
                    elif 'http:' in url['href']:
                        pass                    #百度貌似不支持http访问
                    else:
                        l.append('https://baike.baidu.com'+urllib.parse.unquote(url['href']))
            return l

    def ReturnTitle(self):                      #此函数返回页面的title
        soup = BeautifulSoup(self.html.text, 'html.parser')
        a = ''
        try:
            titles = soup.find('h1')
            contents = soup.find_all('div',class_='para')
        except:
            print('not found title')
        else:
            a=[]                             #这儿本来是想把title的相关内容做下来，感觉水平不行，没完成
            for i in contents[1]:
                try:
                    a.append(i.string)
                except:
                    a.append(i)
            return titles.string                #此处仅返回title
if __name__ == '__main__':
    print('1')