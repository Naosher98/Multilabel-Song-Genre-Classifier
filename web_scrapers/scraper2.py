from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys

def main():
    df = pd.read_csv("data\info_artists.csv")
    artist_names = list(df[df.columns[0]])
    # print(artist_names)

    url = "https://www.azlyrics.com/"
    webdriver_path = "C:\Program Files\ChromeDriver\chromedriver.exe"
    driver = webdriver.Chrome(webdriver_path)
    driver.maximize_window()
    driver.get(url)

    link_contents = []
    for artist_name in artist_names[:]:
        m = driver.find_element(By.NAME, "q")
        #enter search text
        m.send_keys(artist_name)
        time.sleep(1)
        m.send_keys(Keys.ENTER)
        time.sleep(5)

        try:
            more_ele = driver.find_element(By.XPATH, '//a[contains(@class,"btn") and contains(@class,"btn-primary")]')
            actions = ActionChains(driver)
            actions.click(more_ele).perform()
            time.sleep(1)
            for j in range(20):
                song_eles = driver.find_elements(By.XPATH, '//td[contains(@class,"text-left") and contains(@class,"visitedlyr")]')  
                for row in song_eles:
                    lnk = row.find_element(By.TAG_NAME, 'a')
                    link_contents.append(lnk.get_attribute('href'))
                    time.sleep(0.5)
                next_ele = driver.find_element(By.XPATH, '//span[contains(@class,"glyphicon") and contains(@class,"glyphicon-chevron-right")]') 
                actions = ActionChains(driver)
                actions.click(next_ele).perform()
                time.sleep(2)
        except:
            time.sleep(1)
        driver.find_element(By.NAME, "q").clear()
        df = pd.DataFrame(data=link_contents)
        df.to_csv("data\Links.csv")
        time.sleep(1)
    print(len(link_contents))
    
    time.sleep(3)
    driver.close()

if __name__ == "__main__":
    main()