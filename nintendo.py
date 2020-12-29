from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os

print ("Connecting...")


opt = Options()
opt.headless = True
browser = Chrome(options=opt)
browser.get("https://www.nintendo.com/games/nintendo-switch-new-releases/")


try:
    check = browser.find_element_by_id("header")
    print("Successfully Connected to Nintendo.com" + "\n")
except NoSuchElementException:
    print("Unable to connect" + "\n")

os.system('clear')

#table = browser.find_elements_by_xpath("//*[@id='main']/div[3]/div/div[1]")
#table = browser.find_elements_by_xpath("//*[@id='main']/div[3]/div/div[1]/game-tile[1]/h3")

new = "Nintendo: New Releases ( Top 15 )"
print(new.center(45) + "\n")
for x in range(20):
    x += 1
    table = browser.find_elements_by_xpath("//*[@id='main']/div[3]/div/div[1]/game-tile[" + str(x) + "]/h3")
    for item in table:
        print(item.text)
    

