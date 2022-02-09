import webbrowser
import time


country = "Spain is great"

myhtml_content = f'<html> <head> </head> <h1>{country}</h1> <body> <body> </html>'

with open('index.html', 'w+') as myhtml_file:   #with open is good to know
    myhtml_file.write(myhtml_content)  # passing variable myhtml_content and writing it to the new html file
    print("HTML created successfully!!!") # confirmation print


#time.sleep(2) # waiting two second doesn't run
#webbrowser.open("index.html")   #doesn't run
