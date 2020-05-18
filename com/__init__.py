import selenium
from selenium import webdriver
from time import sleep

# chromedriver_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
# driver = webdriver.Chrome(chromedriver_path)

executable_path='/Users/oulingling/Desktop/Tools/chromedriver/80/chromedriver'
driver = webdriver.Chrome(executable_path)

driver.get("http://10.112.68.41/gome-lmis-login/index.do")
driver.maximize_window()

# ermadmin账号登录
# driver.find_element_by_id('userName').clear()
# driver.find_element_by_id('userName').send_keys('ermadmin')
# driver.find_element_by_id('passWord').clear()
# driver.find_element_by_id('passWord').send_keys('aAbb2e33')
# driver.find_element_by_id('btnSub').click()
# FYL140701账号登录
# driver.find_element_by_id('userName').clear()
# driver.find_element_by_id('userName').send_keys('FYL140701')
# driver.find_element_by_id('passWord').clear()
# driver.find_element_by_id('passWord').send_keys('aAbb2e33')
# driver.find_element_by_id('btnSub').click()
# LYJ051228账号登录
driver.find_element_by_id('userName').clear()
driver.find_element_by_id('userName').send_keys('LYJ051228')
driver.find_element_by_id('passWord').clear()
driver.find_element_by_id('passWord').send_keys('aAbb2e33')
driver.find_element_by_id('btnSub').click()
# FYX100514账号登录
# driver.find_element_by_id('userName').clear()
# driver.find_element_by_id('userName').send_keys('FYX100514')
# driver.find_element_by_id('passWord').clear()
# driver.find_element_by_id('passWord').send_keys('aAbb2e33')
# driver.find_element_by_id('btnSub').click()


sleep(1)
driver.find_element_by_id('searchParam').send_keys('领美')
sleep(1)
driver.find_element_by_xpath('//*[@id="maincontainer"]/div[2]/div/div[1]/div/div/span/a').click()
sleep(1)
driver.find_element_by_partial_link_text('领美券促销列表').click()
sleep(1)
driver.switch_to.frame('main_frame1')
sleep(1)
#新增外销券
driver.find_element_by_xpath('//*[@id="search_form"]/div/div[5]/div[1]/button[2]').click()
sleep(1)
#促销名称
driver.find_element_by_id('caseName').send_keys('礼包-美券')
# sleep(1)
#券类型 1.美券 2.营销券

