from UtilityScripts.utils import  *
import time
from service.driver_service import get_browser_driver


class EbayLauncher:
    def __init__(self):
        self.webdriver = None

    def launch_browser_domain(self, domain,maximize_window, env):
        self.webdriver.get_driver()
        self.webdriver.launch_driver()
        time.sleep(2)
        if maximize_window:
            self.webdriver.sdriver.maximize_window()
            time.sleep(2)
        self.webdriver.sdriver.get(domain)
        time.sleep(10)

    def launch_ebay_website(self, browser, os, platform, env, url):
        
        self.webdriver = get_browser_driver(os, platform, browser)
        domain = url
        print("domain:", domain)
        print("platform:", platform)
        maximize_window = not (platform == 'Mobile')
        time.sleep(3)
        print("window maximized", maximize_window)
        self.launch_browser_domain(domain, maximize_window, env)
        return self.webdriver.sdriver