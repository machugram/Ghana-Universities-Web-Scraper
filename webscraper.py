
# from selenium import webdriver
import time
import os
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen


# def wiki_login():
#     # import selenium webdriver
#
#     # set browser / browser options
#     browser = webdriver.safari.webdriver.WebDriver(quiet=False)
#     # get page
#     browser.get('https://www.bog.gov.gh/supervision-regulation/registered-institutions/banks/')
#     # web page IDs that handle log in
#     # username = browser.find_element_by_tag('tbody')
#     # password = browser.find_element_by_id(‘wpPassword1’)
#     # login = browser.find_element_by_id(‘wpLoginAttempt’)
#     # send details to log in IDs
#     # username.send_keys(“Geektechstuff”)
#     # password.send_keys(“WIKI_PASSWORD_HERE”)
#     # login.click()
#     # time.sleep(5)
#     cheese = browser.find_element("table_87_row_0")
#
#     print(cheese)
#     print(browser.find_elements_by_id("table_87_row_0"))


# wiki_login()

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



def wikiSchoolScraping():
    url = "http://en.wikipedia.org/wiki/List_of_senior_high_schools_in_Ghana"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = soup = BeautifulSoup(html, 'html.parser')
    line = list(soup.find_all('table'))
    textfile = open("a_file.txt", "w")
    for element in line:
        textfile.write(element.get_text())
        textfile.write("/n")
    textfile.close()
    print(line[1].get_text())

    # print(line)
    # html2 = list(soup.children)[2]
    # print(list(html2.children))
# wikiSchoolScraping()