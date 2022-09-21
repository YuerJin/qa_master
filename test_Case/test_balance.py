import pytest
import yaml

from test_Case.contract_post import ContractPost

class TestBalance():
    @pytest.mark.parametrize(['valuation_asset','status'],yaml.safe_load(open("../canshu/contractbalabce_data.yaml")))
    def test_balance(self,valuation_asset,status):
        balance=ContractPost()
        assert balance.contract_balance(valuation_asset)==status
if __name__ == '__main__':
    pytest.main()