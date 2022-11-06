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
socket.getaddrinfo('localhost', 8080)
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True,indent=4)
    print(text)
driver=webdriver.Chrome("C://Users//henri//Downloads//chromedriver_win32 (2)//chromedriver.exe")    
#driver = webdriver.Chrome("D://Users//33782//Téléchargements//Webscrappingdoctolib-main//Webscrappingdoctolib-main//chromedriver.exe")
Listedevilldecharlatan = [["osteopathe",231,270],["psychologue",199,267],["chiropracteur",18,22],["dieteticien",47,51],["psychomotricien",13,15],["pedicure-podologue",92,106],["psychanalyste",67,68],["acupuncteur",10,11]]
headers={'Refer':'https://www.doctolib.fr/','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
jobs=['osteopathe','psychologue','chiropracteur','dieteticien','psychomotricien']
a = requests.Session()
full_table=[]
start=datetime.now()
try:
    for nomville in Listedevilldecharlatan:
        for page in range(nomville[1],nomville[2]):
            start_page=datetime.now()
            driver.get("https://www.doctolib.fr/"+str(nomville[0])+"/paris?page="+str(page))
            print("\n URL ENTREE : https://www.doctolib.fr/"+str(nomville[0])+"/paris?page="+str(page)+"\n")
            soup = BeautifulSoup(driver.page_source, 'lxml')
            link = soup.find_all('a',class_="dl-link",href=True)
            tablink = []
            for i in link:
                if(len(tablink)>=1 and tablink[len(tablink)-1] != str(i['href']) and i['href'][0] == '/'):
                    tablink.append(i["href"])
                if(len(tablink) == 0 and i['href'][0] == '/'):
                    tablink.append(i['href'])
            time.sleep(random.randrange(7,11))
            if(len(tablink) == 0):
                print("ERROR ANTI BOT")
                time.sleep(30)
            for result in tablink:
                try:
                    a = requests.get("https://www.doctolib.fr"+str(result),headers=headers)
                    soup = BeautifulSoup(a.text,'lxml')
                    my_bytes = str(soup.encode('utf-8'))
                    time.sleep(1)
                    if(len(soup.find_all('div',class_="dl-profile-row-content"))<2):
                        continue

                    name=etree.HTML(str(soup)).xpath('//span[@itemprop="name"]')[0].text
                    name_list=name.split(' ')
                    last_name=name_list[-1]
                    first_name=' '.join(name_list[:-1])
                    if(len(first_name)>15 or len(last_name)>15):
                            continue
                    job=result.split('/')[1]
                    full_address = ""
                    contact='n/a'
                    if(len(soup.find_all("div",class_="dl-profile-text"))==2):
                        contact = soup.find_all('div',class_="dl-profile-row-content")[0].text.split("Téléphone")[1]
                        full_address = soup.find_all('div',class_="dl-profile-row-content")[1].text.split("Informations d'accès")[1]
                        zipcode = full_address.split(" ")[-2]
                        city = full_address.split(" ")[-1]
                        street = ""
                        for iooj in full_address.split(" ")[:-2]:
                            street += str(iooj+" ")
                    elif(len(soup.find_all("div",class_="dl-profile-text"))>2):
                        full_address=soup.find_all("div",class_="dl-profile-text")[2]
                        full_address=str(full_address).split("<")[-3].split(">")[1]
                    else:
                    #print(full_address)
                        street=' '.join(full_address.split(',')[:-1])
                        rest=full_address.split(',')[-1].split(' ')
                        if(rest[0]=='' and len(rest)>1):
                            zipcode=rest[1]
                            city=' '.join(rest[2:])
                        else:
                            zipcode=rest[0]
                            city=' '.join(rest[1:])
                    
                    
                    
                    adeli_number='n/a' 
                    rpps_number ='n/a'
                    
                    full_table.append([last_name,first_name,job,street,zipcode,city,contact,result])
                    #input()
                    print("Last Name : "+str(last_name))
                    print("First Name : "+str(first_name))
                    print("Job : "+str(job))
                    print("Street : "+str(street))
                    print("ZIP : "+str(zipcode))
                    print("Contact : "+str(contact))
                    time.sleep(random.randrange(7,11))
                except:
                    print('error, skipping',result)
                    traceback.print_exc()
                    time.sleep(random.randrange(7,11))      
except Exception:
    full_df= pd.DataFrame(full_table,columns=['Nom','Prenoms','Profession','Rue','Code Postal','Ville','Contact','Lien'])
    full_df.to_csv("nonconventionnéparis.csv",quoting=csv.QUOTE_ALL,quotechar='"')
    print('something went wrong')
    traceback.print_exc()

driver.quit()
full_df= pd.DataFrame(full_table,columns=['Nom','Prenoms','Profession','Rue','Code Postal','Ville','Contact','Lien'])
full_df.head()

def numero_formatting(numero):
    if(len(numero)>0 and numero[0]=='0'):
        numero='+33 '+numero[1:]
    return numero

def text_formatting(text):
    if (text is None):
        return text
    text=text.replace('é','e')
    text=text.replace('è','e')
    text=text.replace('ê','e')
    text=text.replace('î','i')
    text=text.replace('à','a')
    text=text.replace('â','a')
    text=text.replace("'",'_')
    text=text.replace("ô",'o')
    text=text.replace("ç",'c')
    text=text.replace("É",'E')
    text=text.replace("È",'E')
    text=text.replace("À",'A')
    text=text.replace("Ù",'U')
    text=text.replace("Ç",'C')

    return text

def education_formatting(list):
    for index in range(len(list)):
        list[index]=(text_formatting(list[index][0]),list[index][1])

    return list

def to_upper(word):
    if (word is None):
        return word
    return word.upper()


full_df['Contact d_urgence']=full_df['Contact d_urgence'].apply(numero_formatting)
full_df['Nom']=full_df['Nom'].apply(text_formatting)
full_df['Nom']=full_df['Nom'].apply(to_upper)
full_df['Prenoms']=full_df['Prenoms'].apply(text_formatting)
full_df['Rue']=full_df['Rue'].apply(text_formatting)
full_df['Ville']=full_df['Ville'].apply(text_formatting)
full_df['Moyens de paiement']=full_df['Moyens de paiement'].apply(text_formatting)
full_df['Formations et experiences']=full_df['Formations et experiences'].apply(education_formatting)
#full_df['Formations et experiences']=full_df['Formations et experiences'].apply(text_formatting)




full_df['Visites a domicile']=full_df['Visites a domicile'].apply(numero_formatting)


full_df.head()
full_df.to_csv("nonparis.csv",quoting=csv.QUOTE_ALL)
full_df.to_excel("nonparis.xlsx" )

#,quoting=csv.QUOTE_ALL