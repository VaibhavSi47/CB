import requests
from bs4 import BeautifulSoup

# url = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/coronavirus-disease-covid-19-adolescents-and-youth"

def adol_youth(url):
    r = requests.get(url)
#    print(page)

    soup = BeautifulSoup(r.content, 'html5lib')
#    print(soup)
    pew = soup.findAll('div',
                    attrs={'class': 'sf-accordion__content'})
    print(pew)
#    for soup1 in pew.find('div',
#                             attrs={'class': 'sf-accordion__summary'}):
    soup1 = pew.findAll('div',
                    attrs={'class': 'sf-accordion__summary'})
#        for ad in soup1:
#            print(" ", ad.get_text())

    return soup1.get_text()




