import pytest
import yaml
from test_Case.test_tmp.qa_atomintl import QaAtomintl

# 活动-排行赛-抽奖记录
class TestRecord():
    @pytest.mark.parametrize(['valuation_asset', 'success'], yaml.safe_load(open("/Users/weijinyu/Desktop/AAX/qa-master/canshu/record_data.yaml")))
    def test_record(self,valuation_asset,success):
        res=QaAtomintl()
        record = res.getRecord(valuation_asset)
        assert (record['success'])==success
        print(record)

if __name__ == '__main__':
    pytest.main()


