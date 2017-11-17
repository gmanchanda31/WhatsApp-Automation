from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("/home/pareksha/PycharmProjects/learning_python/drivers/chromedriver")
driver.get("https://web.whatsapp.com/")

time.sleep(15)
search_bar = driver.find_element_by_class_name("input-search")
search_bar.send_keys("shivam")
search_bar.send_keys(Keys.ENTER)

for x in range(72525):
    msg_box = driver.find_element_by_class_name("pluggable-input-body")
    msg_box.send_keys("All the best for papers bro...!!!")
    msg_box.send_keys(Keys.ENTER)

driver.close()
