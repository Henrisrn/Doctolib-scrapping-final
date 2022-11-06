from ast import While
from numpy import append
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import time
import traceback
import requests
from datetime import datetime
from io import StringIO
import csv
import json
import random
from selenium.webdriver.firefox.options import Options
import socket
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
def get_status(logs):
    for log in logs:
        if log['message']:
            d = json.loads(log['message'])
            try:
                content_type = 'text/html' in d['message']['params']['response']['headers']['content-type']
                response_received = d['message']['method'] == 'Network.responseReceived'
                if content_type and response_received:
                    return d['message']['params']['response']['status']
            except:
                pass
Listedevillefrancaise = [["osteopathe","toulouse",44],["osteopathe","nice",28],["osteopathe","nantes",33],["osteopathe","montpellier",27],["osteopathe","strasbourg",19],
["psychologue","Lille",1],["psychologue","bordeaux",35],["psychologue","rennes",18],
["chiropracteur","Lille",1],["chiropracteur","bordeaux",3],["chiropracteur","rennes",2],
["dieteticien","Lille",1],["dieteticien","bordeaux",9],["dieteticien","rennes",4],
["psychomotricien","Lille",1],["psychomotricien","bordeaux",3],["psychomotricien","rennes",2],
["pedicure-podologue","Lille",1],["pedicure-podologue","bordeaux",16],["pedicure-podologue","rennes",9],
["sophrologue","Lille",1],["sophrologue","bordeaux",5],["sophrologue","rennes",4],
["hypnotherapeute","Lille",1],["hypnotherapeute","bordeaux",11],["hypnotherapeute","rennes",6],
["psychanalyste","Lille",1],["psychanalyste","bordeaux",5],["psychanalyste","rennes",2],
["naturopathe","Lille",1],["naturopathe","bordeaux",5],["naturopathe","rennes",2],
["acupuncteur","Lille",1],["acupuncteur","bordeaux",3],["acupuncteur","rennes",2]]

driver = webdriver.Chrome("C://Users//henri//Downloads//chromedriver_win32 (2)//chromedriver.exe", desired_capabilities=capabilities) 
pagemax = []
for i in Listedevillefrancaise: 
    compteur = 1
    bb = get_status(driver.get_log('performance'))
    while bb != 404 :  
        driver.get("https://www.doctolib.fr/"+str(i[0])+"/"+str(i[1])+"?page="+str(compteur))
        compteur+=1
        bb = get_status(driver.get_log('performance'))
        time.sleep(3)
    pagemax.append(str(i[0]))
    pagemax.append(str(i[1]))
    pagemax.append(str(compteur))
    print("\n Proffession : "+str(i[0])+" lieu : "+str(i[1])+" page max : "+str(compteur))
    print(pagemax)
    time.sleep(6)
print(pagemax)


    