from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import re
def main():
    page_contents = []
    for i in range(6):
        
        url = f"https://www.rockarchive.com/artists?page={i+1}"
        webdriver_path = "C:\Program Files\ChromeDriver\chromedriver.exe"
        driver = webdriver.Chrome(webdriver_path)
        driver.maximize_window()
        driver.get(url)
        
        container_ele = driver.find_element(By.XPATH, '//div[contains(@class,"tm-padded-small") and contains(@class,"uk-margin-small-bottom")]')
        des_ele = container_ele.find_elements(By.CLASS_NAME, 'description')
        # print(len(des_ele))
        time.sleep(3)
        for j in range(len(des_ele)):
            # print(des_ele[j].text.split("\n"))
            contents = {}
            contents['artists'] = des_ele[j].text.split("\n")[0]
            contents['artists description'] = des_ele[j].text.split("\n")[1]
            page_contents.append(contents)
        df = pd.DataFrame(data=page_contents, columns = page_contents[0].keys())
        df.to_csv("data\info_artists.csv", index=False)
    
        
        time.sleep(5)




    
        driver.close()
    print(contents)
if __name__ == "__main__":
    main()