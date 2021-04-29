from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('https://itmscoaching.herokuapp.com/form')
driver.find_element_by_id('first-name').send_keys('Binh')
driver.find_element_by_id('last-name').send_keys('Nguyen')
driver.find_element_by_id('job-title').send_keys('Tester')
driver.find_element_by_id('radio-button-3').click()
driver.find_element_by_id('checkbox-2').click()
driver.find_element_by_xpath('//*[@id="select-menu"]/option[4]').click()
driver.find_element_by_id('datepicker').click()
driver.find_element_by_class_name('datepicker-switch').click()
prev_button = driver.find_element_by_css_selector('.datepicker-months .prev')
for i in range (0, 2021 - 2011):
    prev_button.click()
driver.find_element_by_xpath('/html/body/div[2]/div[2]/table/tbody/tr/td/span[7]').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[4]/td[4]').click()
driver.find_element_by_link_text('Submit').click()
driver.quit()