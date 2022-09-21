import pytest
import yaml
from test_Case.contract import Contract


class Testindex():
    @pytest.mark.parametrize(['symbol', 'status'], yaml.safe_load(open("../canshu/contractindex_data.yaml")))
    def test_index(self, symbol, status):
        index = Contract()
        assert index.contract_index(symbol) == status


if __name__ == '__main__':
    pytest.main()
