from bs4 import BeautifulSoup
import shutil
import requests
import os


def image_downloader(url):

    url = requests.get(url)
    source_code = url.text
    soup = BeautifulSoup(source_code, 'html.parser')
    temp = soup.title.string + ".jpg"
    if temp not in os.listdir():
        image_link = soup.find('img', {'id': 'img'}).get('src')
        r = requests.get(image_link, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open(temp, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

def downloader(url):
    base = url[:url.rfind('/')]
    link = requests.get(url)
    source_code = link.text
    soup = BeautifulSoup(source_code,'html.parser')
    temp = soup.find(string = "Next")
    while temp != None:
        image_downloader(url)
        url = "http://www.mangareader.net" +  soup.find(string = "Next").find_parent('a').get('href')
        print(url )
        link = requests.get(url)
        source_code = link.text
        soup = BeautifulSoup(source_code,'html.parser')



downloader("http://www.mangareader.net/attack-on-titan-before-the-fall/25")



 # image_downloader('http://www.mangareader.net/world-trigger/148', r'C:\Users\Acer\PycharmProjects\Web Crawler\Test')