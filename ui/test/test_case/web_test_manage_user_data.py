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
    @classmethod
    def setUpClass(cls):
        super(web_test_manage_user_data, cls).setUpClass()
        cls.driver = simple_login()
        cls.data = Yaml(web_config_path).read()
        cls.env = cls.data['env']
        url = cls.data['portal'][cls.env] + '/admin'
        cls.driver.get(url)

    @unittest.skip("搜索不到对应用户，执行跳过")
    def test01_user_data_page(self):
    #    self.driver = simple_login()
        manage_user_data = manage_user_data_business(self.driver)

    #   manage_user_data.click_admin_link()
    #   manage_user_data.admin_settings_page()
        manage_user_data.search('test1@media.ccsctp.net')
        try:
               self.assertTrue(manage_user_data.get_search_input_user_account(),"搜索用户存在")
        except AssertionError as err:
                print("No this user")
                raise err          
        manage_user_data.account()
    def test02_get_user_report(self):
        manage_user_data = manage_user_data_business(self.driver)    
        manage_user_data.click_get_report()
        time.sleep(5)  # 停顿五秒
        try:
               self.assertTrue(manage_user_data.get_get_report_status(),"验证生成状态")
        except AssertionError as err:
                print("State generating")
                raise err  

        manage_user_data.download()
        self.save_img('web_admin_user_data-test_1-screenshot1')


if __name__ == "_main_":
    unittest.main()
