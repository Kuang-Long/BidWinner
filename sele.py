from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 設置瀏覽器驅動路徑
# driver_path = 'chromedriver-win32/chromedriver.exe' # 替換為你的 WebDriver 路徑
driver = webdriver.Chrome()

# 打開目標網頁
driver.get('https://wmc.kcg.gov.tw/Home/Login')

# 找到表單字段並填入數據
input_element = driver.find_element(By.NAME, 'UnitCode')
input_element.send_keys('your_value')

input_element = driver.find_element(By.NAME, 'UnitCode')
input_element.send_keys('your_value')


# 關閉瀏覽器
# driver.quit()
