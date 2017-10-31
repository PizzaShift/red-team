# from https://stackoverflow.com/questions/20150184/make-a-list-of-all-the-files-on-a-website
from bs4 import BeautifulSoup
import requests

def find_files(url):

    soup = BeautifulSoup(requests.get(url).text,"lxml")

    for a in soup.find_all('a'):
        yield a['href']

for link in find_files("http://10.66.28.202:8230"):
    print(link)
