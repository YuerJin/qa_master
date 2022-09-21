import yaml,json
import requests as r
from test_Case.test_tmp.comm_token import Comm_Token
from common.comm_http import http_get_request,http_post_request

class QaZhuanti():
    env_url = yaml.safe_load(open("/Users/weijinyu/Desktop/AAX/qa-master/config/basic_config.yaml"))['env_info']['qa_url']

    #web-热门专题列表/common/v2/series/list
    def getList(self,type,lang='zh-TW',limit=10,page=0):
        params = {}
        if type:
            params['type'] = type
        if lang:
            params['lang'] = lang
        url = self.env_url + '/common/v2/series/list'
        res = http_get_request(url,params).json()
        print("热门专题列表：\n" + json.dumps(res,ensure_ascii=False))

    #web-热门专题详情/series/detail
    # 活动状态：status 1-进行中 2-未开始 3-已结束
    def getDetail(self,id,status,lang='zh-TW'):
        params = {}
        if id:
            params['id'] = id
        if status:
            params['status'] = status
        if lang:
            params['lang'] = lang
        url = self.env_url + '/common/v2/series/detail'
        # res = http_get_request(url,params).json()
        res =http_get_request(url,params).json()

        print("热门专题详情:\n",json.dumps(res,ensure_ascii=False))

    #web-热门专题活动列表/series/activities
    # 状态：status:1 - 进行中  2 - 未开始 3 - 已结束
    def getActivity(self,seriesId,status,lang='zh-TW'):
        params = {}
        if seriesId:
            params['seriesId'] = seriesId
        if status:
            params['status'] = status
        if lang:
            params['lang'] = lang
        url = self.env_url + '/common/v2/series/activities'
        res = http_get_request(url,params).json()

        print("热门活动专题列表： \n" + json.dumps(res,ensure_ascii=False))

    #admin-

if __name__== '__main__':
    # list= QaZhuanti()
    # list.getList(type='activity',lang='en-US')

    detail = QaZhuanti()
    # detail.getDetail(id="62fafc291d482700de01e4f5",status="")
    detail.getDetail(id="62fcbd15b6d95900b72b42d9",status=3)
    #
    # activity = QaZhuanti()
    # activity.getActivity(seriesId="62fb58bb1783e80095945387",status=3)