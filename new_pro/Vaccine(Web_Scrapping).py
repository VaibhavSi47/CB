'''import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


htmldata = getdata("https://covid-19tracker.milkeninstitute.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
result = (soup.find('div', attrs={'class': 'w-dyn-items'}))
print(result)
# table = (soup.find_all("div", class_="is_h5-2 is_developer w-richtext"))

names = []

for row in result.findAll('div', attrs={'class': 'chart_row-container'}):
    for row1 in result.findAll('div', attrs={'class': 'is_h5-2 is_developer w-richtext'}):
        name = {}
        name['name'] = row1.div.text
        names.append(name)

"""(names)"""

#print("NO 1 " + result[48:125])
#print("NO 2 " + result[178:218])
#print("NO 3 " + result[271:358])
#print("NO 4 " + result[411:436])
#print("NO 5 " + result[490:505])
#print(result) '''

import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


htmldata = getdata("https://covid-19tracker.milkeninstitute.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
result = (soup.find_all("div", class_="is_h5-2 is_developer w-richtext"))
print(result)
names=[]
for row in result:
    name = {'name': row.div.text}
    names.append(name)
print(names)
print("NO 1 " + result[46:86])
print("NO 2 " + result[139:226])
print("NO 3 " + result[279:305])
print("NO 4 " + result[358:375])
print("NO 5 " + result[428:509])
