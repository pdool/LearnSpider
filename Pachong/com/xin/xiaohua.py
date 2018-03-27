#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests,re,os

#文件夹名称
FileName= 'download'
#保存图片
def SaveImage(image,name="temp"):
    #图片存放路径
     fpath = os.path.join(FileName, name+'.jpg')
     response=requests.get("http://www.xiaohuar.com/d/file/"+image).content
     #写入图片
     with open(fpath+'.jpg', 'wb+') as f:
         f.write(response)

#获取当前页图片Url集合
def GetImage(fanyeUr):
    #请求页面
    page =requests.get(fanyeUr)
    #设置编码
    page.encoding='gbk'
    #正则获取图片集合
    imglist = re.findall('alt="(.*?)" src="/d/file/(.*?\.jpg)"', page.text)
    #循环保存图片
    for name,url in imglist:
        print(url,name)
        SaveImage(url,name)

#判断文件夹是否存在
if not os.path.exists(os.path.join(os.getcwd(), FileName)):
    #新建文件夹
    os.mkdir(os.path.join(os.getcwd(),FileName))

#请求第一页
fanyeUr='http://www.xiaohuar.com/p/suyan/index.html'
#循环翻页
for faye in range(1,13):
    #获取翻页Url
    GetImage(fanyeUr)
    fanyeUr='http://www.xiaohuar.com/p/suyan/index_%s.html' % faye