import traceback
import pytest
import logging


# from UtilityScripts.utils import custom_logger, result_logger
# log = custom_logger(logging.INFO)
# description_text = None


def pytest_addoption(parser):
    parser.addoption("--bw", action="store", default="default name", dest="bw")
    parser.addoption("--z", action="store", default="default name")
    parser.addoption("--x", action="store", default="default name")
    parser.addoption("--r", action="store", default="default name")
    parser.addoption("--t", action="store", default="default name")
    parser.addoption("--l", action="store", default="default name")
    parser.addoption("--s", action="store", default="default name")
    parser.addoption("--a", action="store", default="default name")

# @pytest.fixture(scope='session',autouse=True)
# def set_logger(request):
#     log.info(f"Setting Custom Logger with type {set_logger}")
#     logger = result_logger(logging.INFO)
#     request.session.result_logger = logger

