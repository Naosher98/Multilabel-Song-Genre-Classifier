from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys

def main():
    df = pd.read_csv("data3\merged_df.csv")
    # df = df.dropna(axis = 0)
    artist_names = list(df[df.columns[0]])
    song_names = list(df[df.columns[1]])
    lyrics_names = list(df[df.columns[2]])
    

    url = "https://www.chosic.com/music-genre-finder/"
    webdriver_path = "C:\Program Files\ChromeDriver\chromedriver.exe"
    driver = webdriver.Chrome(webdriver_path)
    driver.maximize_window()
    driver.get(url)

    page_contents = []
    K = 8093
    version = 11
    for i in range(K, 10547):
        content = {}
        try:
            content['artist'] = artist_names[i]
            content['song'] = song_names[i]
            content['lyrics'] = lyrics_names[i]
            m = driver.find_element(By.NAME, "q")
            #enter search text
            time.sleep(5)
            m.send_keys(artist_names[i] +' '+ song_names[i])
            
            # m.send_keys(Keys.ENTER)
       
        
            time.sleep(3)
            sug_ele = driver.find_element(By.ID, "form-suggestions")
            first_ele = sug_ele.find_element(By.ID, 'hh1')
            actions = ActionChains(driver)
            time.sleep(2)
            actions.click(first_ele).perform()
            
            time.sleep(2)
            sp_ele = driver.find_element(By.CLASS_NAME, 'spotify-result')
            gerne_ele = sp_ele.find_element(By.XPATH, '//div[contains(@class,"pl-tags ") and contains(@class,"tagcloud")]')
            tag_ele = gerne_ele.find_elements(By.TAG_NAME, 'a')
            li = [] 
            for i in tag_ele:
                li.append(i.text.replace('\n', ''))
            content['gerne spotify']= li
            gerne_ele_wiki = driver.find_element(By.ID, 'wiki-genres')
            tag_ele_wiki = gerne_ele_wiki.find_elements(By.TAG_NAME, 'a')
            li2 = [] 
            for i in tag_ele_wiki:
                li2.append(i.text.replace('\n', ''))
           
            content['gerne wiki']= li2
            
        except:
            time.sleep(10)
            continue
        
        driver.find_element(By.NAME, "q").clear()
        page_contents.append(content)
        df = pd.DataFrame(data=page_contents,  columns = page_contents[0].keys())
        df.to_csv(f"data3\main_{version}.csv")
        time.sleep(2)
    
    driver.close()

if __name__ == "__main__":
    main()