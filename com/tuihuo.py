from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

# mac系统
# executable_path='/Users/oulingling/Desktop/Tools/chromedriver/80/chromedriver'
# driver = webdriver.Chrome(executable_path)

# Windows系统
driver = webdriver.Chrome()

# 用户名/密码
username = 'fengjiangwei'
password = '123456'
# 金力建档号
jilijiandanghao = '6600139803'
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
# 是否退货 选择是
driver.find_element_by_xpath('//*[@id="wayBillStatusPage_isReturn"]/input[1]').click()
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
# 入库
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
# 打开，对内仓储子系统
driver.find_element_by_xpath('//*[@id="btn_wms_in"]').click()
sleep(3)
# 切换当前平台
driver.find_element_by_xpath('//*[@id="header"]/table/tbody/tr[2]/td[5]/span/span/a').click()
sleep(5)
# 切换为北京国美北京配送快速退换货库
driver.find_element_by_id('_easyui_combobox_i1_8').click()
sleep(5)
# 交货入库
driver.find_element_by_xpath('//*[@id="_easyui_tree_5"]/span[4]').click()
sleep(1)
# 交货单号
driver.find_element_by_xpath('//*[@id="deliveryEnterPage_form"]/table/tbody/tr[1]/td[2]/span/input[1]').send_keys(jiaohuodanhao)
sleep(1)
# 查询
driver.find_element_by_xpath('//*[@id="deliveryEnterPage_form_searchId"]/span/span[1]').click()
sleep(1)
# 勾选
driver.find_element_by_xpath('//*[@id="deliveryEnterPage"]/div[2]/div/div/div/div[1]/div[2]/div[2]/table/tbody').click()
sleep(1)
# 交货入库
driver.find_element_by_xpath('//*[@id="deliveryEnterPage_form"]/table/tbody/tr[3]/td[2]/a/span').click()
sleep(2)
# 确认
driver.find_element_by_xpath('/html/body/div[13]/div[3]/a[1]').click()
sleep(10)










