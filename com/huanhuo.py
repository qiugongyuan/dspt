from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

# mac系统
#executable_path='/Users/oulingling/Desktop/Tools/chromedriver/80/chromedriver'
# driver = webdriver.Chrome(executable_path)

# Windows系统
driver = webdriver.Chrome()

# # 用户名/密码
username = 'fengjiangwei'
password = '123456'
# 金力建档号
jilijiandanghao = '9500066501'
# 别名
bieming = '0409'

# 安迅物流
driver.get("http://10.112.68.41/gome-lmis-login/index.do")
driver.maximize_window()
# 账号登录
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('loginBtn').click()
sleep(1)
# 关闭修改密码弹窗
driver.find_element_by_xpath('/html/body/div[9]/div[1]/div[3]/a').click()
sleep(1)
# 打开，运输子系统
driver.find_element_by_xpath('//*[@id="btn_tms"]').click()
sleep(1)
# 切换当前平台
driver.find_element_by_xpath('//*[@id="header"]/table/tbody/tr[2]/td[5]/span/span/a').click()
# 切换为北分北京配送中心
driver.find_element_by_id('_easyui_combobox_i1_19').click()
sleep(3)
# 运单状态追踪
driver.find_element_by_xpath('//*[@id="_easyui_tree_5"]/span[4]').click()
sleep(3)
# 金力建档号
driver.find_element_by_xpath('//*[@id="wayBillStatusPage_form"]/table/tbody/tr[3]/td[2]/span/input[1]').send_keys(jilijiandanghao)
sleep(1)

# 查询
driver.find_element_by_xpath('//*[@id="wayBillStatusPage_form"]/table/tbody/tr[4]/td[5]/a[2]/span/span[1]').click()
sleep(3)
# 获取运单号
# 运单号
element1 = driver.find_element_by_xpath('//*[@id="datagrid-row-r3-2-0"]/td[5]')
sleep(1)
yundanhao = element1.text
# 交货单号
sleep(1)
element2 = driver.find_element_by_xpath('//*[@id="datagrid-row-r3-2-0"]/td[8]')
sleep(1)
jiaohuodanhao = element2.text
sleep(1)

# # 换货
# # 安迅物流
# driver.get("http://10.112.68.41/gome-lmis-login/index.do")
# driver.maximize_window()
# # 账号登录
# driver.find_element_by_id('username').clear()
# driver.find_element_by_id('username').send_keys(username)
# driver.find_element_by_id('password').clear()
# driver.find_element_by_id('password').send_keys(password)
# driver.find_element_by_id('loginBtn').click()
# sleep(1)
# # 关闭修改密码弹窗
# driver.find_element_by_xpath('/html/body/div[9]/div[1]/div[3]/a').click()
# sleep(1)
# # 打开，对内仓储子系统
# driver.find_element_by_xpath('//*[@id="btn_wms_in"]').click()
# sleep(3)
# # 切换当前平台
# driver.find_element_by_xpath('//*[@id="header"]/table/tbody/tr[2]/td[5]/span/span/a').click()
# sleep(5)
# #切换为北京国美北京配送正常库
# driver.find_element_by_id('_easyui_combobox_i1_2').click()
# sleep(5)
# # 转仓出库
# driver.find_element_by_xpath('//*[@id="_easyui_tree_9"]/span[4]').click()
# sleep(1)
# # 转仓发货单号
# driver.find_element_by_xpath('//*[@id="switchOutPage_form"]/table/tbody/tr[1]/td[2]/span/input[1]').send_keys(jiaohuodanhao)
# sleep(1)
# # 查询
# driver.find_element_by_xpath('//*[@id="searchS"]/span/span[1]').click()
# sleep(1)
# # 勾选
# driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div/input').click()
# sleep(1)
# # 转仓出库
# driver.find_element_by_xpath('//*[@id="switchOutPage_form"]/table/tbody/tr[3]/td[2]/a/span/span[1]').click()
# sleep(3)
# #确定
# driver.find_element_by_xpath('/html/body/div[12]/div[3]/a[1]/span/span').click()
#
# #切换平台
# driver.find_element_by_xpath('//*[@id="header"]/table/tbody/tr[2]/td[5]/span/span/a').click()
# sleep(5)
# #切换为北京国美北京配送残次库
# driver.find_element_by_xpath('//*[@id="_easyui_combobox_i1_3"]').click()
# sleep(5)
# # 转仓入库
# driver.find_element_by_xpath('//*[@id="_easyui_tree_4"]/span[4]').click()
# sleep(1)
#
# # 转仓收货单号
# driver.find_element_by_xpath('//*[@id="switchForm"]/table/tbody/tr[1]/td[2]/span/input[1]').send_keys('9500190005')
# sleep(1)
# # 查询
# driver.find_element_by_xpath('//*[@id="switchForm_searchId"]/span/span[1]').click()
# sleep(1)
# # 勾选
# driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div/input').click()
# sleep(1)
# # 转仓入库
# driver.find_element_by_xpath('//*[@id="switchForm"]/table/tbody/tr[3]/td[2]/a/span/span[1]').click()
# sleep(1)
# #弹窗确定
# driver.find_element_by_xpath('/html/body/div[13]/div[3]/a[1]/span/span').click()

