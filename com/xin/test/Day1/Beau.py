#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

import os

from com.xin.util import util

folderName = "download"
urlPath = "http://www.xiaohuar.com/p/suyan/index.html"


def SaveImage(index, url, name):
    if name == '点击这里给我发消息':
        return

    fpath = os.path.join(folderName, name)
    response = requests.get('http://www.xiaohuar.com/d/file/' + url).content
    # 写入图片
    with open(fpath + str(index) + '.jpg', 'wb+') as f:
        f.write(response)
    print(name + str(index))


def hasAlt(tag):
    rs = tag.name == 'img' and tag.has_attr('alt')
    return rs


def startRead():
    # 请求页面
    urlPathLoacl = urlPath
    index = 1
    for i in range(1, 13):
        page = requests.get(urlPathLoacl)
        urlPathLoacl = "http://www.xiaohuar.com/p/suyan/index_" + str(i) + ".html"
        # 设置编码
        page.encoding = 'gbk'
        soup = BeautifulSoup(page.text, "html.parser")
        imgs = soup.find_all(hasAlt)
        for img in imgs:
            name = img.attrs['alt']
            dir = img.attrs['src']
            imgPath = dir[dir.rfind("/")+1:len(dir)]
            SaveImage(index, imgPath, name)
            index = index + 1

    print("结束")


if __name__ == '__main__':
    util.checkFolder(folderName)
    startRead()
    pass
# 只是练习了bs的查找