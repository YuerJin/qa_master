import base64
import datetime
import hashlib
import hmac
import json
import urllib

import requests
import yaml

from test_Case.test_tmp.comm_token import Comm_Token

TIMEOUT = 5


# 各种请求，获取数据方式
# get
def http_get_request(url, params, add_to_headers=None):
    token = Comm_Token()
    qa_toekn = token.get_token("372863")  # qa环境，替换自己的uid
    # qa_toekn = token.get_token("")  # qa环境，替换自己的uid
    headers = {'Accept-Language': 'en-US',
              "Authorization": qa_toekn
              };

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
    token = Comm_Token()
    qa_toekn = token.get_token("372863")  # qa环境，替换自己的uid
    headers = {'Accept-Language': 'en-US',
              "Authorization": qa_toekn
              };

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
