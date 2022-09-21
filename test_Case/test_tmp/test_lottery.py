import pytest
import yaml
from test_Case.test_tmp.qa_atomintl import QaAtomintl

# 活动-排行赛-抽奖
class TestLottery():
    @pytest.mark.parametrize(['valuation_asset','success'],yaml.safe_load(open("/Users/weijinyu/Desktop/AAX/qa-master/canshu/lottery_data.yaml")))
    def test_lottery(self, valuation_asset, success):
        res = QaAtomintl()
        lottery = res.postLottery(valuation_asset)
        assert (lottery['success']) == success
        print(lottery)


if __name__ == '__main__':
    pytest.main()