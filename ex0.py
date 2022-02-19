import requests  #this is a library
 #taking text from a website using requests

payload = {'page':2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)

#print(r)

#print(r.status_code)
#print(r.ok)

#print(dir(r))

print(r.text)


# https://www.youtube.com/watch?v=tb8gHvYlCFs
