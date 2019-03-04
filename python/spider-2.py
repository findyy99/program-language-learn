import re
import requests
from bs4 import BeautifulSoup
def get_content(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'}
        r = requests.get(url,headers=headers)
        r.status_code
        r.encoding = 'gbk'
        return r.text
    except:
        print('访问出错了')
def get_url(url):
    html = get_content(url)
    soup = BeautifulSoup(html,'html.parser')
    urls = soup.find('ul', class_='picList clearfix')
    url = urls.find_all('li')
    for i in url:
        img_url = i.find('img')['src']
        name = i.find('span',class_='sTit').text
        try:
            time = i.find('span',class_='sIntro').text
        except:
            time = '暂无上映日期'
        if i.find_all('p',class_='pTxt pIntroHide'):
            intro = i.find_all('p',class_='pTxt pIntroHide')
            for i in intro:
                a=(str(i).index('M')) - 11
            intro = str(i)[48:a]
        else:
            intro = i.find('p',class_='pTxt pIntroShow').string
        actors = i.find('p',class_="pActor")
        act = ''
        if actors:
            for actor in actors.contents:
                act += actor.string + ' '
        with open('result.txt','a+') as file:
            file.write("片名：{}\n{}\n{}\n{} \n \n".format(name, time, act, intro))
        with open('/Users/jianzhao/Desktop/img/' + name + '.png', 'wb+') as f:
            f.write(requests.get('http:'+img_url).content)


def main():
    url = 'http://dianying.2345.com/top/'
    get_url(url)

if __name__ == '__main__':
    main()
