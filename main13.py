from selenium import webdriver
import time

chrome_driver_path = "/Users/carolinejernigan/Documents/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on.
cookie = driver.find_element_by_id("bigCookie")

#Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes
