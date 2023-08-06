import os
import requests 
from bs4 import BeautifulSoup 

# needed for google search
def download_google_images(search, n_images):

        
    # download first n images from google image search
    GOOGLE_IMAGE = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'


    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }

    # Creating images foleder if not exists
    if not os.path.exists('images'):
        os.mkdir('images')

    #Crating search url for search input
    searchurl = GOOGLE_IMAGE + 'q=' + search

    #getting link
    response = requests.get(searchurl, headers=usr_agent)

    #Finding image in html
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('img', {'class': 'yWs4tf'}, limit=n_images)

    #storing each image in images folder
    for i,img in enumerate(results):
        res= requests.get(img['src'])
        img_name = 'images' + '/' + search + str(i+1) + '.png'
        with open(img_name, 'wb') as f:
            f.write(res.content)
        