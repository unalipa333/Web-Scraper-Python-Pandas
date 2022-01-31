from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get('https://quotes.toscrape.com')

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

quotes = soup.findAll('span', attrs={'class':'text'})

authors = soup.findAll('small', attrs={'class':'author'})

#for quote in quotes:
#    print(quote.text)

#for author in authors:
#    print(author.text)



file = open('scraped_quotes.csv', 'w')
writer = csv.writer(file)

writer.writerow(['QUOTES', 'AUTHORS'])

for quote, author in zip(quotes, authors):
    print(quote.text + ' - ' + author.text)
    writer.writerow([quote.text, author.text]) 
file.close()

# https://www.youtube.com/watch?v=QhD015WUMxE
