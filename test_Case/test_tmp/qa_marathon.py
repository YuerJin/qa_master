import yaml, json
from common.comm_http import http_get_request, http_post_request


class QaMarathon():
    # /Users/weijinyu/Desktop/AAX/qa-master/config/basic_config.yaml
    env_url = yaml.safe_load(open("/Users/weijinyu/Desktop/AAX/qa-master/config/basic_config.yaml"))['env_info']['qa_url']
    env_url_admin = yaml.safe_load(open("/Users/weijinyu/Desktop/AAX/qa-master/config/basic_config.yaml"))['env_info']['qa_admin']

    # 【web/h5】获取马拉松详情/common/v2/marathon/detail
    def getDetail(self, name):
        params = {}
        if name:
            params['name'] = name

        url = self.env_url + '/common/v2/marathon/detail'
        res = http_get_request(url, params).json()
        print("马拉松详情:\n" + json.dumps(res, ensure_ascii=False))

    # 【web/h5】获取ticket记录 /common/v2/marathon/userRecordList
    def getUserrecordlist(self, name, page=0, limit=6):
        params = {}
        if name:
            params['name'] = name
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit

        url = self.env_url + '/common/v2/marathon/userRecordList'
        res = http_get_request(url, params).json()
        print("获取ticket记录:\n" + json.dumps(res, ensure_ascii=False))

    # 【web/h5】报名    /common/v2/marathon/join
    def postJoin(self, name):
        params = {}
        if name:
            params['name'] = name

        url = self.env_url + '/common/v2/marathon/join'
        res = http_post_request(url, params)
        print("报名:\n" + json.dumps(res, ensure_ascii=False))


    # 【web/h5】领取奖励 /common/v2/marathon/getRewards
    def postgetRewards(self, name, taskType, taskId):
        params = {}
        if name:
            params['name'] = name
        if taskType:
            params['taskType'] = taskType
        if taskId:
            params['taskId'] = taskId

        url = self.env_url + '/common/v2/marathon/getRewards'
        res = http_post_request(url, params)
        print("领取奖励：\n" + json.dumps(res, ensure_ascii=False))

    #【admin】获取马拉松列表 /common/v2/marathon/list
    def getList(self,page=1,limit=10):
        params = {}
        if page:
            params['page'] = page
        url = self.env_url_admin + '/marathon/list'
        res =http_get_request(url,params).json()
        print("获取马拉松列表：\n" + json.dumps(res,ensure_ascii=False))

    #【admin】获取奖励名单 /marathon/rewardUserList
    def getRewardUserList(self,name):
        params = {}
        if name:
            params['name'] = name

        url = self.env_url_admin+'/marathon/rewardUserList'
        res = http_get_request(url,params)
        print("获取奖励名单：\n" + json.dumps(res,ensure_ascii=False))

    # 【admin】发奖/marathon/sendReward
    def postsenReward(self,name):
        params = {}
        if name:
            params['name'] = name

        url = self.env_url_admin+'/marathon/sendReward'
        res = http_post_request(url,params).json()
        print("发奖：\n"+json.dumps(res,ensure_ascii=False))



if __name__ == '__main__':
    # 【web/h5】获取马拉松详情/common/v2/marathon/detail
    detail = QaMarathon()
    detail.getDetail('Marathon1661935684431')

    # 【web/h5】获取ticket记录 /common/v2/marathon/userRecordList
    userRecordList = QaMarathon()
    userRecordList.getUserrecordlist('Marathon1661935684431')

    # # 【web/h5】报名    /common/v2/marathon/join
    # join = QaMarathon()
    # join.postJoin(name='Marathon1661935684431')

    # # 【web/h5】领取奖励 /common/v2/marathon/getRewards
    # getRewards = QaMarathon()
    # getRewards.postgetRewards(name='Marathon1661935684431',taskType='CheckPoint',taskId=1)
    # #
    # # 【admin】获取马拉松列表 /common/v2/marathon/list
    # list = QaMarathon()
    # list.getList()
    #
     #【admin】获取奖励名单 /marathon/rewardUserList
    RewardUserList = QaMarathon()
    RewardUserList.getRewardUserList('Marathon1661935684431')

    # # 【admin】发奖/marathon/sendReward
    # sendRewards = QaMarathon()
    # sendRewards.postsenReward()