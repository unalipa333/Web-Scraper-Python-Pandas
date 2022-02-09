from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup




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
        item1 = item.find('span').text
        print(item1)
    # return

c = extract()
d = transform(c)    # test that it runs
print(d)
