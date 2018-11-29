import requests
from bs4 import BeautifulSoup
import csv

#TODO: un-hardcode, make different functions for different parameters
url = 'https://terrasect.com/'
r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, 'lxml')

links = soup.find_all('a')
links = [a.get('href') for a in soup.find_all('a', href=True)]
#print(links)

def RunScraper():
	url = 'https://terrasect.com/'
	r = requests.get(url)
	html_content = r.text
	soup = BeautifulSoup(html_content, 'lxml')

	links = soup.find_all('a')
	links = [a.get('href') for a in soup.find_all('a', href=True)]
	#print(links)
	

	

	