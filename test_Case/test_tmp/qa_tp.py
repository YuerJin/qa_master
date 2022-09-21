import yaml,json

from common.comm_http import http_get_request,http_post_request

class QaTp():
    env_url = yaml.safe_load(open("/config/basic_config.yaml"))['env_info']['qa_url']

    #划转
    def postPurse(self,quantity,currencyCode,fromPurseType,toPurseType):
        params = {}
        if quantity:
            params['quantity'] = quantity
        if currencyCode:
            params['currencyCode'] = currencyCode
        if fromPurseType:
            params['fromPurseType'] = fromPurseType
        if toPurseType:
            params['toPurseType'] = toPurseType

        url = self.env_url + '/common/v2/assets/purseTransfer'
        res = http_post_request(url,params).json()
        print("划转：\n" + json.dumps(res,ensure_ascii=False))

if __name__== '__main__':
    purse = QaTp()
    purse.postPurse()

