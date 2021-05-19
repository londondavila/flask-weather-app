import os
from selenium import webdriver


class Request:
    
    # define url, create phantomjs driver
    def __init__(self, base_url):
        self.phantomjs_path = os.path.join(os.curdir, 'phantomjs/bin/phantomjs')
        self.base_url = base_url
        self.driver = webdriver.PhantomJS(self.phantomjs_path)

    # format url and add forecast/area option
    def fetch_data(self, forecast, area):
        url = self.base_url.format(forecast=forecast, area=area)
        self.driver.get(url)

        if self.driver.title == '404 Not Found':
            err = ('Could not find the area that you are searching for')
            raise Exception(err)

        return self.driver.page_source