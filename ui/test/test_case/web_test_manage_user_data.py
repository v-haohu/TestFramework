# coding=utf-8

import sys
import os
import time
import unittest
from ui.view.businessview.web.common.login_business import simple_login
from ui.view.businessview.web.admin.manage_user_data_business import *
from ui.lib.base_runner import BaseWebTestCase
from common.lib.base_yaml import Yaml
from ui.lib.browser_engine import Logger, web_config_path


class web_test_manage_user_data(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)
        self.data = Yaml(web_config_path).read()
        self.env = self.data['env']
        self.homeUrl = self.data['portal'][self.env].rstrip("/")

    def test_admin_page(self):
        self.driver = simple_login()
        manage_user_data = manage_user_data_business(self.driver)

        manage_user_data.click_admin_link()
        manage_user_data.admin_settings_page()
        manage_user_data.search('test1@media.ccsctp.net')
        manage_user_data.account()
        manage_user_data.click_get_report()
        time.sleep(5)  # 停顿五秒
        manage_user_data.download()
        self.save_img('web_admin_user_data-test_1-screenshot1')


if __name__ == "_main_":
    unittest.main()
