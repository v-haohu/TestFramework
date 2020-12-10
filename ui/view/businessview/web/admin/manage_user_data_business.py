# coding=utf-8
# @Time    :
# @Author  :
# @File    : manage_user_data_business.py

from ui.view.baseview.web.business_web import BusinessWebPage
from ui.view.page.web.business.admin.manage_user_data_page import manageuserspage as page
from ui.lib.browser_engine import Logger

class manage_user_data_business(BusinessWebPage):
    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = page()

    # 获取元素点击按钮
    def settings_element(self, sname):
        if self.is_element_clickable(sname):
            self.click(sname)
        else:
            element = self.find_element(*sname)
            self.perform_javascript_click(element)

    # 点击admin_settings按钮
    def click_admin_link(self):
        self.settings_element(self._page.settings_button)
        self.settings_element(self._page.Admin_settings_button)
    
    # 进入manage_user_data页面
    def admin_settings_page(self):
        self.settings_element(self._page.Manage_user_data_button)

    # 搜索用户生成报告
    def search(self, text):
        self.send_keys(self._page.search_people_button, text,need_enter=True)
        # self.click(self._page.get_report_button)
    
    # 选择用户
    def account(self):
        self.click(self._page.user_account)

    # 生成用户数据
    def click_get_report(self):
        self.click(self._page.get_report_button)

    def download(self):
        self.click(self._page.download_button)