# 签收管理 ---- 操作
driver.get("http://10.112.68.41/gome-lmis-login/index.do")
driver.maximize_window()
# 账号登录
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('loginBtn').click()
sleep(1)
# 关闭修改密码弹窗
driver.find_element_by_xpath('/html/body/div[9]/div[1]/div[3]/a').click()
sleep(1)
# 打开，运输子系统
driver.find_element_by_xpath('//*[@id="btn_tms"]').click()
sleep(1)
# 切换当前平台
driver.find_element_by_xpath('//*[@id="header"]/table/tbody/tr[2]/td[5]/span/span/a').click()
# 切换为北分北京配送中心
driver.find_element_by_id('_easyui_combobox_i1_19').click()
sleep(3)
# 签收管理
driver.find_element_by_xpath('//*[@id="_easyui_tree_20"]/span[4]').click()
sleep(2)
# 运送单
driver.find_element_by_xpath('//*[@id="signatureManager_page"]/div[1]/div/table/tbody/tr[1]/td[2]/span/input[1]').send_keys(yundanhao)
sleep(2)
# 查询
driver.find_element_by_xpath('//*[@id="signatureManager_page"]/div[1]/div/table/tbody/tr[2]/td[2]/a[2]/span/span[1]').click()
sleep(2)
# 勾选
driver.find_element_by_xpath('//*[@id="signatureManager_page"]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input').click()
sleep(1)
# 右键
element7 = driver.find_element_by_xpath('//*[@id="datagrid-row-r3-2-0"]/td[1]/div/input')
ActionChains(driver).context_click(element7).click().perform()
# 妥投
driver.find_element_by_xpath('/html/body/div[12]/div[7]/div[1]').click()
sleep(5)
# 回执详情查询
driver.find_element_by_xpath('//*[@id="_easyui_tree_32"]/span[4]').click()
sleep(2)
# 运单号
driver.find_element_by_xpath('//*[@id="cmReceiptDetailPage_form"]/table/tbody/tr[1]/td[4]/span/input[1]').send_keys(yundanhao)
sleep(1)
# 查询
driver.find_element_by_xpath('//*[@id="cmReceiptDetailPage_form"]/table/tbody/tr[2]/td[3]/a[2]/span/span[1]').click()
sleep(1)
# 勾选
driver.find_element_by_xpath('//*[@id="cmReceiptDetailPage"]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input').click()
sleep(5)
# 右键
element8 = driver.find_element_by_xpath('//*[@id="cmReceiptDetailPage"]/div[2]/div/div/div/div[1]/div[2]/div[2]')
ActionChains(driver).context_click(element8).click().perform()
sleep(3)
# 回执
driver.find_element_by_xpath('//*[@id="TMS050205"]/div[1]').click()
sleep(1)
# 确定回执
driver.find_element_by_xpath('/html/body/div[19]/div[3]/a[1]').click()
sleep(10)










