#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import re
import requests

from com.xin.util import util

folderName = "download"
urlPath = "http://www.xiaohuar.com/p/suyan/index.html"


def SaveImage(url, name):

    fpath = os.path.join(folderName, name)
    response = requests.get( 'http://www.xiaohuar.com/d/file/' + url).content
    # 写入图片
    with open(fpath + '.jpg', 'wb+') as f:
        f.write(response)


def startRead():
    # 请求页面
    urlPathLoacl = urlPath
    for i in range(1,13):
        page = requests.get(urlPathLoacl)

        urlPathLoacl = "http://www.xiaohuar.com/p/suyan/index_"+str(i)+".html"
        # 设置编码
        page.encoding = 'gbk'
        # 正则获取图片集合
        imglist = re.findall('alt="(.*?)" src="/d/file/(.*?\.jpg)"', page.text)
        # 循环保存图片
        for name, url in imglist:
            print(url, name)
            SaveImage(url,name)





if __name__ == '__main__':

    util.checkFolder(folderName)
    startRead()

    pass

# 1、学习requests

    # r.text 返回headers中的编码解析的结果，可以通过r.encoding = 'gbk'来变更解码方式
    # r.content返回二进制结果


# 2、re正则表达式