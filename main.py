import requests
from bs4 import BeautifulSoup as BS
import csv




def get_html(cars_url):
    response = requests.get(cars_url)
    return response.text
    

def get_soup(html):
    soup = BS(html, 'lxml')
    return soup

def get_cars(soup):
    cars = soup.find_all('div', class_="list-item list-label")
    
    
    for i in cars:
        try:
            title = i.find('div', class_='block title').text.strip()
        except AttributeError:
            title = 'None'
       
       
        try:
            price = i.find('div', class_='block price').get_text(strip=True)
        except AttributeError:
            price = '0'
        
    
        try:
            img = i.find('div', class_='thumb-item-carousel').find('img', class_='lazy-image').get('data-src')     
        except AttributeError:
            img = 'No pict'
            
    
        try:
            discription = i.find('div', class_="info-wrapper").get_text(strip=True)
        except AttributeError:
            discription= 'No result'

        print(title) 
        print(price)
        print(img)
        print(discription)

        write_csv({
        'title':title,
        'price':price,
        'img':img,
        'discription':discription
    })    

def write_csv(data):
    with open('cars.csv', 'a') as file:
        names = ['title','price','img','discription']
        write = csv.DictWriter(file, delimiter=',',fieldnames=names)
        write.writerow(data)


def main():
    for i in range(1, 100):
        cars_url = f'https://www.mashina.kg/search/all/page-{i}'
        html = get_html(cars_url)
        soup = get_soup(html)
        avto = get_cars(soup)
    
        if avto =='END':
            break
main()

  