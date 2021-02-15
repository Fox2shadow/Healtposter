## Healtposter 体温上报助手

(适用于 唐山市师生健康大数据系统 )

### 参数介绍

---

```json
{
	"userId": "",
	"reportTime": "",
	"temperature": "",
	"selfHealthy": "",
	"familyHealthy": "",
	"helpMethed": "",
	"testPerson": ""
}
```

1. **上报人 (id)**

2. **上报日期**

   格式：yyyy-mm-dd

3. **体温**

   格式：xx.x

4. **检测人**

5. **是否出现下列四种情况？(默认无)**

   A.确诊 B.疑似 C.密切接触者 D.发热人员 E.无

6. **你的家人朋友是否出现下列四种情况？(默认无)**

   A.确诊 B.疑似 C.密切接触者 D.发热人员 E.无

7. **救助及防护措施 (默认无)**

   A.住院治疗 B.定点隔离 C.无

---
### 使用说明
运行
```shell
python3 healtposter.py
```

使用
```shell
日期： 2021-XX-XX, XX:XX
体温： 
```
输入体温后回车即可，之后会返回提交状态。
提交成功 或 今天已经提交过了。




(后续功能开发中。)
---
<u>Copyright (c) 2018 NeTFox. power by ALex Zerkio.</u>
