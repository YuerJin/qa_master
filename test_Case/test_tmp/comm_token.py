import requests as r
import yaml

class Comm_Token():
    env_url = yaml.safe_load(open("/Users/weijinyu/Desktop/AAX/qa-master/config/basic_config.yaml"))['env_info']['qa_url']
    def get_token(self,uid):
        orderName = '/common/v2/user/getToken'
        param = 'userId='+str(uid)
        r1 = r.get(self.env_url+orderName,param)
        return 'Bearer ' +r1.json()['data']['token']
        # print('Bearer ' +r1.json()['data']['token'])



if __name__=='__main__':
    qa_token=Comm_Token()
    qa_token.get_token('372863')