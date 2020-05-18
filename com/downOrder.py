from selenium import webdriver
from time import sleep

executable_path='/Users/oulingling/Desktop/Tools/chromedriver/80/chromedriver'
driver = webdriver.Chrome(executable_path)
# driver = webdriver.Chrome()
#国美账号和密码
username = '13691246710'
password = 'qwert12345'
# 国美登录
driver.get('http://login.atguat.com.cn/login?intcmp=sy-public01035&type=logout')
driver.maximize_window()
sleep(1)

jsLogin="var q=document.getElementById('tabRight').click()"
driver.execute_script(jsLogin)
sleep(5)



# driver.find_element_by_css_selector('#loginNameDiv').send_keys('1111')
# driver.find_element_by_id('loginNameDiv').send_keys(username)
# driver.find_element_by_id('loginPasswordDiv').send_keys(password)
# driver.find_element_by_xpath('//*[@id="loginNameDiv"]').send_keys(username)
# driver.find_element_by_xpath('//*[@id="loginPasswordDiv"]').send_keys(password)
# driver.find_element_by_xpath('//*[@id="frm"]/div/div[5]/input[5]').click()
sleep(8)
# 要下单的商品
driver.get('http://item.atguat.com.cn/9200057602-1000217668.html')
driver.maximize_window()

# 加入购物车
js = "var q=document.documentElement.scrollTop=100"
driver.execute_script(js)
sleep(2)
js2="var q=document.getElementById('addCart').click()"
driver.execute_script(js2)
sleep(2)
#切换页面
now_handle = driver.current_window_handle
print(now_handle)
all_handle = driver.window_handles
print(all_handle)
driver.switch_to.window(all_handle[1])

# 进入我的购物车
driver.find_element_by_id('hdrcarttext').click()
sleep(3)
#去结算
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div/div[6]/a').click()
#提交订单
js3 = "var q=document.documentElement.scrollTop=100000"
driver.execute_script(js3)
sleep(3)
driver.find_element_by_xpath('//*[@id="id_commit"]').click()
sleep(2)
#获取支付单号
paymentId=driver.find_element_by_xpath('//*[@id="orderInfo_PTSYT"]/div[1]/h3/i').text
print(paymentId)
sleep(2)
#付款
paymentUrl='http://10.115.2.178:3123/testPayment.do?payType=1&pReqNo='+paymentId+'&payModel=0&accountCode=YA'
driver.get(paymentUrl)

