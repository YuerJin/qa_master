import base64
import datetime
import hashlib
import hmac
import json
import urllib

import requests

TIMEOUT = 5


# 各种请求，获取数据方式
# get
def http_get_request(url, params, add_to_headers=None):
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept-Language": "zh-CN",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }

    if add_to_headers:
        headers.update(add_to_headers)
    data = urllib.parse.urlencode(params)
    try:
        response = requests.get(url, data, headers=headers, timeout=TIMEOUT)
        if response.status_code == 200:
            return response
        else:
            return {"status": "fail"}
    except Exception as e:
        print(f"httpGet failed,detail is {e}")
        return {"status": "fail", "msg": f"{e}"}


# post
def http_post_request(url, params, add_to_headers=None):
    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }
    if add_to_headers:
        headers.update(add_to_headers)
    postdata = json.dumps(params)
    try:
        response = requests.post(url, postdata, headers=headers, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        print(f"httpPost failed,details is {e}")
        return {"status": "fail", 'msg': f'{e}'}


def api_key_get(url, request_path, params, ACCESS_KEY, SECRET_KEY):
    method = 'GET'
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dt%H:%M:%S')
    params_to_sign = {
        'AccessKeyId': ACCESS_KEY,
        'SignatureMethod': 'HmacSHA256',
        'SignatureVersion': '2',
        'Timestamp': timestamp
    }
    host_url = url
    host_name=urllib.parse.urlparse(host_url).hostname
    host_name=host_name.lower()
    params_to_sign['Signature']=createSign(params,method,host_name,request_path,SECRET_KEY)
    url=host_url+request_path
    return http_get_request(url,params)


def createSign(pParams,method,host_url,request_path,secret_key):
    sorted_params =sorted(pParams.items(),key=lambda d:d[0],reverse=False)
    encode_params=urllib.parse.urlencode(sorted_params)
    payload=[method,host_url,request_path,encode_params]
    payload='\n'.join(payload)
    secret_key=secret_key.encode(encoding='UTF8')
    digest=hmac.new(secret_key,payload,digestmod=hashlib.sha256).digest()
    signature=base64.b64decode(digest)
    signature=signature.decode()
    return signature


