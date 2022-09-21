from jsonpath import jsonpath
import yaml
from common.uitl_http import http_post_request

class ContractPost():
    env_url=yaml.safe_load(open("../config/basic_config.yaml"))['env_info']['api_url']

    # 获取账户总资产估值
    def contract_balance(self,valuation_asset='BTC'):
        params={"valuation_asset":'BTC'}
        if valuation_asset:
            params['valuation_asset']=valuation_asset
        url=self.env_url+'/api/v1/contract_balance_valuation'
        r=http_post_request(url=url,params=params)
        # print(r)
        # print(jsonpath(r, '$..status'))
        return jsonpath(r,'$..status')

if __name__=='__main__':
    info=ContractPost()
    info.contract_balance('')



