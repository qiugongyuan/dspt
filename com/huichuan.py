from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get("http://10.115.2.142:9005/gome3c-web/mng/index.htm")
sleep(1)
driver.maximize_window()
#TNT错误订单处理
driver.find_element_by_xpath('//*[@id="cc"]/div[3]/div/ul[2]/a[1]').click()
sleep(3)

#手工推送订单
driver.switch_to_frame(1)
sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/input[3]').click()
sleep(1)
#输入订单号
driver.find_element_by_xpath('//*[@id="handOrderNum"]').send_keys('JL602570450376')
sleep(1)
#输入订单来源
driver.find_element_by_xpath('//*[@id="handOrderFrom"]').send_keys('LSP')
sleep(1)
#输入订单状态
driver.find_element_by_xpath('//*[@id="handOrderStatus"]').send_keys('DL')
sleep(1)
#确定
driver.find_element_by_xpath('//*[@id="handSentDiv"]/div[2]/a[1]/span').click()
sleep(1)

