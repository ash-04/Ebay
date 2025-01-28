import subprocess
import sys
import time
from datetime import datetime
import os
from UtilityScripts.utils import read_result_log, delete_folder

logsDir = os.path.abspath(__file__ + '/../Logs/')


def run_get_price_api_suite(browser, os, platform, environment, item):
    try:
        command = f'pytest -v -m "chrome_windows_desktop" -s Test_Cases/test_add_item_cart.py --bw {browser} --z {os} --x {platform} --t {environment} --a "{item}"'
        print(f"Running Command: {command}")

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   universal_newlines=True)
        for line in process.stdout:
            print(line, end='')

        return_code = process.wait()
        if return_code == 0:
            print("Pytest Process completed successfully.")
            return True
        else:
            print(f"Process failed with return code {return_code}.")

    except Exception as e:
        print(f"Failure in running Suite: {e}")
        return False


def chat_alert():
    pass


if __name__ == "__main__":
    start_time = datetime.now()
    print('argv:', sys.argv)
    browser = sys.argv[1]
    os = sys.argv[2]
    platform = sys.argv[3]
    environment = sys.argv[4]
    item = sys.argv[5]
    print("Deleting Logs folder from the local dir")
    print(logsDir)
    delete_folder(logsDir)

    suite_completion = run_get_price_api_suite(browser, os, platform, environment, item)
    time.sleep(3)
    print(suite_completion)
