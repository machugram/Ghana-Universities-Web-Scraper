
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen


def ghanaUniversities():
    url =  "https://www.4icu.org/gh/a-z/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = soup = BeautifulSoup(html, 'html.parser')
    line = list(soup.find_all('table'))
    textfile = open("schools.json", "w")
    jsonResponse = "schools: "
    jsonArray = []
    for element in line:
        rows = soup.findAll('tr')
        rows = rows[2:]
        for x in range(len(rows)):
            eachSchool = rows[x]
            names =  list(eachSchool.findAll('td'))
            schoolName = names[0].get_text()
            ranking = names[1].get_text()
        
            jsonResponse =  """{"name" :  "%(schoolName)s" , "ranking" : "%(ranking)s"}""" % {
            "schoolName": ranking, "ranking": schoolName }
            # print(jsonResponse)
            jsonArray.append('%(jsonResponse)s,\n'%{"jsonResponse" :jsonResponse})            
    jsonArray.pop(-1)
    finalResponse = "%(json)s" %{
        "json":jsonArray
    }
    finalLine = jsonArray.pop(-1)
    finalLine = finalLine[:-2:]
    textfile.write('[')
    finalJsonArray = ''.join(jsonArray)
    textfile.write(finalJsonArray)
    textfile.write(finalLine)
    textfile.write(']')
    textfile.close()

ghanaUniversities()


