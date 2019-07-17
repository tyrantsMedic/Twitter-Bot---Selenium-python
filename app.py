import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()


    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        print('Logging in')
        email = bot.find_element_by_class_name('text-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        print("logged in")

    def like(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    print("liked tweet")
                    time.sleep(5)
                except Exception as ex:
                    print('Did not work! Trying again in a minute')
                    time.sleep(20)


hamza = TwitterBot('Your Email', 'Your password') #Enter your email and password here
hamza.login()
hamza.like(input("Enter a hashtag: #"))
 