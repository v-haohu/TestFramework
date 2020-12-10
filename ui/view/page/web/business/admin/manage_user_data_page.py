# coding=utf-8
# @Time    :
# @Author  :
# @File    : browse_page.py


from selenium.webdriver.common.by import By

class manageuserspage:
    settings_button = (By.XPATH, '//span[@class="ms-Icon--Settings"]')
    #Admin_settings_button = (By.XPATH, '//input[@id="AdminSettingsLink or @value="管理设置"]')
    Admin_settings_button = (By.ID, 'AdminSettingsLink')
    Manage_user_data_button = (By.XPATH, '//*[@id="manage-users-navigation"]/nav/ul/li[1]/button')
    search_people_button = (By.NAME, 'search-field')
    user_account = (By.XPATH, '/html/body/div[1]/div/div[2]/admin-setting-detail/div/section/div/div[2]/personal-data/div/div[2]/div[2]/principal-group-search/div/div[2]/div/ul/li[1]/div/div[2]')
    get_report_button = (By.XPATH, '//button[@class= "stream-btn btn-primary get-report-button ng-binding"]')
    #download_button = (By.ID, 'icon_download')
    download_button = (By.XPATH, '//div[contains(@infinite-scroll-container, "window")]/div[1]/item/personal-data-principal-item/principal-item-base/div/list-row/ng-transclude/list-cell[6]/div/div/ng-transclude/ng-transclude/custom-column4/a')