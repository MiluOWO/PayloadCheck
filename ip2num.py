import requests
import re 
session = requests.session()
c = list()
for i in range(2,66):

	burp0_url = "http://ip/admin/users/"+str(i)
	burp0_cookies = {"session": "62f9e69b-e995-4a7d-9f20-9897ccbe38b0"}
	burp0_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
	a = session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
	b=re.findall(r'(?:\d{1,3}\.){3}\d{1,3}',a.text)
	if(b!=[]):
		c.append(str(i)+'->'+str(b))

print(c)