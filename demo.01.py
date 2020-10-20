from selenium import webdriver
driver = webdriver.Chrome()
# 输入网址
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("G2Bent")

driver.find_element_by_id("su").click()

driver.close()