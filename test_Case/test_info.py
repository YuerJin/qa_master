import pytest
import yaml

from test_Case.contract import Contract


class Testinfo():
    # def __init__(self):
    #     self.info = Contract()

    # def test_info1(self):
    #     info=Contract()
    #     # return  self.info.contract_info("ETH", "this_week")
    #     contract_code = info.contract_info("ETH", "this_week")
    #     assert contract_code == ['ETH220513']



    @pytest.mark.parametrize(["symbol","contract_type","contract_code"], yaml.safe_load(open(
        "../canshu/contractinfo_data.yaml")))
    def test_info(self,symbol,contract_type,contract_code):
        info = Contract()
        assert  info.contract_info(symbol,contract_type)==contract_code

if __name__ == '__main__':
    pytest.main()
    # a = Testinfo()
    # a.test_info1()
#     a.test_info2()