#促销类型 1.单张券 3.礼包券
#1.单张券
# driver.find_element_by_xpath('//*[@id="caseType"]/option[1]').click()
#2.礼包券
driver.find_element_by_xpath('//*[@id="caseType"]/option[2]').click()
#领券时间 1.开始时间 2.结束时间
js = '''var element = document.querySelectorAll("input[readonly='readonly']");
for(var i = 0;i < element.length; i++)
{
element[i].readOnly = false;
}'''
driver.execute_script(js)
#1.开始时间
# driver.find_element_by_id('startTime').send_keys('2019-10-21 00:00:00')
# sleep(1)
# #2.结束时间
# driver.find_element_by_id('endTime').send_keys('2019-10-21 23:59:59')
# sleep(5)
#设置会员等级 默认为不需要
#=G1
# driver.find_element_by_xpath('//*[@id="framebody"]/div/div[2]/table/tbody/tr[5]/td[2]/label[2]/input').click()
# #>=G2
# driver.find_element_by_xpath('//*[@id="framebody"]/div/div[2]/table/tbody/tr[5]/td[2]/label[3]/input').click()
# #>=G3
# driver.find_element_by_xpath('//*[@id="framebody"]/div/div[2]/table/tbody/tr[5]/td[2]/label[4]/input').click()
# #>=G4
# driver.find_element_by_xpath('//*[@id="framebody"]/div/div[2]/table/tbody/tr[5]/td[2]/label[5]/input').click()
# #>=G5
# driver.find_element_by_xpath('//*[@id="framebody"]/div/div[2]/table/tbody/tr[5]/td[2]/label[6]/input').click()
# #不需要
# driver.find_element_by_xpath('//*[@id="framebody"]/div/div[2]/table/tbody/tr[5]/td[2]/label[1]/input').click()
#发放中心 1.业务/运营 2.国美管家 3.客服中心
#1.业务/运营
driver.find_element_by_xpath('//*[@id="distributionCenterTd"]/label[1]/input').click()
#2.国美管家
# driver.find_element_by_xpath('//*[@id="distributionCenterTd"]/label[2]/input').click()
#3.客服中心
# driver.find_element_by_xpath('//*[@id="distributionCenterTd"]/label[3]/input').click()
#获取路劲 1.扫码领券 2.其它渠道领券
#1.扫码领券
driver.find_element_by_xpath('//*[@id="getPatchTd"]/label[1]/input').click()
#2.其它渠道领券
driver.find_element_by_xpath('//*[@id="getPatchTd"]/label[3]/input').click()
#是否验证手机 1.不需要 2.需要
#2.需要
# driver.find_element_by_xpath('//*[@id="framebody"]/div/div[2]/table/tbody/tr[11]/td[2]/label[2]/input').click()
# #1.不需要
# driver.find_element_by_xpath('//*[@id="framebody"]/div/div[2]/table/tbody/tr[11]/td[2]/label[1]/input').click()
#单个用户可领数量
driver.find_element_by_xpath('//*[@id="userCount"]').send_keys('10')
#券份数
driver.find_element_by_xpath('//*[@id="couponCount"]').send_keys('10')
#1.开始时间
driver.find_element_by_id('startTime').send_keys('2019-10-22 00:00:00')
# sleep(1)
#2.结束时间
driver.find_element_by_id('endTime').send_keys('2019-10-22 23:59:59')
# sleep(5)
#增加
driver.find_element_by_xpath('//*[@id="gomeCoupon"]/div[1]/button[3]').click()
#券规则 1.美券 2.营销券
#1.美券
driver.find_element_by_xpath('//*[@id="gomeCoupon"]/div[1]').find_element_by_class_name('input-medium').click()
# sleep(2)
driver.switch_to.frame('coupon_rule_frame')
sleep(1)
driver.find_element_by_xpath('//*[@id="framebody"]/div[1]/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/button[2]').click()
#2.营销券

# 释放iframe，重新回到主页面上
driver.switch_to.default_content()
# sleep(2)
#切换到当前iframe
driver.switch_to.frame('main_frame1')
# sleep(2)
#单次可领x张
driver.find_element_by_xpath('//*[@id="gomeCoupon"]/div[1]').find_element_by_css_selector('#count').send_keys('1')

sleep(2)
#美券
#1.美券
driver.find_element_by_xpath('//*[@id="gomeCoupon"]/div[2]').find_element_by_class_name('input-medium').click()
# sleep(2)
driver.switch_to.frame('coupon_rule_frame')
sleep(1)
driver.find_element_by_xpath('//*[@id="framebody"]/div[1]/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[9]/div/button[2]').click()
# 释放iframe，重新回到主页面上
driver.switch_to.default_content()
# sleep(2)
#切换到当前iframe
driver.switch_to.frame('main_frame1')
sleep(2)
#单次可领x张
driver.find_element_by_xpath('//*[@id="gomeCoupon"]/div[2]').find_element_by_css_selector('#count').send_keys('2')
sleep(1)
# 释放iframe，重新回到主页面上
driver.switch_to.default_content()
# sleep(2)
#切换到当前iframe
driver.switch_to.frame('main_frame1')
sleep(2)
#增加
driver.find_element_by_xpath('//*[@id="gomeCoupon"]/div[1]/button[3]').click()
sleep(1)
#保存
driver.find_element_by_xpath('//*[@id="addFormBtn"]').click()
sleep(1)

#清空
# driver.find_element_by_xpath('//*[@id="framebody"]/div/div[2]/div[2]/div/button[2]').click()
#返回列表
# driver.find_element_by_xpath('//*[@id="framebody"]/div/div[2]/div[2]/div/button[3]').click()









