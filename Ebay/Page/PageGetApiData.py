import json
import logging
from UtilityScripts.utils import custom_logger
import requests
from bs4 import BeautifulSoup
from os.path import join, abspath


log = custom_logger(logging.INFO)


class PageAPISuite:

    @staticmethod
    def validate_get_price_api(url):
        result = False
        try:
            response = requests.get(url)
            print(f'status_code: {response.status_code}')
            if response.status_code != 200:
                result = False
            else:
                data = json.loads(response.text)
                print(data)
                result = True
        except Exception as e:
            log.error(f'Exception {e} occurred')
        finally:
            return result

    @staticmethod
    def validate_bpis(url):
        result = False
        try:
            response = requests.get(url)
            data = json.loads(response.text)
            if 'bpi' in data:
                bpi = data["bpi"]
                expected_currencies = {"USD", "GBP", "EUR"}
                actual_currencies = set(bpi.keys())
                print(actual_currencies)
                if actual_currencies == expected_currencies:
                    result = True
        except Exception as e:
            log.error(f'Exception {e} occurred')
        finally:
            return result

    @staticmethod
    def validate_GBP(url):
        result = False
        try:
            response = requests.get(url)
            data = json.loads(response.text)
            if 'bpi' in data:
                bpi = data["bpi"]
                if bpi["GBP"]["description"] == "British Pound Sterling":
                    result = True
        except Exception as e:
            log.error(f'Exception {e} occurred')
        finally:
            return result

