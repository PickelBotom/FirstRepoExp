#! usr/bin/python3
from bs4 import BeautifulSoup
import requests

def scrape():
    for i in range(2,6):
        Pg2Scrape = requests.get(f"https://books.toscrape.com/catalogue/category/books_1/page-{i}.html") 
        soup = BeautifulSoup(Pg2Scrape.text,"html.parser")
        ol = soup.find("ol")
        articles= ol.find_all("article",attrs={"class":"product_pod"})
        for art in articles:
            img = art.find('img')
            name= img.attrs['alt']
            price= art.find("p",attrs={"class":"price_color"}).text
            rprice = float (price[2:])*19.93
            output = "{} \tR{:.2f}".format(name,rprice) 
            print(output)

if __name__ == '__main__':
    scrape()