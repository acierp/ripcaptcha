# `ripcaptcha`
`ripcaptcha` is an **open source** python-based [captcha.rip](https://captcha.rip) api wrapper. 

## Table of Contents

* [Examples](#Examples)
* [Documentation](#documentation)

## Examples
### Solving a captcha
```python
token = ripcatcha.FunCaptchaTaskProxyless(
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
token = ripcatcha.FunCaptchaTask(
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
