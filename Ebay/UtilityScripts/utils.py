import hashlib
import inspect
import json
import shutil
import re
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date, datetime
import os

MOBILE = 'Mobile'
DESKTOP = 'Desktop'
exception_string = "There is a error of"


def is_present(driver, element_id, timeout, by):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, element_id)))
    except Exception as e:
        print(exception_string, str(e))
        print('element not present:', element_id)
        return False
    return True


def get_element_text(driver, element_id, timeout, by):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, element_id)))
        element_text = element.text
        print("element value", element_text)
    except Exception as e:
        print(exception_string, str(e))
        return False
    return element_text


def click_element(driver, element_id, timeout, by):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, element_id)))
        print('element found:', element, element_id)
        time.sleep(2)
        element.click()
        time.sleep(1)
    except Exception as e:
        print(exception_string, str(e))
        return False
    return True


def input_value(driver, element_xpath, timeout, by, value):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, element_xpath)))
        element.click()
        element.send_keys(value)
        time.sleep(4)
    except Exception as e:
        print(exception_string, e)
        return False
    return True


def custom_logger(logLevel=logging.INFO):
    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    if not logger.handlers:
        # By default, log all messages
        logger.setLevel(logging.INFO)
        create_dir(os.path.join(os.path.abspath(__file__ + '/../../'), 'Logs'))
        log_file_path = os.path.join(os.path.abspath(__file__ + '/../../'), 'Logs', f'Logs_{date.today()}.log')
        file_handler = logging.FileHandler(log_file_path, mode='a')
        file_handler.setLevel(logLevel)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logLevel)

        formatter = logging.Formatter('%(asctime)s [%(levelname)4s] %(message)s (%(filename)s:%(lineno)s)',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    return logger


def result_logger(logLevel=logging.INFO, test_type=None):
    logger = logging.getLogger('result_logger')
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        create_dir(os.path.join(os.path.abspath(__file__ + '/../../'), 'Logs'))
        log_file_path = os.path.join(os.path.abspath(__file__ + '/../../'), 'Logs', 'result_logs.log')
        file_handler = logging.FileHandler(log_file_path, mode='w')
        file_handler.setLevel(logLevel)
        formatter = logging.Formatter('%(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger


def create_dir(path):
    '''to create directory'''
    if not os.path.isdir(path):
        os.mkdir(path, 0o777)


def create_file(path):
    '''to create file'''
    if not os.path.isfile(path):
        with open(path, 'w') as fp:
            pass


def clear_and_input_value(driver, element_id, timeout, by, value):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, element_id)))
        element.click();
        element.clear()
        element.send_keys(value)
    except Exception as e:
        print(exception_string, e)
        return False
    return True

def get_css_value(driver, by, locator, css_property):
    """"
    This method will get the CSS property of the element
    :return: CSS property Value
    """
    element = driver.find_element(by, locator)
    return element.value_of_css_property(css_property)


def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)

def delete_folder(path):
    if os.path.isdir(path):
        shutil.rmtree(path)

def create_session_data_file(driver, path):
    '''
    create data.json for stats suite
    '''
    if not os.path.isfile(path):
        with open(path, 'w') as fp:
            session = driver.execute_script("return window.sessionStorage.getItem('sessionId');")
            print("session data is here", session)
            fp.write(session)
        return session


def create_session_data_file_berlin(driver, path):
    '''
    create data.json for stats suite berlin
    '''
    if not os.path.isfile(path):
        with open(path, 'w') as fp:
            session = driver.execute_script("return window.sessionStorage.getItem('fe_uaSessionId');")
            print("session data is here", session)
            if session:
                fp.write(session)
        return session


def read_result_log():
    log_file_path = os.path.join(os.path.abspath(__file__ + '/../../Logs/'), 'result_logs.log')
    with open(log_file_path, 'r+') as result_logs:
        failure_alert = False
        for log in result_logs.readlines():
            log_split = log.split('::')
            result = log_split[2].strip()
            matches = re.findall(r"'(.*?)'", log)
            if result == "FAIL":
                failure_alert = True
                matches = re.findall(r"'(.*?)'", log)
                if matches:
                    break

    return failure_alert, matches

def elements_exists(driver, element_id, timeout, by):
    try:
        element_list = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((by, element_id)))
    except Exception as e:
        print('Exception occurred:', str(e))
        print('elements not present:', element_id)
        return False
    return element_list



