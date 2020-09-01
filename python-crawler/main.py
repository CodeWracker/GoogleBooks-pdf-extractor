from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
url = input('Link do Google Books: ')
options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path=r'geckodriver')

driver.get(url)
time.sleep(2)
driver.find_element_by_class_name('gback').click()
SCROLL_PAUSE_TIME = 0.5

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
        break
    last_height = new_height
pages = driver.find_elements_by_xpath('//img')
for page in pages:
    print(page.get_attribute('src'))