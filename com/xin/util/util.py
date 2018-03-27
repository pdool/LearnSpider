#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os


# 检查文件夹
def checkFolder(folderName):
    # 判断文件夹是否存在
    if not os.path.exists(os.path.join(os.getcwd(), folderName)):
        # 新建文件夹
        os.mkdir(os.path.join(os.getcwd(), folderName))
    pass
