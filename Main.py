from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

creator_url = "https://www.youtube.com/"

driver.get(creator_url)

time.sleep(5)

# videos = driver.find_elements(By.XPATH, "//a[@id='video-title-link']")

# for video in videos:
#     title = video.get_attribute("title")
#     url = video.get_attribute("href")

#     print(title)
#     print(url)

driver.quit()