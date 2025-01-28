from selenium.webdriver.common.by import By
from UtilityScripts.utils import is_present, click_element,  clear_and_input_value
from Locators.common_locators import *
from UtilityScripts.Screenshot import Screenshot
import time
from bs4 import BeautifulSoup


class EBayHomePage:

    @Screenshot.take_screenshot_on_failure
    def verify_item_is_searchable(self, driver, item_name):
        result = False
        print(f"The item to search is: {item_name}")
        if is_present(driver, search_box, 30, By.ID):
            clear_and_input_value(driver, search_box, 30, By.ID, item_name)
            click_element(driver, search_button, 10, By.ID)
            time.sleep(5)
            page_source = driver.page_source
            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(page_source, 'html.parser')
            # Search for the desired text in the page content
            if soup.find(text=lambda t: t and item_name.lower() in t.lower()):
                result = True
        return result

    @Screenshot.take_screenshot_on_failure
    def verify_click_first_search_result(self, driver, item_name):
        result = False
        time.sleep(10)
        original_window = driver.current_window_handle
        print(f"Orginal window is : {original_window}")
        if is_present(driver, first_search_result, 10, By.XPATH):
            click_element(driver, first_search_result, 10, By.XPATH)
            time.sleep(10)
            new_window = [window for window in driver.window_handles if window != original_window][0]
            driver.switch_to.window(new_window)
            new_tab_url = driver.current_url
            print(f"Tab URL is {new_tab_url}")
            if item_name in new_tab_url:
                result = True
        return result

    @Screenshot.take_screenshot_on_failure
    def verify_item_is_added_in_cart(self, driver):
        result = False
        if is_present(driver, add_to_cart_button, 10, By.XPATH):
            click_element(driver, add_to_cart_button, 10, By.XPATH)
            time.sleep(5)
            cart_url = driver.current_url
            print(f"The cart URL is : {cart_url}")
            if is_present(driver, item_added_icon, 10, By.XPATH):
                result =True
        return result

