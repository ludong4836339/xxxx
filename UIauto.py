from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
# d.get(url='https://music.163.com/')
d.get("http://bj.ganji.com/")
d.maximize_window()
d.implicitly_wait(10)
# d.find_element(By.PARTIAL_LINK_TEXT,"登录").click()
# d.find_element(By.PARTIAL_LINK_TEXT,"选择其他登录模式").click()
# d.find_element(By.ID,'j-official-terms').click()
# d.find_element(By.PARTIAL_LINK_TEXT,"QQ登录").click()
# handle=d.window_handles
# d.switch_to.window(handle[1])
# print(handle)
# print(d.title)

#  切换句柄
d.find_element(By.LINK_TEXT,"手机上赶集").click()
h=d.window_handles
print(h)
d.switch_to.window(h[1])
print(d.title)
print(d.current_window_handle)
d.quit()
print(d.current_window_handle)
# d.save_screenshot("C:\\Users\小可爱\Desktop\1")
d.get_screenshot_as_file('/Screenshots/foo.png')

# d.find_element(by=By.LINK_TEXT,value="登录").click()
sleep(10)
# print(d.title)
# assert  "百度" in d.title