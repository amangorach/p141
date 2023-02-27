from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("C:/Users/rahil/Downloads/New folder/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)
star_data = []

def scrape():
    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for tr_tag in soup.find_all("tr",attrs = {"tr"}):
            td_tags =tr_tag.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
        browser.find_element(by = By.XPATH,value='//*[@id="mw-content-text"]/div[1]/table/thead/tr/th[2]').click()
            
scrape()

headers = ["Name", "Distance", "Mass", "Radius"]

star_df1 = pd.DataFrame(star_data,columns = headers)
star_df1.to_csv('scraped.csv',index = True, index_label = "id")
