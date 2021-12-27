# https://www.youtube.com/watch?v=ng2o98k983k&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=46&t=1s&ab_channel=CoreySchafer

from bs4 import BeautifulSoup
import requests

condition = False

if condition:

    with open('simple.html') as html_file:
        soup = BeautifulSoup(html_file, 'lxml')

    # returns <title> tag
    match = soup.title.text

    # retruns the first <div> it finds along with children
    match = soup.div

    # returns the first <div> it finds along with children
    match = soup.find('div')

    # returns <div> with 'footer' class. We use "class_" because "class" is a reserved word in python
    match = soup.find('div', class_='footer')
    print(match)

    # get the article of simple.html
    article = soup.find('div', class_='article')
    print(article.h2.a.text)
    summary = article.p.text
    print(summary)

    # now lets get all releveant items using find_all()
    for article in soup.find_all('div', class_='article'):
        print(article.h2.a.text)


source = requests.get('https://coreyms.com', verify=False).text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())