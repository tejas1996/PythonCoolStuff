import requests
from bs4 import BeautifulSoup

def crawler(depth):
    page = 0
    while page < depth:
        url = "http://www.deepakvadgama.com/"
        source = requests.get(url)
        text = source.text
        soupObject = BeautifulSoup(text)
        for rows in soupObject.findAll('a'):
            link = rows.get('href')
            print(link)
            getData(link)

        page += 1

def getData(url):
    if('www.deepakvadgama.com' in url):
        source = requests.get(url)
        text = source.text
        soupObject = BeautifulSoup(text)
        print("printing for url " + url)
        for item in soupObject.findAll('p'):
            print(item.text)


crawler(2)