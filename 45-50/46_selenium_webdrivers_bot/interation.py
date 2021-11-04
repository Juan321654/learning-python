from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# https://chromedriver.storage.googleapis.com/index.html?path=95.0.4638.54/
# to download chrome drivers

chrome_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a").text
print(article_count)

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)