#beautifulsoap is library to pass or fetch data. here we import beautifulsoup and request
from bs4 import BeautifulSoup
import requests
#fetching data from websites
response = requests.get('https://en.wikipedia.org/wiki/List_of_Hindi_films_of_1980')
#checking status of the response of website link
response.status_code
print(response.text[:1000])
type(response.text)#what type of data is this
html = response.text
data = BeautifulSoup(html,'html.parser')
print(data.prettify())#makes data in easy readable format
data.title
print(data.title.string)

import re
heading_before_table = data.find_all('h2')
heading_before_table

table_data = data.find_all('table', class_='wikitable')
len(table_data)#length of table data
table_data

table_data = data.find('table',class_='wikitable')
rows = table_data.find_all('tr')
rows

movies = []
for row in rows:
    curr_movie = []#store movies list individualy
    for cell in row.find_all("td"):
        if cell.string != "\n" and cell.string != None:#checking string conditions
            curr_movie.append(cell.string)
        else:
            curr_movie.append("NA")
    movies.append(curr_movie)
    #print(curr_movie)
print(movies)

import pandas as pd
#pandas are fast and flexible tool used for data analysis and manipulations

df = pd.DataFrame()

for row in movies:
    if len(row) != 0:
        df = df._append({'Movie Name' : row[0],
                       'Director' : row[1],
                       'Cast' : row[2],
                       'Genre': row[3]},ignore_index= True)

print(df)
df.head()#gives first five values of dataframe
df.tail()#gives last five values of dataframe
