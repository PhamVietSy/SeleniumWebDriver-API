from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('https://the-internet.herokuapp.com')
driver.find_element_by_link_text('Form Authentication').click()
driver.find_element_by_id('username').send_keys('tomsmith')
driver.find_element_by_id('password').send_keys('SuperSecretPassword!')
driver.find_element_by_tag_name('button').click()
print(driver.title)
driver.quit()