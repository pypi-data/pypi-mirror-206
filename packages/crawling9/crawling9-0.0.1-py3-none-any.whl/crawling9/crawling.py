from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
    
def get_comments(url, find, wait_time=5, delay_time=0.1):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage') 
    driver = webdriver.Chrome('chromedriver', options=options)
    print(1)
    
    driver.implicitly_wait(wait_time)
    
    driver.get(url)
    
    while True:
        
        try:
            more = driver.find_element(By.CSS_SELECTOR,'a.u_cbox_btn_more')
            more.click()
            time.sleep(delay_time)
            
        except:
            print("hi")
            break


    html = driver.page_source

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml') #html.parser

    contents = soup.select(find)
    list_contents = [content.text for content in contents]

    list_sum = list(zip(list_contents))
    driver.quit()
  
    return list_sum

def get_excel(col,comments,filename):
  df = pd.DataFrame(comments, columns=col)
  df.to_excel(str(filename), sheet_name='comment')