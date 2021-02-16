# Copyright <c> 2018 NeTFoX
# Power by ALex Zerkio
#

import os
import requests
import json
import time

# 请求地址
url = "http://health.laotingedu.cn/api/services/app/organUser/SubmitUserHealth"

# 消息头
headers = {
        "Connection": "keep-alive",
        "Content-Length": "283",
        "Cache-Control": "max-age=0",
        "Origin":"http://health.laotingedu.cn",
        "Upgrade-Insecure-Requests":"1",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1901A Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36 MMWEBID/3390 MicroMessenger/8.0.1.1841(0x28000157) Process/tools WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
        "Accept": "*/*",
        "X-requested-With": "com.tencent.mm",
        "Referer": "http://health.laotingedu.cn/index.html?v=2.1",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": "Abp.Localization.CultureName=en-US; ASP.NET_SessionId=j54jt4uh4gjqgeewzcluyfyp; webToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoi5YiY5a6H6L2pIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiNmNhZWFiOWNhZTUxNDc2OWJlNWJmNTMyODZhZTg5ZTYiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL2FjY2Vzc2NvbnRyb2xzZXJ2aWNlLzIwMTAvMDcvY2xhaW1zL2lkZW50aXR5cHJvdmlkZXIiOiJBU1AuTkVUIElkZW50aXR5IiwiaHR0cDovL3d3dy5hc3BuZXRib2lsZXJwbGF0ZS5jb20vaWRlbnRpdHkvY2xhaW1zL3RlbmFudElkIjoiMSIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiODQ0NjIwOCIsInN1YiI6Ijg0NDYyMDgiLCJqdGkiOiI4MWQ0YmY0OS02YzE2LTQzYzMtODdiOC1lOWY3MzFiMzhlMjMiLCJpYXQiOjE2MTIxMDg3MDYsIm5iZiI6MTYxMjEwODcwNiwiZXhwIjoxNjQzNjQ0NzA2LCJpc3MiOiJIRjEwNDY3ODhMaSIsImF1ZCI6IkhGQ1l4MTA3ODkifQ.IHNjkO4bZQfpAe_yGggScU0HWTprym_MJaoZP3TYdvA",
        }

# title
localtime = time.localtime(time.time())
lotime = time.strftime("%H:%M", time.localtime(time.time()))
RPTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
print("日期：", RPTime, lotime)
temp = input("体温： ")

# 消息体
payload = {
        "id": 0,
        "userId": 000000,
        "reportTime": RPTime,
        "temperature": temp,
        "DoNucleicAcidTest": "否",
        "FirstResult": "",
        "SecondResult": "",
        "SelfCurrentArea": "否",
        "DoNucleicAcidTestReason": "",
        "selfHealthy": "无",  
        "familyHealthy": "无",
        "helpMethed": "无",
        "testPerson": "某某某",
        "status": 0,
        }

# 发送POST请求
rp = requests.post(url, json=payload, headers=headers,verify=False)

# 打印结果
if rp.json()["success"] == False:
    os.system("echo 状态： \033[31m今天已经提交过了\033[0m")
elif rp.json()["success"] == True:
    os.system("echo 状态： \033[32m提交成功\033[0m")





