import logging
import time

import pytest
from Page.PageAddItemInCart import EBayHomePage
from Page_Objects.browser_launcher import EbayLauncher
from UtilityScripts.utils import custom_logger

url = 'https://ebay.com'


@pytest.mark.usefixtures('page_objects')
class TestBerlinSuite:
    @pytest.fixture(scope='class')
    def page_objects(self, request, pytestconfig):
        browser = pytestconfig.getoption('bw')
        os = pytestconfig.getoption('z')
        platform = pytestconfig.getoption('x')
        env = pytestconfig.getoption('t')
        item_name = pytestconfig.getoption('a')

        br_proxy_obj = EbayLauncher()
        request.cls.br_proxy_obj = br_proxy_obj
        request.cls.obj_proxy = br_proxy_obj.launch_ebay_website(browser, os, platform, env, url)
        request.cls.page_obj = EBayHomePage()

        request.cls.log = custom_logger(logging.INFO)
        request.cls.url = url
        request.cls.item = item_name
        yield

        del request.cls.br_proxy_obj

    @pytest.mark.chrome_windows_desktop
    @pytest.mark.run(order=1)
    def test_ebay_item_search(self):
        """EBay::Homepage--->Verify if item is searchable via search box"""
        time.sleep(2)
        result = self.page_obj.verify_item_is_searchable(self.obj_proxy, self.item)
        assert result is True

    @pytest.mark.chrome_windows_desktop
    @pytest.mark.run(order=2)
    def test_ebay_first_item_clickable(self):
        """EBay::Homepage--->Verify if the first item is clickable """
        time.sleep(5)
        result = self.page_obj.verify_click_first_search_result(self.obj_proxy, self.item)
        assert result is True

    @pytest.mark.chrome_windows_desktop
    @pytest.mark.run(order=3)
    def test_ebay_first_item_added_cart(self):
        """EBay::Homepage--->Verify if the first item is added in the cart """
        time.sleep(5)
        result = self.page_obj.verify_item_is_added_in_cart(self.obj_proxy)
        assert result is True
