"""
    Compare your following to your followers on instagram
    To Do:
    1. Open instagram.com
    2. Log in to instagram
    3. Get following list
    4. Get followers list
    5. Compare two lists
"""

from selenium import webdriver
from pynput.mouse import Button, Controller
from time import sleep


class InstaBot:
    """
        Opens chrome, logs in to instagram, and extracts
        follower/following lists
    """
    def __init__(self, user, pwd):
        self.driver = webdriver.Chrome('C:\\Users\hirda\Documents\PyCharmProjects\Selenium\chromedriver.exe')
        self.mouse = Controller()

        self.driver.maximize_window()
        self.driver.get('https://www.instagram.com/')
        sleep(2)

        self.username = user
        self. password = pwd
        self.login()

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
            .send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')\
            .send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')\
            .click()
        sleep(4)

        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')\
            .click()
        sleep(1)

        self.get_followers()

    def get_followers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)

        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        sleep(2)

        self.get_names()

    def get_names(self):
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div")
        self.mouse.position = (980, 538)
        self.mouse.click(Button.left, 1)
        sleep(2)

        for x in range(200):
            self.mouse.scroll(0, -100)
            sleep(0.2)


if __name__ == "__main__":
    bot = InstaBot('hirdayesh5987', 'D@ddy275641!')
