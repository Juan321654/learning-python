from selenium import webdriver

# https://chromedriver.storage.googleapis.com/index.html?path=95.0.4638.54/
# to download chrome drivers

chrome_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/HAVIT-Rainbow-Backlit-Gaming-Keyboard/dp/B016Y2BVKA/ref=sr_1_2_sspa?crid=1A0TMSAGVHBTS&dchild=1&keywords=keyboard&qid=1635981762&sprefix=keyboard%2Caps%2C64&sr=8-2-spons&psc=1&smid=A3TJEO884AOUB3&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUU9DUEo2UDlXV1BTJmVuY3J5cHRlZElkPUEwNDA0OTQ3MTQyVDlLTU9WTDcxMCZlbmNyeXB0ZWRBZElkPUEwMDI3MDQxMVBSTlIwOFNKRFg5USZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
# price = driver.find_element_by_class_name("a-price")
# print(price.text) # 27.99

driver.get("https://www.python.org/")
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
  events[n] = {
    "time": event_times[n].text,
    "name": event_times[n].text
  }

print(events)

# driver.close()
driver.quit()
