import requests as r
import re
from bs4 import BeautifulSoup

letterDict = {}

for i in range(0, 500):
    request = r.get("https://www.samgongustofa.is/siglingar/skrar-og-utgafa/skipaskra/uppfletting?sq=" + str(i))

    soup = BeautifulSoup(request.content, "html.parser")

    items = soup.findAll(text="Umdæmisstafir:")

    if len(items) > 0:
        item = items[0].parent.parent
        m = re.search(' (.+)-', item.find("span").text)
        m2 = re.search('\((.+)\)', item.find("span").text)
        if m and m2:
            letters = m.group(1).strip()
            area = m2.group(1).strip()
            letterDict[letters] = area


with open('letterAndAre.csv','w') as file:
    for key, value in letterDict.items():
        stringToWrite = str(key) + ', ' + str(value)
        file.write(stringToWrite)
        file.write('\n')
