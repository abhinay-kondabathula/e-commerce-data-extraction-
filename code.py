import pandas as pd
import requests
from bs4 import BeautifulSoup


names_list = []
price_list= []
disc_list = []
reviews_list = []

for i in range(2,10):
    url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="+str(i)

    doc = requests.get(url)
    print(doc)
    soup = BeautifulSoup(doc.content,'html.parser')
    ptfy = soup.prettify()
        # print(url)

    # while True:
    # link = soup.find('a',class_='page-link').get('href')
    # full_link = 'https://webscraper.io'+link
    # print(full_link)

        # url = full_link
        # doc = requests.get(url)
        # soup = BeautifulSoup(doc.content
        # ,'html.parser')


    names = soup.find_all('a',class_='title')
    for i in names:
        name = i.text
        names_list.append(name)
    # print(names_list)

    prices = soup.find_all('h4',class_="price float-end card-title pull-right")
    for i in prices:
        price = i.text
        price_list.append(price)
    # print(price_list)

    discriptions = soup.find_all('p',class_='description card-text')
    for i in discriptions:
        discription = i.text
        disc_list.append(discription)
    # print(disc_list)

    reviews = soup.find_all('p',class_="review-count float-end")
    for i in reviews:
        review = i.text
        reviews_list.append(review)
    # print(reviews_list)

df = pd.DataFrame({'Names':names_list,"Prices":price_list,"Discription":disc_list,"Reviews":reviews_list})
df.to_csv('prac4.csv')
print(len(names_list))