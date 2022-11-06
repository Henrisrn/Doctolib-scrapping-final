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
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True,indent=4)
    print(text)
#driver=webdriver.Chrome("C://Users//henri//Downloads//chromedriver_win32 (2)//chromedriver.exe")    
driver = webdriver.Chrome("D://Users//33782//Téléchargements//Webscrappingdoctolib-main//Webscrappingdoctolib-main//chromedriver.exe")
a = requests.Session()
full_table=[]
start=datetime.now()
#Mettre 905
rpps = []

#METTRE LE CHEMIN D'ACCES DE L'EXCEL
df = pd.read_excel("Scrappingville//Scrappingdetoutdoctolib.xlsx")

time.sleep(1)
compteur = 0
pointdedepart = 50
maxvaleur = 1000
for j in range(pointdedepart):
    rpps.append("PAS PRIS EN COMPTE DANS CE PROGRAME")
try:
    for i in df["Lien"][pointdedepart:]:
        if(compteur == maxvaleur):
            break
        else:
            print(i)
            driver.get(i)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            adeli_number='n/a' 
            rpps_number ='n/a'
            try: 
                adeli=soup.find_all('div',class_="dl-profile-row-section")[-1].text
                rppss = soup.find_all('div',class_="dl-profile-row-section")[-2].text
                if('RPPS' in rpps):
                    rpps_number=rppss.split('S')[1]
                    print("Numéro rpps = "+rpps_number)
                    print("Numéro rpps = "+rpps_number)
                if('RPPS' in adeli):
                    rpps_number=adeli.split('S')[1]
                    print("Numéro rpps = "+rpps_number)
                    print("Numéro rpps = "+rpps_number)
            except:
                print(str(i)+" Has no RPPS or ADELI")
            rpps.append(rpps_number)
            time.sleep(4)
            compteur+=1
except:
    print("ERROR")


df.insert(10,'RPPS'+str(pointdedepart),pd.Series(rpps))
df.to_excel("Scrappingville//Scrappingdetoutdoctolibbbb.xlsx")