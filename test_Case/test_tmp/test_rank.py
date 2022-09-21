import pytest
import yaml
from test_Case.test_tmp.qa_atomintl import QaAtomintl

# 活动-排行赛-排名
class TestRank():
    @pytest.mark.parametrize(['valuation_asset','success'],yaml.safe_load(open("/Users/weijinyu/Desktop/AAX/qa-master/canshu/rank_data.yaml")))
    def test_rank(self, valuation_asset, success):
        res = QaAtomintl()
        rank = res.getRank(valuation_asset)
        assert (rank['success']) == success
        print(rank)


if __name__ == '__main__':
    pytest.main()