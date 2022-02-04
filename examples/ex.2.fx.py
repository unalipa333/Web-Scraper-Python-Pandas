import requests
from bs4 import BeautifulSoup




def extract(page):
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}

    url = f'https://www.indeed.com/jobs?q=python%20developer&l=Orange%20County,%20CA&start={page}&vjk=7f05dae8482c5b6d'

    r = requests.get(url, headers)

    soup = BeautifulSoup(r.content, 'html.parser')

    return soup

  #  return r.status_code          # testing to see if code runs

#print(extract(20))                # testing to see if code runs 200 code is good

c = extract(20)
