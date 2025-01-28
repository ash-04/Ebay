import pytest
from Page.PageGetApiData import PageAPISuite


class TestPriceAPI:

    price_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


    @pytest.mark.prod
    @pytest.mark.staging
    @pytest.mark.qa
    @pytest.mark.run(order=265)
    def test_getPrice_api(self):
        """API::MISC --->Verify get api is working fine"""
        status = PageAPISuite.validate_get_price_api(TestPriceAPI.price_url)
        if not status:
            assert status is True, 'getprice API list is empty'

    @pytest.mark.prod
    @pytest.mark.staging
    @pytest.mark.qa
    @pytest.mark.run(order=266)
    def test_getPrice_bpis(self):
        """API::MISC --->Verify if there are 3 bpis"""
        status = PageAPISuite.validate_bpis(TestPriceAPI.price_url)
        assert status is True

    @pytest.mark.prod
    @pytest.mark.staging
    @pytest.mark.qa
    @pytest.mark.run(order=267)
    def test_getPrice_GBP(self):
        """API::MISC --->Verify if GBP is Pound Sterling"""
        status = PageAPISuite.validate_GBP(TestPriceAPI.price_url)
        assert status is True