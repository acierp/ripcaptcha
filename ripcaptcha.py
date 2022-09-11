import requests
import time

class ripcatcha:
    def FunCaptchaTaskProxyless(siteurl, serviceurl, publickey, key, delay=1, useragent=None, blob=None):
        solvej = {
        "key": key,
        "task": {
            "type": "FunCaptchaTaskProxyless",
            "site_url": siteurl,
            "public_key": publickey,
            "service_url": serviceurl,
        }
        }
        if blob: solvej['task']['blob'] = blob
        if useragent: solvej['task']['user_agent'] = useragent
        create = requests.post('https://captcha.rip/api/create', json=solvej)
        if not "id" in create.text:
            return {"message": "error creating task", "error": create.json()}
        checkj = {
            'key': key,
            'id': create.json()['id']
        }
        fetch = requests.post('https://captcha.rip/api/fetch', json=checkj)
        while fetch.json()['message'] == 'Processing':
            time.sleep(delay)
            fetch = requests.post('https://captcha.rip/api/fetch', json=checkj)
        if fetch.json()['message'] == 'Solved':
            return {"message": 'solved', 'token': fetch.json()['token']}
        else:
            return {"message": "failed to solve", "error": fetch.json()}

    def FunCaptchaTask(siteurl, serviceurl, publickey, key, proxy, delay=1, useragent=None, blob=None):
        if len(proxy.split(":")) == 4:
            ip, port, user, password = proxy.split(":")
        elif len(proxy.split(":")) == 2:
            raise("user:pass is currently unsupported by captcha.rip")
        else:
            raise('unsupported proxy type')
        solvej = {
        "key": key,
        "task": {
            "type": "FunCaptchaTask",
            "site_url": siteurl,
            "public_key": publickey,
            "service_url": serviceurl,
            "username": user,
            "password": password,
            "ip": ip,
            "port": port
        }
        }
        if blob: solvej['task']['blob'] = blob
        if useragent: solvej['task']['user_agent'] = useragent
        create = requests.post('https://captcha.rip/api/create', json=solvej)
        if not "id" in create.text:
            return {"message": "error creating task", "error": create.json()}
        checkj = {
            'key': key,
            'id': create.json()['id']
        }
        fetch = requests.post('https://captcha.rip/api/fetch', json=checkj)
        while fetch.json()['message'] == 'Processing':
            time.sleep(delay)
            fetch = requests.post('https://captcha.rip/api/fetch', json=checkj)
        if fetch.json()['message'] == 'Solved':
            return {"message": 'solved', 'token': fetch.json()['token']}
        else:
            return {"message": "failed to solve", "error": fetch.json()}
