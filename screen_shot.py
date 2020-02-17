import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time

dest1 = "37.3980187,140.3879142" #郡山
dest2 = "37.5242475,139.9404067" #会津
# url(任意の検索結果)
url_str = "https://www.google.com/maps/dir/?api=1&origin={}&destination={}&travelmode=driving".format(dest1,dest2)
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
img = Image.open('screen_shot.png')
w, h = img.size
img = img.resize((int(w/2), int(h/2)))
cropped_img = img.crop((410,100, 800, 500))
print(img.size)
cropped_img.save('screen_shot.gif')