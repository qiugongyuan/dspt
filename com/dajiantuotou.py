from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

executable_path='/Users/oulingling/Desktop/Tools/chromedriver/80/chromedriver'
driver = webdriver.Chrome(executable_path)

# 用户名/密码
username = 'fengjiangwei'
password = '123456'
# 金力建档号
jilijiandanghao = '2570446923'
# 运单号
yundanhao = 'AX62186118338'
# 交货单号
jiaohuodanhao = '7000154525'
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
# 查询
driver.find_element_by_xpath('//*[@id="wayBillStatusPage_form"]/table/tbody/tr[4]/td[5]/a[2]/span/span[1]').click()
sleep(3)
# 获取运单号
# 待补充

# 取派分单
driver.find_element_by_xpath('//*[@id="_easyui_tree_26"]/span[4]').click()
sleep(3)
# 运单号
driver.find_element_by_xpath('//*[@id="partBillPage"]/div[1]/div/table/tbody/tr/td[2]/span/input[1]').send_keys(yundanhao)
# 显示全部单据
driver.find_element_by_xpath('//*[@id="TMS0403_isAll"]').click()
# 查询
driver.find_element_by_xpath('//*[@id="partBillPage"]/div[1]/div/table/tbody/tr/td[8]/a[2]/span/span[1]').click()
sleep(3)
# 勾选
driver.find_element_by_xpath('//*[@id="datagrid-row-r4-1-0"]/td/div').click()
sleep(3)
# 右键
element=driver.find_element_by_xpath('//*[@id="datagrid-row-r4-1-0"]/td/div')
ActionChains(driver).context_click(element).click().perform()
sleep(1)
# 派送分单
driver.find_element_by_xpath('//*[@id="TMS040306"]/div[1]').click()
sleep(1)
# 派送承运商
driver.find_element_by_xpath('//*[@id="waybillCarrierDesignatePage_CarrierDesignate_form1"]/table/tbody/tr[3]/td[2]/span/span/a').click()
# 北京东方物流有限公司
driver.find_element_by_xpath('//*[@id="_easyui_combobox_i4_3"]').click()
sleep(1)
# 派送配送区域
driver.find_element_by_xpath('//*[@id="waybillCarrierDesignatePage_CarrierDesignate_form1"]/table/tbody/tr[4]/td[2]/span/span/a').click()
sleep(1)
# 1115北京丰台区
driver.find_element_by_xpath('//*[@id="_easyui_combobox_i6_0"]').click()
# 保存
driver.find_element_by_xpath('//*[@id="waybillCarrierDesignatePage1"]/div/a/span/span[1]').click()
sleep(3)
# 取派计划
driver.find_element_by_xpath('//*[@id="_easyui_tree_27"]/span[4]').click()
sleep(1)
# 右键
element1 = driver.find_element_by_xpath('//*[@id="takePlan_indexPage"]/div[1]/div/div[1]/div[2]/div[2]')
ActionChains(driver).context_click(element1).click().perform()
# 新建
driver.find_element_by_xpath('//*[@id="TMS040110"]/div[1]').click()
sleep(3)
# 承运商
driver.find_element_by_xpath('//*[@id="takePlan_edit_form"]/table/tbody/tr[3]/td[2]/span/span/a').click()
sleep(1)
# 北京东方物流有限公司
driver.find_element_by_xpath('//*[@id="condition"]').send_keys('北京东方物流有限公司')
# 查找
driver.find_element_by_xpath('//*[@id="search"]').click()
sleep(5)
element2 = driver.find_element_by_css_selector('#datagrid-row-r11-2-0')
ActionChains(driver).double_click(element2).perform()
sleep(6)
# 司机
driver.find_element_by_xpath('//*[@id="takePlan_edit_form"]/table/tbody/tr[5]/td[2]/span/span/a').click()
sleep(1)
# 康盛金
element3 = driver.find_element_by_css_selector('#datagrid-row-r12-2-2')
ActionChains(driver).double_click(element3).perform()
sleep(3)
# 运单号
driver.find_element_by_xpath('//*[@id="takePlan_addSendWaybill_form"]/table/tbody/tr[1]/td[4]/span/input[1]').send_keys(yundanhao)
sleep(1)
# 查询
driver.find_element_by_xpath('//*[@id="takePlan_addSendWaybill_form"]/table/tbody/tr[5]/td[3]/a[1]/span/span[1]').click()
# 勾选
driver.find_element_by_xpath('//*[@id="takePlanAdd_sendWaybill_Page"]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input').click()
sleep(1)
# 右键
element4 = driver.find_element_by_xpath('//*[@id="datagrid-row-r7-2-0"]')
ActionChains(driver).context_click(element4).click().perform()
sleep(1)
# 添加派送运单
driver.find_element_by_xpath('//*[@id="autoSendWaybillMenu"]/div[2]/div[1]').click()
sleep(5)
# 别名
driver.find_element_by_xpath('//*[@id="takePlan_edit_form"]/table/tbody/tr[2]/td[2]/span/input[1]').send_keys(bieming)
sleep(1)
# 保存
driver.find_element_by_xpath('//*[@id="saveTakePlan"]/span/span[1]').click()
sleep(3)
# 确定
driver.find_element_by_xpath('/html/body/div[50]/div[3]/a[1]/span/span').click()
sleep(3)
# 关闭
driver.find_element_by_xpath('//*[@id="takePlan_edit_form"]/table/tbody/tr[22]/td/a[2]/span/span[1]').click()
sleep(2)
# 右键
element5 = driver.find_element_by_xpath('//*[@id="takePlan_indexPage"]/div[1]/div/div[1]/div[2]/div[2]')
ActionChains(driver).context_click(element5).click().perform()
sleep(1)
# 查询全部
driver.find_element_by_xpath('//*[@id="TMS040102"]/div[1]').click()
sleep(5)
# 勾选
driver.find_element_by_xpath('//*[@id="datagrid-row-r5-2-0"]/td[4]').click()
sleep(5)
# 右键
element6 = driver.find_element_by_xpath('//*[@id="datagrid-row-r5-2-0"]/td[4]')
ActionChains(driver).context_click(element6).click().perform()
# 确认发车
driver.find_element_by_xpath('//*[@id="TMS040109"]/div[1]').click()
# 确定
driver.find_element_by_xpath('/html/body/div[31]/div[3]/a[1]').click()
# 发货
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
# 切换为北京国美北京配送正常库
driver.find_element_by_id('_easyui_combobox_i1_2').click()
sleep(5)
# 交货出库
driver.find_element_by_xpath('//*[@id="_easyui_tree_11"]/span[4]').click()
sleep(1)
# 交货单号
driver.find_element_by_xpath('//*[@id="deliveryOrderIndexPage_form"]/table/tbody/tr[1]/td[2]/span/input[1]').send_keys(jiaohuodanhao)
sleep(1)
# 查询
driver.find_element_by_xpath('//*[@id="searchD"]/span/span[1]').click()
sleep(1)
# 勾选
driver.find_element_by_xpath('//*[@id="deliveryOrderIndexPage"]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div').click()
sleep(1)
# 交货出库
driver.find_element_by_xpath('//*[@id="deliveryOrderIndexPage_form"]/table/tbody/tr[3]/td[2]/a/span/span[1]').click()
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
driver.find_element_by_xpath('//*[@id="_easyui_tree_21"]/span[4]').click()
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
driver.find_element_by_xpath('//*[@id="_easyui_tree_33"]/span[4]').click()
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
element8 = driver.find_element_by_xpath('//*[@id="cmReceiptDetailPage"]/div[2]/div/div/div/div[1]/div[2]/div[2]/table')
ActionChains(driver).context_click(element8).click().perform()
sleep(3)
# 回执
driver.find_element_by_xpath('//*[@id="TMS050205"]/div[1]').click()
sleep(1)
# 确定回执
driver.find_element_by_xpath('/html/body/div[19]/div[3]/a[1]').click()
sleep(10)










