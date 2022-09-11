# `ripcaptcha`
`ripcaptcha` is an **open source** python-based [captcha.rip](https://captcha.rip) api wrapper. 

## Table of Contents

* [Examples](#Examples)
* [Documentation](#documentation)

## Examples
### Solving a captcha
```python
token = ripcaptcha.FunCaptchaTaskProxyless(
    siteurl="https://www.roblox.com/",
    serviceurl="https://roblox-api.arkoselabs.com/",
    publickey="A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F",
    key='01191ab71d4b4ceda5a9ae21542566df',
    blob=blob
)
```
```json
{"message": "solved", "token": "334631e2b9087f0a9.1702353901|r=us-east-1|metabgclr=transparent|guitextcolor=%23474747|maintxtclr=%23b8b8b8|metaiconclr=%23757575|meta=3|lang=en|pk=A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F|at=40|ht=1|ag=101|cdn_url=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-us-east-1.arkoselabs.com|surl=https%3A%2F%2Froblox-api.arkoselabs.com|smurl=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager"}
```
### Solving a captcha with a proxy
```python
token = ripcaptcha.FunCaptchaTask(
    siteurl="https://www.roblox.com/",
    serviceurl="https://roblox-api.arkoselabs.com/",
    publickey="A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F",
    key='01191ab71d4b4ceda5a9ae21542566df',
    blob=blob,
    proxy="ip:port:user:pass"
)
```
```json
{"message": "solved", "token": "334631e2b9087f0a9.1702353901|r=us-east-1|metabgclr=transparent|guitextcolor=%23474747|maintxtclr=%23b8b8b8|metaiconclr=%23757575|meta=3|lang=en|pk=A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F|at=40|ht=1|ag=101|cdn_url=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-us-east-1.arkoselabs.com|surl=https%3A%2F%2Froblox-api.arkoselabs.com|smurl=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager"}
```
### Obtaining a blob and solving a captcha
```py
from ripcaptcha import ripcaptcha
import time
import requests

def csrf():
    return requests.post('https://catalog.roblox.com/v1/catalog/items/details').headers['x-csrf-token']

def registerinfo():
    cdetails = requests.post("https://auth.roblox.com/v2/signup", headers={"x-csrf-token":csrf(), "User-Agent":"Mozilla/5.0 (Windows; U; Windows CE) AppleWebKit/534.47.7 (KHTML, like Gecko) Version/4.1 Safari/534.47.7"}, json={"username":"fsdhfkshdfk123","password":"WE*@*!&EUAHUISFHS","birthday":"1962-04-08T23:00:00.000Z","gender":2,"isTosAgreementBoxChecked":True,"agreementIds":["848d8d8f-0e33-4176-bcd9-aa4e22ae7905","54d8a8f0-d9c8-4cf3-bd26-0cbf8af0bba3"]})
    return cdetails.json()["errors"][0]["fieldData"].split(",")[0], cdetails.json()["errors"][0]["fieldData"].split(",")[1]
        
cid, blob = registerinfo()
token = ripcatcha.FunCaptchaTaskProxyless(
    siteurl="https://www.roblox.com/",
    serviceurl="https://roblox-api.arkoselabs.com/",
    publickey="A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F",
    key='db31742e2ffd442e85653b891d1473af',
    blob=blob
)
if token['message'] == 'solved':
    print(token['token'])
else:
    print("error", token)
```
```
334631e2b9087f0a9.1702353901|r=us-east-1|metabgclr=transparent|guitextcolor=%23474747|maintxtclr=%23b8b8b8|metaiconclr=%23757575|meta=3|lang=en|pk=A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F|at=40|ht=1|ag=101|cdn_url=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-us-east-1.arkoselabs.com|surl=https%3A%2F%2Froblox-api.arkoselabs.com|smurl=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager
```
## Documentation
#### ```FunCaptchaTaskProxyless```: siteurl, serviceurl, publickey, key, delay=1, useragent, blob
#### ```FunCaptchaTask```: siteurl, serviceurl, publickey, key, proxy, delay=1, useragent, blob
