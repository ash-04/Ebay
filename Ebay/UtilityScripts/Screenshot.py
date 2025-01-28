class Screenshot:

    def take_screenshot_on_failure(func):
        def wrapper(*arg, **kw):
            res = func(*arg, **kw)
            driver = arg[1]  #assumes driver is the second argument

            if not res:
                driver.save_screenshot("Logs/failed_" + func.__name__ + ".png")

            return res

        return wrapper
