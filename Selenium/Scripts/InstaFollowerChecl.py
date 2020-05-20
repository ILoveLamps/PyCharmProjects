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
        self.followers = []
        self.following = []
        self.main()

        self.get_unfollowers()

    def main(self):
        # # Insert Username
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
            .send_keys(self.username)

        # # Insert password
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')\
            .send_keys(self.password)

        # # Press Log In
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')\
            .click()
        sleep(5)

        # # Press Not now
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')\
            .click()
        sleep(1)

        # # Clicking on username
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(5)

        # # Getting followers and following
        self.get_followers()
        self.get_following()

    def get_followers(self):
        # # Clicking on followers
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        sleep(1)

        self.followers = self.get_names()

    def get_following(self):
        # # Clicking on followers
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sleep(1)

        self.following = self.get_names()

    def get_names(self):
        # # Position mouse inside scroll box
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div")
        self.mouse.position = (980, 538)
        self.mouse.click(Button.left, 1)
        sleep(2)

        # # Scrolling to bottom - try to use javascript for this
        for x in range(100):
            self.mouse.scroll(0, -100)
            sleep(0.2)
        sleep(2)

        # # Extract names
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        # # Close scroll window
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button')\
            .click()

        return names

    def get_unfollowers(self):
        # unfollowers = [user for user in self.following if user not in self.followers]
        unfollowers = [user for user in self.followers if user not in self.following]
        print(unfollowers)


if __name__ == "__main__":
    bot = InstaBot('hirdayesh5987', '')
