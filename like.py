from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep
import random
import sys
from random import randint
import screte
import hashtag
import comment


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        # self.chrome_options = Options()
        # self.mobile_emulation = { "deviceName": "Nexus 5" }
        # self.chrome_options.add_experimental_option("mobileEmulation", self.mobile_emulation)
        #chrome_options=self.chrome_options
       
        

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        username_element = driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        sleep(5)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
    
        like_limit= 100
     
        like_counter = 0

        try:
            sleep(random.randint(5, 7))
            hrefs_in_view = driver.find_elements_by_tag_name('a')
            hrefs_in_view = [elem.get_attribute('href')
                             for elem in hrefs_in_view
                             if '/p/' in elem.get_attribute('href')]

            # Removing the top 9 posts.
            hrefs_in_view = hrefs_in_view[0:]

        except Exception as e:
            print(e)

        # Liking photos
        total_photos = len(hrefs_in_view)
        for pic_href in hrefs_in_view:
            driver.get(pic_href)
            sleep(random.randint(1, 3))
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            sleep(random.randint(1, 3))
            driver.execute_script(
                "window.scrollTo(0, -document.body.scrollHeight);")
            try:
                sleep(random.randint(2, 4))
                
            
                comments = comment.comments
	
                

                if like_counter < like_limit:
                    
                    followButton = driver.find_element_by_class_name('fr66n')
                    followButton.click()
                    like_sleep = random.randint(20, 77)
                    print('Image Liked!!')
                    print('Taking a Snap for {0} secs'.format(like_sleep))
                    sleep (like_sleep)
                    like_limit +=1
                    print('Done with liking snap!')

                

                    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').click()
                    print('Comment process Stared')
                    sleep(random.randint(20, 77))
                    print('Preparing Comment')
                    driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(comments[randint(0,10)])
                    sleep(random.randint(20, 107))
                    print('Commented ')
                    print( "Total like and comments :{0} ".format(like_counter+1))
                    
                    driver.find_element_by_xpath("//button[@type='submit']").click()
                    like_counter +=1
                    
                # print( "Total like and comments : " + like_counter)
                total_photos -= 1
                for second in reversed(range(0, random.randint(20, 30))):
                    print_same_line("#" + hashtag + ': unique photos left: ' +
                                    str(total_photos) + " | Sleeping " + str(second) + " | " )
                    sleep(1)

            except Exception as e:
                sleep(2)


if __name__ == "__main__":

    username = screte.user_name
    password = screte.pwd

    ig = InstagramBot(username, password)
    ig.login()

    hashtags = hashtag.hashtags
    

    while True:
        try:
            tag = random.choice(hashtags)
            ig.like_photo(tag)
            
        except Exception:
            ig.closeBrowser()
            sleep(60)
            ig = InstagramBot(username, password)
            ig.login()
