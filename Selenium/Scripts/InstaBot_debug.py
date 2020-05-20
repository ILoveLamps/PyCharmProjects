from selenium import webdriver
from pynput.mouse import Button, Controller
from time import sleep


driver = webdriver.Chrome('C:\\Users\hirda\Documents\PyCharmProjects\Selenium\chromedriver.exe')
mouse = Controller()

driver.maximize_window()
driver.get('https://www.instagram.com/')
sleep(2)

username = 'hirdayesh5987'
password = 'D@ddy275641!'

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
    .send_keys(username)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')\
    .send_keys(password)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')\
    .click()
sleep(5)

driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')\
    .click()
sleep(1)

driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(username))\
    .click()
sleep(5)

driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
    .click()
sleep(3)


