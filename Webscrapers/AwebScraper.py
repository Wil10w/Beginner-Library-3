#this is a webscraper that pulls a simple dataset of countries and their
# general information (name, popSize, Area(km2), Capitol, etc), cleans it up
# and puts it into a SQL database using Beautiful soup and pyodbc.

from bs4 import BeautifulSoup
import requests
import io

#here we get the website in txt format
html_text = requests.get('https://scrapethissite.com/pages/simple/').text
#we then create a var that uses lxml parser with our 'website' var above
soup = BeautifulSoup(html_text, 'lxml')
#another var to collect all info under div class 'col-md-4 country' - this is where all the contry info is found on the website
countries = soup.find_all('div', class_ = "col-md-4 country")
# a dictionary to separate and hold the data(not necessarily the best way, but the way I did it. maybe a possible revamp later in time.
outputDict = {}
#loop through all the rows of countries that have been pulled from the website as we used .find_all so the script has pulled all the data, not just one line.
for country in countries:
    #we create a var that finds the country name within the html and pulls only the text. we also start the formatting process with .replace
    name = country.find('h3', class_ = 'country-name').text.replace('        ', ' ')
    #more formatting to remove double-spaces
    name = name.replace('   ', ' ')
    name = name.replace('  ', ' ')
    #this removes more whitedpace on the end of the sentences
    name = name.lstrip()
    #gets rid of the blank line
    name = name.replace('\n', '')
    #now we create a variable for the country info with formatting
    info = country.find('div', class_ = 'country-info').text.replace('\n', ' ')
    #we remove the headings from each piece of data, but leave the ':' for .split reasons - as default split will separate city names that have two words - Bandar Seri Begawan, = Bandar, Seri, Begawan,
    info = info.replace('Population', '')
    info = info.replace('Area (km2)', '')
    info = info.replace('Capital','')
    # we remove extra whitespace before .split
    info = info.replace(' : ', ':')
    info = info.rstrip()
    info = info.split(':')
    #the split has added '' to list[0] so we add only list[1:len] and skip the unwanted index.
    outputDict[name] = info[1:]
    #Dictionary is complete and ready to be added to SQL DB

import pyodbc
#we open SQLdb with .connect below
myDB = pyodbc.connect('Driver={SQL Server};' 
                      'Server=DESKTOP-K2DFS1E;' 
                      'Database=TestDB;' 
                      'Trusted_COnnection=yes')
#activate cursor
cursor = myDB.cursor()
#Make a variable with our SQL query that adds the data to the db
insert_query = ''' INSERT INTO Countries (Country, Capitol, Population, Area) VALUES (?, ?, ?, ?);'''

#we loop over the dictionary and unpack i into key and values(data)
for i in outputDict.items():
    key, data = i
    #we then sort everything into a var called values for the SQL query
    values = (key, data[0], data[1], data[2])
    #we execute the query with the query variable and the var(values)
    cursor.execute(insert_query, values)
#commit it to SQL Database
myDB.commit()
#close connection and remove cursor
cursor.close()
myDB.close()

cursor.execute('SELECT * FROM Countries')

for row in cursor:
    print(row)













