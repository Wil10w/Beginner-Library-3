from bs4 import BeautifulSoup
import requests
import io


def concat(alist):
    return description[1]+' '+description[2]+' '+description[3]+' '+description[4]+' '+description[5]





html_text = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops').text

soup = BeautifulSoup(html_text, 'lxml')

shopping = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')

outputDict = ()
inputfile = open('ecommerceScape.txt', 'a')
for items in shopping:
    price = items.find('h4', class_ = "pull-right price").text
    description = items.find('p', class_ = 'description').text.split(',')
    description = concat(description)
    name = items.find('p', class_ = 'description').text.split(',')
    name = name[0]
    reviews = items.find('p', class_ = "pull-right").text
    outputDict = name+'  '+price+'  '+reviews+'  '+description
    print(outputDict)
    print(outputDict, file=inputfile)





