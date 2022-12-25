from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

elem = driver.find_element_by_name("q")


elem.send_keys("고태광")

elem.send_keys(Keys.RETURN)


SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(
                "#islmp > div > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input").click()

        except:
            break
    last_height = new_height


images = driver.find_elements_by_css_selector(".bRMDJf.islir")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgurl = driver.find_element_by_css_selector(
            "div.qdnLaf.isv-id.b0vFpe > div > a > img").get_attribute("src")
        count = count + 1
        urllib.request.urlretrieve(imgurl, str(count)+".jpg")
    except:
        pass


driver.close()
