from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
# def break_down(driver):
#     container = {}
#     try:
#         artist_ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[3]/h2/b')
#         container['artist'] = artist_ele.text.replace(" Lyrics", "")
#         song_name = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/b')
#         container['song name'] = song_name.text

#         lyrics_ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[5]')
#         container['lyrics'] = lyrics_ele.text.replace('\n', ' ')

#         writer_ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[10]/small')
#         container['writer(s)'] = writer_ele.text

#         album_ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[12]/div[1]/b')
#         container['album'] = album_ele.text
#     except:
#         time.sleep(0.5)
#     return container
def main():
    df = pd.read_csv("data\Links.csv")
    webdriver_path = "C:\Program Files\ChromeDriver\chromedriver.exe"

    link_contents = list(df[df.columns[1]])
    print(len(link_contents))

    
    page_contents = []
    for lnk_url in link_contents[3380:]:
        container = {}
        driver = webdriver.Chrome(webdriver_path)
        driver.maximize_window()
        driver.get(lnk_url)
        time.sleep(2)
        try:
            time.sleep(2)
            artist_ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[3]/h2/a/b')
            container['artist'] = artist_ele.text.replace(" Lyrics", "")
            song_name = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/b')
            container['song name'] = song_name.text

            lyrics_ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[5]')
            container['lyrics'] = lyrics_ele.text.replace('\n', ' ')

            writer_ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[10]/small')
            container['writer(s)'] = writer_ele.text

            album_ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[12]/div[1]/b')
            container['album'] = album_ele.text
            print(artist_ele.text.replace(" Lyrics", ""))
            
            time.sleep(1)

        except:
            time.sleep(1)
            # break_down(driver)
        page_contents.append(container)
        df = pd.DataFrame(data=page_contents, columns = page_contents[0].keys())
        df.to_csv("data\df13.csv", index=False)
        driver.close()
        
    # print(page_contents)


if __name__ == "__main__":
    main()