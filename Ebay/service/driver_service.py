from UtilityScripts.Webdriver import *

MOBILE = 'Mobile'
DESKTOP = 'Desktop'
TABLET = 'Tablet'

def get_browser_driver(os, platform, browser):
    webdriver = None
    if platform == MOBILE:
        if os == 'iOS':
            if browser == 'Safari':
                webdriver = SafariDriver(platform)
            else:
                print('Invalid iOS Browser!!!')
        elif os == 'Android':
            print("Android OS")
            if browser == 'Chrome':
                print('Chrome launch on android')
                webdriver = ChromeDriver(os)
            elif browser == 'Edge':
                print ('Edge launch on android')
                webdriver = EdgeDriver(platform)
            else:
                print('Invalid Android Browser')


    elif platform == DESKTOP:
        if os == 'Windows':
            if browser == 'Chrome':
                webdriver = ChromeDriver(os)
            elif browser == 'Edge':
                webdriver = EdgeDriver(platform)
            else:
                print('Invalid Browser!!!')
        elif os == 'iOS':
            if browser == 'Chrome':
                webdriver = ChromeDriver(os)
            elif browser == 'Safari':
                webdriver = SafariDriver(platform)
            else:
                print('Invalid Browser!!!')
    return webdriver