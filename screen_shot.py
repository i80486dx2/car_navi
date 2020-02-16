import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# url(任意の検索結果)
url_str = "https://www.google.co.jp/maps/dir/%E9%83%A1%E5%B1%B1%E9%A7%85%E3%80%81%E3%80%92963-8003+%E7%A6%8F%E5%B3%B6%E7%9C%8C%E9%83%A1%E5%B1%B1%E5%B8%82%E5%AD%97%E7%87%A7%E7%94%B0/%E6%9D%B1%E4%BA%AC%E9%A7%85%E3%80%81%E3%80%92100-0005+%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%8D%83%E4%BB%A3%E7%94%B0%E5%8C%BA%E4%B8%B8%E3%81%AE%E5%86%85%EF%BC%91%E4%B8%81%E7%9B%AE/@36.5571801,139.0720946,8z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x60206c8736345d81:0xd361d50391bb0a9d!2m2!1d140.3881291!2d37.3981956!1m5!1m1!1s0x60188bfbd89f700b:0x277c49ba34ed38!2m2!1d139.7671248!2d35.6812362!3e0?hl=ja"
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# urlからページを取得する
driver.get(url_str)

# すぐにスクリーンショットを撮ると検索結果が撮影されない(Seleniumによる操作のため)
time.sleep(10)
# スクリーンショット
driver.save_screenshot("./screen_shot.png")
driver.quit()