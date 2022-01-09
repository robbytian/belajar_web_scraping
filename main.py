import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler',params={'tag_from':'wp_cb_mostPopular_more'});
soup = BeautifulSoup(html_doc.text,'html.parser')
populer_area = soup.find('div','grid-row list-content')
titles =populer_area.find_all(attrs={'class':'media__title'})
images = populer_area.find_all(attrs={'class':'media__image'})

for image in images:
    print(image.find('a').find('img')['title    '])
# print(titles)