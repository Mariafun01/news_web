'''
新浪新闻：http://news.sina.com.cn/society/
Date：20180920
Author：lizm
Description：获取新浪新闻
'''
import requests
from bs4 import BeautifulSoup
from urllib import request
from lxml import etree
import sys
import re
import os

def getNews(title,url,m):
    Hostreferer = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    req = request.Request(url)
    response = request.urlopen(req)
    #过滤非utf-8的网页新闻
    response = response.read().decode('utf-8',"ignore")
    soup = BeautifulSoup(response,'lxml')
    tag = soup.find('div',class_='article')
    if tag == None:
        return 0
    #获取文章发布时间
    fb_date = soup.find('div','date-source').span.string
    #获取发布网站名称
    fb_www= soup.find('div','date-source').a.string
    #获取文章内容
    rep = re.compile("[\s+\.\!\/_,$%^*(+\"\']+|[+<>?、~*（）]+")
    title = rep.sub('',title)
    title = title.replace(':','：')
    filename = sys.path[0]+"/news/"+title+".txt"
    with open(filename,'w',encoding='utf8') as file_object:
        file_object.write(fb_date + " " + fb_www)
        file_object.write("\n")
        file_object.write("网址:"+url)
        file_object.write("\n")
        file_object.write(title)
        file_object.write(tag.get_text())

    i = 0
    for image in tag.find_all('div','img_wrapper'):
        title_img = title +str(i)
        #保存图片
        #判断目录是否存在
        if (os.path.exists(sys.path[0]+"/news/"+title)):
            pass
        else:
            #不存在，则新建目录
            os.mkdir(sys.path[0]+"/news/"+title)
        os.chdir(sys.path[0]+"/news/"+title)
        file_name = "http://news.sina.com.cn/"+image.img.get('src').replace('//','')
        html = requests.get(file_name, headers=Hostreferer)
        # 图片不是文本文件，以二进制格式写入，所以是html.content
        title_img = title_img +".jpg"
        f = open(title_img, 'wb')
        f.write(html.content)
        f.close()
        i+=1
    print('成功爬取第', m,'个新闻',title)
    return 0

#获取社会新闻（最新的162条新闻）
def getTitle(url):
    req = request.Request(url)
    response = request.urlopen(req)
    response = response.read().decode('utf8')
    soup = BeautifulSoup(response,'lxml')
    y = 0
    for tag in soup.find('ul',class_='seo_data_list').find_all('p'):

        if tag.a != None:
            #if y== 27:
            print(y,tag.a.string,tag.a.get('href'))
            temp = tag.a.string
            getNews(temp,tag.a.get('href'),y)
            y += 1

if __name__ == '__main__':
    url = 'http://news.sina.com.cn/society/'
    getTitle(url)