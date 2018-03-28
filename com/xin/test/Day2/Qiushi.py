#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

import os

from com.xin.util import util

startUrl = "https://www.qiushibaike.com/text/"
folderName = "txts"

def isText(tag):
    return tag.name == 'div' and 'class' in tag.attrs and tag.attrs['class'][0] == "content"

def isContent(tag):
    return tag.name == 'a' and tag.name == 'a' and 'class' in tag.attrs and tag.attrs['class'][0] == "contentHerf"


def saveText(item):
    fpath = os.path.join(folderName, "qiushibaike.txt")
    # 写入图片
    with open(fpath, 'a+',encoding='utf-8') as f:
        f.write(item)
    pass


def readOneItem(param):
    url = 'https://www.qiushibaike.com' + param
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    items = soup.find(isText)

    saveText(items.text)
    pass


def readPage(page):
    # 设置编码
    soup = BeautifulSoup(page.text, "html.parser")
    items = soup.find_all(isContent)

    for item in items:
        readOneItem(item['href'])
    pass


def startRead():

    # 请求页面
    urlPathLoacl = startUrl
    for i in range(1, 13):
        page = requests.get(urlPathLoacl)
        readPage(page)

    pass


if __name__ == '__main__':
    util.checkFolder(folderName)

    startRead()
    print("OK")
    pass
