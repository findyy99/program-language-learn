dict1 = {'翠一教':'001',
         '翠二教':'002',
         '翠三教':'003',
         '翠四教':'004',
         '翠五教':'005',
         '翠六教':'006',
         '翠七教':'007',
         '翠八教':'008',
         '翠九教':'009',
         '翠十教':'010',
         '翠十一教':'011',
         '翠十二教':'012',
         '风雨操场(翡翠湖校区)':'030',
         '4＃实验楼(翡翠湖校区)':'040',
         '地质基础实验室':'041',
         '3#实验楼(翡翠湖校区)':
         '042','机房(翡翠湖校区)':
         '043','东楼(南校区)':'050',
         '西楼(南校区)':'051',
         '主楼(南校区)':'052',
         '西二(南校区)':'053',
         '电教楼(南校区)':'054',
         '逸夫楼(南校区)':'055',
         '操场(南校区)':'056',
         '其他(其他)':'999',
         }
for i in dict1.items():
    print(i)
import requests
from bs4 import BeautifulSoup
requests = requests.session()
def login():
    url1 = 'http://bkjw.hfut.edu.cn/pass.asp'
    data1 = {'UserStyle':'OtherUser',
        'user':'JSCX02',
        'password':'abc123'}
    response1 = requests.post(url1,data = data1)
def getclass():
    url2 = 'http://bkjw.hfut.edu.cn/OtherUser/asp/m_webkxjscx_1.asp'
    data2 = {'jyz':input('请输入教学周:\n'),'jxldm':input('请输入查询的教学楼代码:\n'),'lcdm':input('请输入要查询的楼层:\n'),'jslxdm':'00','jsrl':input('请输入教室容量(163,132,120,76,68,46,36):\n'),'zjjy':input('请输入查询日期(例如：周一：输入 1):\n'),'jyjc':'1','jyjc':'2','jyjc':'3','jyjc':'4','jyjc':'5','jyjc':'6','jyjc':'7','jyjc':'8','jyjc':'9','jyjc':'10'
             }
    response2 = requests.post(url2,data = data2)
    soup = BeautifulSoup(response2.text,'html.parser')
    print(response2.text)
    tags = soup.find_all('td')
    value = []
    for tag in tags:
        value.append(tag.string)
    value1 = value[8:]
    print('你查询的时间段有如下教室空闲:\n')
    try:
        for i in range(len(value1)):
            if i%5 == 0:
                value2 = value1[i:i+5]
                print("   {:^3}\t{:^3}\t{:^3}\t{:^3}\t{:^3}".format(value2[0],value2[1],value2[2],value2[3],value2[4]))
            else:
                i = i+1
    except:
        print( '    gg ','         gg','      gg','      gg','   gg')
def main():
    login()
    getclass()
main()
