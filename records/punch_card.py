import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree

# start = time.time()
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(options=chrome_options)
# wait = WebDriverWait(browser, 5)
# browser.get('https://xd.boxkj.com/?code=031XxZ100RWRsN1y5c400ut5Cv2XxZ19&state=123#/pages/user/user')
# login = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page'
#                                                          '-body/uni-view/uni-view/uni-view[1]/uni-view/uni-text['
#                                                          '1]/span')))
# login.click()
#
# user_name = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni'
#                                                                  '-page-body/uni-view/uni-view[2]/uni-view['
#                                                                  '1]/uni-view/uni-input/div/input')))
# password = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni'
#                                                                 '-page-body/uni-view/uni-view[2]/uni-view['
#                                                                 '2]/uni-view/uni-input/div/input')))
# user_name.send_keys('20010190010')
# password.send_keys('15829415820.yun')
#
# time.sleep(0.1)
# wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view'
#                                                  '/uni-view[3]/uni-button'))).click()
# browser.get(
#     "https://xd.boxkj.com/?code=031XxZ100RWRsN1y5c400ut5Cv2XxZ19&state=123#/pages/stu/clock/stuPunchRecordList?userNum=20010190010&sysTermId=12")
#
# wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-item-1"]'))).click()
# time.sleep(0.2)
# # print(browser.page_source)
# res_text = etree.HTML(browser.page_source)
# data_list = res_text.xpath('//*[@id="goodundefined"]')
# # print(data_list)
# for data in data_list:
#     record = data.xpath('./uni-view/uni-view//text()')
#     print(record)
# end = time.time()
# print(end - start)


class Punch(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=chrome_options)

        self.login_url = 'https://xd.boxkj.com/?code=031XxZ100RWRsN1y5c400ut5Cv2XxZ19&state=123#/pages/user/user'
        self.data_url = 'https://xd.boxkj.com/?code=031XxZ100RWRsN1y5c400ut5Cv2XxZ19&state=123#/pages/stu/clock/stuPunchRecordList?userNum=20010190010&sysTermId=12'
        self.wait = WebDriverWait(self.browser, 5)

    def login(self):
        self.browser.get(self.login_url)
        login = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page'
                                                                 '-body/uni-view/uni-view/uni-view[1]/uni-view/uni-text['
                                                                 '1]/span')))
        login.click()

        user_name = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni'
                                                      '-page-body/uni-view/uni-view[2]/uni-view['
                                                      '1]/uni-view/uni-input/div/input')))
        password = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni'
                                                      '-page-body/uni-view/uni-view[2]/uni-view['
                                                      '2]/uni-view/uni-input/div/input')))
        user_name.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(0.1)
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view'
                                                  '/uni-view[3]/uni-button'))).click()

    def get_data(self):
        self.browser.get(self.data_url)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-item-1"]'))).click()
        time.sleep(0.2)
        # print(browser.page_source)
        res_text = etree.HTML(self.browser.page_source)
        data_list = res_text.xpath('//*[@id="goodundefined"]')
        # print(data_list)
        res_data = []
        for data in data_list:
            record = data.xpath('./uni-view/uni-view//text()')
            address = record[0]
            remark = record[1]
            date = record[2]
            data_dict = {'address': address, 'remark': remark, 'date': date}
            res_data.append(data_dict)
        return res_data

    def run(self):
        self.login()
        return self.get_data()


if __name__ == '__main__':
    demo = Punch('20010190010', '15829415820.yun')
    demo.run()
