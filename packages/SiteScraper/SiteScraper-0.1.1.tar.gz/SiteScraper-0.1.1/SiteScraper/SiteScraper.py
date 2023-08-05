from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
class yt_vedio():
       
    def yt_vedios_data(self, url,browser='Chrome'):
        if browser=='Chrome' or browser=='chrome':
            driver = webdriver.Chrome()
            self.url = url
            try:
                driver.get(self.url)
                
                prev_h = 0
                while True:
                    height = driver.execute_script('''
                        return Math.max(
                        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                        );''')
                    driver.execute_script(f"window.scrollTo({prev_h},{prev_h+500})")
                    time.sleep(3)
                    prev_h += driver.execute_script('return window.innerHeight;')
                    if prev_h >= height:
                        break

                videos = driver.find_elements(By.XPATH, '//*[@id="contents"]')
                title = list()
                views = list()
                when = list()
                for vedio in videos:
                    title.append(vedio.find_element(By.ID, 'video-title').text)
                    views.append(vedio.find_element(
                        By.XPATH, './/*[@id="metadata-line"]/span[1]').text)
                    when .append(vedio.find_element(
                        By.XPATH, './/*[@id="metadata-line"]/span[2]').text)
                    

                list_of_dic = {'title': title, 'views': views, 'when': when}
                
                driver.quit()
                return list_of_dic
            except:
                driver.quit()
                logging.error("Invalid url")
            
        else:
            driver = webdriver.Firefox()
            self.url = url
            try:
                driver.get(self.url)
                
                prev_h = 0
                while True:
                    height = driver.execute_script('''
                        return Math.max(
                        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                        );''')
                    driver.execute_script(f"window.scrollTo({prev_h},{prev_h+500})")
                    time.sleep(3)
                    prev_h += driver.execute_script('return window.innerHeight;')
                    if prev_h >= height:
                        break

                videos = driver.find_elements(By.XPATH, '//*[@id="contents"]')
                title = list()
                views = list()
                when = list()
                for vedio in videos:
                    title.append(vedio.find_element(By.ID, 'video-title').text)
                    views.append(vedio.find_element(
                        By.XPATH, './/*[@id="metadata-line"]/span[1]').text)
                    when .append(vedio.find_element(
                        By.XPATH, './/*[@id="metadata-line"]/span[2]').text)
                    

                list_of_dic = {'title': title, 'views': views, 'when': when}
                
                driver.quit()
                return list_of_dic
            except:
                driver.quit()
                logging.error("Invalid url")
    def yt_vedio_comment(self,url,browser='Chrome'):
        if browser=='Chrome' or browser=='chrome':
            driver = webdriver.Chrome()
            self.url = url
            try:
                driver.get(url)
                time.sleep(5)
                prev_h = 0
                while True:
                    #Returns the page length dynamically
                    height = driver.execute_script('''
                            return Math.max(
                        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                        );
                        ''')
                    driver.execute_script(f"window.scrollTo({prev_h},{prev_h+600})")
                    time.sleep(3)
                    prev_h += driver.execute_script('return window.innerHeight;')
                    if prev_h >= height:
                        break
                comments_text = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
                # print(elements)
                txt=list()
                for element in comments_text:
                    txt.append(element.text)
                comment_likes=driver.find_elements(By.XPATH,'//*[@id="vote-count-middle"]')
                likes=list()
                for element in comment_likes:
                    likes.append(element.text)
                time_posted=list()
                comment_time=driver.find_elements(By.XPATH,'//*[@id="header-author"]/yt-formatted-string/a')
                for element in comment_time:
                    time_posted.append(element.text)
                dic={'comment_text':txt,'likes':likes,'comment_time':time_posted}
                
                driver.quit()
                return dic

            except:
                driver.quit()
                logging.error('Invalid url')
        else: 
            driver = webdriver.Firefox()
            self.url = url
            try:
                driver.get(url)
                time.sleep(5)
                prev_h = 0
                while True:
                    #Returns the page lenght dynamically
                    height = driver.execute_script('''
                            return Math.max(
                        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                        );
                        ''')
                    driver.execute_script(f"window.scrollTo({prev_h},{prev_h+500})")
                    time.sleep(3)
                    prev_h += driver.execute_script('return window.innerHeight;')
                    if prev_h >= height:
                        break
                comments_text = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
                # print(elements)
                txt=list()
                for element in comments_text:
                    txt.append(element.text)
                comment_likes=driver.find_elements(By.XPATH,'//*[@id="vote-count-middle"]')
                likes=list()
                for element in comment_likes:
                    likes.append(element.text)
                time_posted=list()
                comment_time=driver.find_elements(By.XPATH,'//*[@id="header-author"]/yt-formatted-string/a')
                for element in comment_time:
                    time_posted.append(element.text)
                dic={'comment_text':txt,'likes':likes,'comment_time':time_posted}
                
                driver.quit()
                return dic

            except:
                driver.quit()
                logging.error('Invalid url')
