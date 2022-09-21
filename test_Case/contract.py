# import jsonpath as jsonpath
import yaml
from jsonpath import jsonpath
from common.uitl_http import http_get_request


# 合约市场行情
class Contract:
    env_url = yaml.safe_load(open("../config/basic_config.yaml"))['env_info']['api_url']
    print(env_url)

    # 获取合约信息
    def contract_info(self, symbol='', contract_type='', contract_code=''):
        params = {}
        if symbol:
            params['symbol'] = symbol
        if contract_type:
            params['contract_type'] = contract_type
        if contract_code:
            params['contract_code'] = contract_code
        url = self.env_url + '/api/v1/contract_contract_info'
        # return http_get_request(url,params)
        r = http_get_request(url, params)
        return jsonpath(r.json(), '$..contract_code')

    # 获取合约指数信息
    def contract_index(self, symbol=''):
        params = {}
        if symbol:
            params['symbol'] = symbol
        url = self.env_url + '/api/v1/contract_index'
        r = http_get_request(url, params)
        # return jsonpath(r.json(), '$..status')
        print(r)
        # print(jsonpath(r.json(), '$..status'))


if __name__ == '__main__':
    info = Contract()
    # info.contract_info()
    info.contract_index()
