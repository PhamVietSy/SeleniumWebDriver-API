from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('http://practice.automationtesting.in/')
driver.find_element_by_link_text('My Account').click()
driver.find_element_by_id('reg_email').send_keys('abc@gmail.com')
driver.find_element_by_id('reg_password').send_keys('abc123')
driver.find_element_by_name('register').click()
driver.quit()