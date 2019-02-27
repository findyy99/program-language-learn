import requests
from bs4 import BeautifulSoup
import time
import re
def geturl():       #get电影地址和名称
    url = 'http://www.dytt8.net/'      #初始url
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'      #伪装headers
    headers = {'User-Agent':user_agent}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,'html.parser',from_encoding='gb18030')        #soup解析
    titles = soup.find_all('td')        #寻找td标签
    global list_name,list_url           #定义全局变量存储电影地址和名称
    list_url = []                       #创建列表以存储电影详细的URL
    list_name = []                      #存储电影名称
    for title in titles:                                #提取所需的网址和名称
        for n in title.find_all('a', href=re.compile('^/html/gndy/dyzz/201')):
            list_url.append('https://www.dytt8.net'+n.get('href'))
            list_name.append(n.string)
def get_dlurl():     #get下载链接
    global downloads
    downloads = []
    useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
    headers = {'User-Agent':useragent}
    for url in list_url:
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.content,'html.parser',from_encoding='gb18030')
        dlurls = soup.find_all('a')
        list = []
        for dlurl in dlurls:
            if 'magnet' in str(dlurl):
                list.append(dlurl)
                downloads.append('种子链接： '+dlurl.get('href'))
                print('getting download url')
def main():
    geturl()
    get_dlurl()
    for (name,download) in zip(list_name,downloads):
        with open('result.txt','a+') as file:
            file.write('电影名称: '+name+'\n'+download + '\n')
        time.sleep(1)
        print('writing the file')
    print('Done, please open the result.txt.')
main()