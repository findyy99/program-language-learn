import requests
from bs4 import BeautifulSoup
import time
def spider_1():
    url = 'http://www.ygdy8.net/'      #初始url
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'      #伪装headers
    headers = {'User-Agent':user_agent}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,'html.parser',from_encoding='gb18030')        #soup解析
    titles = soup.find_all('td')        #寻找td标签
    list = []                           #创建列表以存储电影详细的URL
    for title in titles:
        for n in title.find_all('a'):
            if '201902'and'gndy'and'dyzz' in str(n):
                if '2' in n.get('href'):
                    a.append('http://www.ygdy8.net'+n.get('href'))
            print('runing spider_1')
    return list
def spider_2(urls):
    global names
    names = []
    useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
    headers = {'User-Agent':useragent}
    for url in urls:
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.content,'html.parser',from_encoding='gb18030')
        head = soup.head.title.string
        names.append('电影名称: '+ head)
        print('runing spider_2')
def spider_3(urls):
    global downloads
    downloads = []
    useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
    headers = {'User-Agent':useragent}
    for url in urls:
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.content,'html.parser',from_encoding='gb18030')
        dlurls = soup.find_all('a')
        list = []
        for dlurl in dlurls:
            if 'magnet' in str(dlurl):
                list.append(dlurl)
                downloads.append('种子链接： '+dlurl.get('href'))
                print('runing spider_3')
def main():
    spider_2(spider_1())
    spider_3(spider_1())
    for (name,download) in zip(names,downloads):
        with open('result.txt','a+') as file:
            file.write(name+'\n'+download + '\n')
            time.sleep(2)
    print('Done')
main()