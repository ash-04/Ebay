import chromedriver_autoinstaller
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.microsoft import EdgeChromiumDriverManager



class BaseDriver:
    def __init__(self):
        self.sdriver = None

    def get_driver(self):
        pass

    def launch_driver(self):
        pass

    def __del__(self):
        print("deleting session")
        print(self.sdriver)
        if self.sdriver:
            for handle in self.sdriver.window_handles:
                self.sdriver.switch_to.window(handle)
                self.sdriver.close()
            self.sdriver.quit()


class ChromeDriver(BaseDriver):
    def __init__(self, os, platform=None, real_device=False):
        super().__init__()
        self.chrome_options = None
        self.os = os
        self.platform = platform
        self.real_device = real_device

    def get_driver(self):
        if self.os == 'Windows':
            self.chrome_options = webdriver.ChromeOptions()

            self.chrome_options.add_argument("--no-sandbox")
            self.chrome_options.add_argument("--window-size=1024,1080")
            self.chrome_options.add_argument("--ignore-certificate-errors")
            self.chrome_options.add_argument("--disable-dev-shm-usage")
            yield self.sdriver
            self.sdriver.quit()
        #elif self.os == 'Android':
        #         self.chrome_options = webdriver.ChromeOptions()
        elif self.os == 'Android':
            if self.real_device:
                pass
            else:
                self.options = webdriver.ChromeOptions()
                self.options.add_experimental_option('androidPackage', 'com.android.chrome')
        else:
            pass

    def launch_driver(self):
        if self.os == 'Windows':
            caps = DesiredCapabilities.CHROME
            caps['goog:loggingPrefs'] = {'performance': 'ALL'}
            self.sdriver = webdriver.Chrome(options=self.chrome_options)
        elif self.os == 'Android':
            d_capabilities = DesiredCapabilities.CHROME
            if not self.real_device:
                username = cfg.drivers_config["BROWSERSTACK_USERNAME"]
                accessKey = cfg.drivers_config["BROWSERSTACK_ACCESS_KEY"]
                if self.platform == 'Tablet':
                    d_capabilities.update(cfg.drivers_config["desired_caps_android_tablet"])
                else:
                    d_capabilities.update(cfg.drivers_config["desired_caps"])
                print("caps:", d_capabilities)
                self.sdriver = webdriver.Remote(
                    command_executor='https://' + username + ':' + accessKey + '@hub-cloud.browserstack.com/wd/hub',
                    desired_capabilities=d_capabilities)

            else:
                if self.platform == 'Mobile':
                    desired_caps = cfg.drivers_config["desired_capabilities_for_mobile"]
                else:
                    desired_caps = cfg.drivers_config["desired_capabilities_for_android_tablet"]
                appium_server = 'http://localhost:4723/wd/hub'
                self.sdriver = appium_webdriver.Remote(appium_server, desired_caps)
        else:
            de_capabilities = DesiredCapabilities.CHROME
            de_capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
            self.sdriver = webdriver.Chrome(chromedriver_autoinstaller.install())


class EdgeDriver(BaseDriver):
    def __init__(self, platform):
        super().__init__()
        self.platform = platform

    def get_driver(self):
        return self.sdriver

    def launch_driver(self):
        d = DesiredCapabilities.EDGE
        d['ms:loggingPrefs'] = {'performance': 'ALL'}
        d['acceptInsecureCerts'] = bool(True)

        # load the desired webpage
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        edge_options.set_capability("ms:edgeOptions", d)

        # self.sdriver = Edge(EdgeChromiumDriverManager().install(), options=edge_options)
        # Create a service object for the Edge driver
        service = Service(executable_path=edge_driver_path)

        # Create a new instance of the Edge driver
        self.sdriver = Edge(service=service, options=options)

    def __del__(self):
        if self.sdriver:
            self.sdriver.quit()


class SafariDriver(BaseDriver):
    def __init__(self, platform):
        super().__init__()
        self.platform = platform

    def get_driver(self):
        return self.sdriver

    def launch_driver(self):
        cap_safari = DesiredCapabilities.SAFARI
        cap_safari['goog:loggingPrefs'] = {'performance': 'ALL'}
        if self.platform == 'Mobile':
            cap_safari = DesiredCapabilities.SAFARI

            username = cfg.drivers_config["BROWSERSTACK_USERNAME"]
            accessKey = cfg.drivers_config["BROWSERSTACK_ACCESS_KEY"]

            cap_safari.update(cfg.drivers_config["desired_capabilities_ios_safari"])
            print("caps:", cap_safari)

            # self.sdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cap_safari)
            self.sdriver = webdriver.Remote(
                command_executor='https://' + username + ':' + accessKey + '@hub-cloud.browserstack.com/wd/hub',
                desired_capabilities=cap_safari)

        elif self.platform == 'Desktop':
            self.sdriver = webdriver.Safari(desired_capabilities=cap_safari)
        else:
            print("Invalid selection")
