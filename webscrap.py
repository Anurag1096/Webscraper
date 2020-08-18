from bs4 import BeautifulSoup
import requests

# webname = input("ENter the website url")
source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())
# sta = input("Enter a tag")

article = soup.find('article')
# print(article.prettify())

summary = article.find('div', class_='entry-content').p.text
print(summary)



 headline = article.h2.a.text
# print(headline)
'''
with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
for article in  soup.find_all('div', class_='article'):
    #print(article)

    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
'''
