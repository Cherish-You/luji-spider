# coding=utf-8
from urllib import request
import urllib
import re
import chardet

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" size'
    imgre = re.compile(reg)
    encode_type = chardet.detect(html)
    html = html.decode(encode_type['encoding'])
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

# dowmload pictures from website
html = getHtml("https://tieba.baidu.com/p/5230780089")
print (getImg(html))
