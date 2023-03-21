from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd


def func(webdriver_path,page_contents, lnk_url):
    # Define the user-agent string
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    # Define the options for the Chrome browser
    options = Options()
    options.add_argument(f'user-agent={user_agent}')

    # Initialize the Chrome browser with the desired options
    driver = webdriver.Chrome(options=options)
    container = {}
    driver.maximize_window()
    driver.get(lnk_url)
    time.sleep(5.5)
    try:
        time.sleep(1)
        artist_ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[3]/h2/a/b')
        container['artist'] = artist_ele.text.replace(" Lyrics", "")
        song_name = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/b')
        container['song name'] = song_name.text

        lyrics_ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[5]')
        container['lyrics'] = lyrics_ele.text.replace('\n', ' ')

        writer_ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[10]/small')
        container['writer(s)'] = writer_ele.text

        
    except:
        pass
    page_contents.append(container)
    time.sleep(0.5)
    driver.quit()
    return page_contents

def main(k, l, m):
    df = pd.read_csv("data\Links.csv")
    webdriver_path = "C:\Program Files\ChromeDriver\chromedriver.exe"

    link_contents = list(df[df.columns[1]])
    print(len(link_contents))

    
    page_contents = []
    for lnk_url in link_contents[k:]:
        l=l+1
        try:
            func(webdriver_path,page_contents, lnk_url)
        except WebDriverException:
            m=m+1
            k=l+k
            print(m, k, l)
            time.sleep(15)
            main(k, l, m)

        df = pd.DataFrame(data=page_contents, columns = page_contents[0].keys())
        df.to_csv(f"data2\df{m}.csv", index=False)
        
        
    # print(page_contents)


if __name__ == "__main__":
    k=10215
    l=0
    m=41
    main(k, l, m)