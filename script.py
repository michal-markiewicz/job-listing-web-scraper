import requests
from bs4 import BeautifulSoup

URL = "https://www.pracuj.pl/praca/programista;kw/praca%20zdalna;wm,home-office?et=17"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# offer = soup.find(attrs={"data-test": "default-offer"})
# offerPretty = offer.prettify()
# companyName = offer.find(attrs={"data-test": "text-company-name"}).text
# title = offer.find(attrs={"data-test": "offer-title"}).text

everyOffer = soup.findAll(attrs={"data-test": "default-offer"})
companyNames = []
titles = []
for offer in everyOffer:
    companyName = offer.find(attrs={"data-test": "text-company-name"}).text
    title = offer.find(attrs={"data-test": "offer-title"}).text
    companyNames.append(companyName)
    titles.append(title)

print(companyNames)
print(titles)


# print(sectionOffers)
# print(companyName)
# print(title)