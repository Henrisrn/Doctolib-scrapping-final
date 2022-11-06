import pandas as pd
import openpyxl
a = pd.read_excel("C://Users//henri//Webscrapping 2//Scrappingville//Ceciestlebonneexcel.xlsx")

contact = []
for i in a["Contact fixee"]:
    if(str(i)[0] == "0"):
        print("Avant : "+i)
        list_of_chars = list(str(i))
        list_of_chars[0] = '+33 '
        new_str = ''.join(list_of_chars)
        i = new_str
        contact.append(i)
        print("Après : "+i)
    if(str(i)[0] != "0"):
        contact.append(i)
#a.insert(10,"Contact fixee",pd.Series(contact))

contact = []
for i in a["Contact d'urgence mobilee"]:
    if(str(i)[0] == "0"):
        print("Avant : "+i)
        list_of_chars = list(str(i))
        list_of_chars[0] = '+33 '
        new_str = ''.join(list_of_chars)
        i = new_str
        contact.append(i)
        print("Après : "+i)
    if(str(i)[0] != "0"):
        contact.append(i)
#a.insert(10,"Contact d'urgence mobilee",pd.Series(contact))

contact = []
for i in a["Contact d'urgence fixee"]:
    if(str(i)[0] == "0"):
        print("Avant : "+i)
        list_of_chars = list(str(i))
        list_of_chars[0] = '+33 '
        new_str = ''.join(list_of_chars)
        i = new_str
        contact.append(i)
        print("Après : "+i)
    if(str(i)[0] != "0"):
        contact.append(i)
#a.insert(10,"Contact d'urgence fixee",pd.Series(contact))

contact = []
for i in a["Numero visites a domicile mobilee"]:
    if(str(i)[0] == "0"):
        print("Avant : "+i)
        list_of_chars = list(str(i))
        list_of_chars[0] = '+33 '
        new_str = ''.join(list_of_chars)
        i = new_str
        contact.append(i)
        print("Après : "+i)
    if(str(i)[0] != "0"):
        contact.append(i)
#a.insert(10,"Numero visites a domicile mobilee",pd.Series(contact))

contact = []
for i in a["Numero visites a domicile fixee"]:
    if(str(i)[0] == "0"):
        print("Avant : "+i)
        list_of_chars = list(str(i))
        list_of_chars[0] = '+33 '
        new_str = ''.join(list_of_chars)
        i = new_str
        contact.append(i)
        print("Après : "+i)
    if(str(i)[0] != "0"):
        contact.append(i)
#a.insert(10,"Numero visites a domicile fixee",pd.Series(contact))
#for i in range(len(a["Contact d'urgence mobile"])):
#    if(a["Contact d'urgence mobile"][i] == a["Contact d'urgence fixe"][i] and a["Contact d'urgence fixe"][i] != ""):
#        a["Contact d'urgence fixe"][i] = ""
#        #print(a["Contact d'urgence mobile"][i])
#a.to_excel("Scrappingville//Ceciestlebonneexcel.xlsx")

