# Pay Rockwood Oregon Water Bill
__author__ = 'Benjamin Isaacson'
__copyright__ = GPL-3.0

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

ACCOUNT = '222223333'
FIRST_NAME = 'Yours'
LAST_NAME = 'Truly'
ADDRESS = '123 SE 162ND AVE'
CITY = 'Portland'
ZIP = '97233'
STATE = 'or'
PHONE = '5031112222'
EMAIL = 'a@b.c'
CC_NUMBER = '0000123456789012'
EXP = '12/19'
CVV = '123'

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
# Open site
driver.get("https://client.pointandpay.net/web/RockwoodWaterPUD")
# Select "Payment Type"
select = Select(driver.find_element_by_css_selector('.bditProductSelect'))
select.select_by_visible_text('Utility Bill')
# Search for account number
search_field = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr/td/div/table/tbody/tr/td[1]/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/div/div/table/tbody/tr[2]/td/div/input')
search_field.send_keys(ACCOUNT)
search = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr/td/div/table/tbody/tr/td[1]/div/table/tbody/tr[3]/td/div/input')
search.click()
# Add the account's bill to the "cart" and continue and confirm
add_to_cart = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[4]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td[1]/div/table/tbody/tr/td[2]/div/a/nobr')
add_to_cart.click()
continue_button = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td/div/table/tbody/tr/td/div/input')
continue_button.click()
continue_button_2 = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td/div/table/tbody/tr/td/div/input')
continue_button_2.click()
# Fill out payment form
first_name = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[2]/td/div/div/div/input')
first_name.send_keys(FIRST_NAME)
last_name = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td/div/table/tbody/tr/td[2]/div/div/div/table/tbody/tr[2]/td/div/div/div/input')
last_name.send_keys(LAST_NAME)
address = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[2]/td/div/div/div/input')
address.send_keys(ADDRESS)
city = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[6]/td/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[2]/td/div/div/div/input')
city.send_keys(CITY)
state = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[6]/td/div/table/tbody/tr/td[2]/div/div/div/table/tbody/tr[2]/td/div/div/select')
state.send_keys(STATE)
zip_code = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[6]/td/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[2]/td/div/div/div/input')
zip_code.send_keys(ZIP)
phone = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[7]/td/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[2]/td/div/div/div/input')
phone.send_keys(PHONE)
email = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[7]/td/div/table/tbody/tr/td[2]/div/div/div/table/tbody/tr[2]/td/div/div/div/input')
email.send_keys(EMAIL)
card_num = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[10]/td/div/table/tbody/tr/td/div/div/div/table/tbody/tr[2]/td/div/input')
card_num.send_keys(CC_NUMBER)
card_exp = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[11]/td/div/table/tbody/tr/td/div/div/div/table/tbody/tr[2]/td/div/input')
card_exp.send_keys(EXP)
card_cvv = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[12]/td/div/table/tbody/tr/td/div/div/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[1]/div/input')
card_cvv.send_keys(CVV)
continue_button_3 = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td/div/table/tbody/tr/td/div/input')
continue_button_3.click()
# Check confirmation checkbox and click submit payment button
confirmation_box = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr[4]/td/div/table/tbody/tr[1]/td/div/table/tbody/tr/td[1]/div/input[2]')
confirmation_box.click()
submit_payment = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/div/table/tbody/tr[5]/td/div/table/tbody/tr/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[1]/td[3]/div/table/tbody/tr/td/div/table/tbody/tr/td/div/input')
submit_payment.click()
#Wait so you can observe payment summary
input('Press Enter')
driver.quit()
exit()
