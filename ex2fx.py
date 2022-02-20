
import requests
from bs4 import BeautifulSoup
import pandas as pd 


def extract():
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}

    url = 'https://quotes.toscrape.com/'

    r = requests.get(url, headers)

    soup = BeautifulSoup(r.content, 'html.parser')

    return soup

    #return print(r.status_code)          # testing to see if code runs

#extract()                # testing to see if code runs 200 code is good


def transform(soup):
    quotes = soup.find_all('div', class_ = 'quote')
    

    #return len(quotes)  # returns quantity of objects


    for item in quotes:            
       quote = item.find('span').text
       author = item.find('small', class_= 'author').text
       tags = item.find('div', class_='tags').text.strip().replace('\n','')
       #print(quote,author,tags)
       dict_quotes = {
           'quote': quote,
           'author': author,
           'tags': tags

       }
       list_quotes.append(dict_quotes)

    return   

list_quotes = [] 

c = extract()
transform(c)    # test that it runs

df = pd.DataFrame(list_quotes)

print(df)

df.to_html('quotes.html')
