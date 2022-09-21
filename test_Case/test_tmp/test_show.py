import pytest
import yaml
from test_Case.test_tmp.qa_atomintl import QaAtomintl

# 活动-排行赛-展示
class TestShow():
    @pytest.mark.parametrize(['valuation_asset','success'],yaml.safe_load(open("/Users/weijinyu/Desktop/AAX/qa-master/canshu/show_data.yaml")))
    def test_show(self, valuation_asset, success):
        res = QaAtomintl()
        show = res.getShow(valuation_asset)
        assert (show['success']) == success
        print(show)


if __name__ == '__main__':
    pytest.main()