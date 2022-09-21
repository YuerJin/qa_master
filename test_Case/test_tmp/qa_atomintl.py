
import yaml,json
import requests as r
from test_Case.test_tmp.comm_token import Comm_Token
from common.comm_http import http_get_request,http_post_request

class QaAtomintl():
    env_url = yaml.safe_load(open("/Users/weijinyu/Desktop/AAX/qa-master/config/basic_config.yaml"))['env_info']['qa_url']

    # 活动-排行赛-抽奖记录/race/lottery/records
    def getRecord(self,name,page=0,limit=10):
        params = {}
        if name:
            params['name'] = name
        url = self.env_url + '/common/v2/race/lottery/records'
        response =  http_get_request(url, params).json()
        # return response
        print("抽奖记录: "+json.dumps(response))

     #活动-排行赛-梯级任务(礼包)列表/race/task
    def getTask(self,name,page=0,limit=10):
        params = {}
        if name:
            params['name'] = name
        url = self.env_url+'/common/v2/race/task'
        response = http_get_request(url,params).json()
        print("阶梯任务（礼包）列表 ： " + json.dumps(response))

    # #活动-排行赛-展示/v2/race/show
    def getShow(self,name,force=True):
        params = {}
        if name:
            params['name'] = name
        if force:
            params['force'] = force
        url = self.env_url+'/common/v2/race/show'
        res = http_get_request(url,params).json()
        # return res.json()
        print("展示：" + json.dumps(res))


    #活动-排行赛-排名/v2/race/ranking
    def getRank(self,name,userName='',teamName='',top=10,page=0,limit=10):
        params ={}
        if name:
            params['name'] = name
        if userName:
            params['userName'] = userName
        if teamName:
            params['teamName'] = teamName
        if top:
            params['top'] = top
        url = self.env_url + '/common/v2/race/ranking'
        res = http_get_request(url,params)
        return res.json()
        # print(res.json())


    #抽奖/race/lottery
    def postLottery(self,name):
        header={
            "Content-Type" : "application/json"
        }
        params = {}
        if name:
            params['name'] = name
        url = self.env_url + "/common/v2/race/lottery"
        res = http_post_request(url=url,params=params,add_to_headers=header)
        return res
        # print(res)

#     查询用户是否被屏蔽/user/activityExcludeTags
    def getExcludeTags(self,activityName):
        params = {}
        if activityName:
            params['activityName'] = activityName

        url = self.env_url+'/common/v2/user/activityExcludeTags'
        res = http_get_request(url,params).json()
        print("该用户是否被屏蔽（false被屏蔽）：\n" + json.dumps(res,ensure_ascii=False))




if __name__== '__main__':
    tags = QaAtomintl()
    tags.getExcludeTags("SpaceRun")
    tags.getExcludeTags("NewWelfare")
    tags.getExcludeTags("TaskCenter")
    tags.getExcludeTags("gameHall")

    # record= QaAtomintl()
    # record.getRecord('RACE202208BO')
    #
    # show = QaAtomintl()
    # show.getShow('RACE202208BO')
    #
    # rank = QaAtomintl()
    # rank.getRank("")
    #
    # lottery = QaAtomintl()
    # lottery.postLottery("")
    #
    # task = QaAtomintl()
    # task.getTask("RACE202208BO")





