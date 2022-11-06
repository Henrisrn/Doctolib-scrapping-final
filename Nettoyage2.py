import pandas as pd
import time

full_df=pd.read_excel("Aclasser.xlsx")
full_df.head()
cb = []
colonne = ["Nom","Prenoms","Profession","NoADELI","Rue","Code Postal","Ville","Carte Bancairee","Carte Bancaire","Formation 1","Date 1","Formation 2","Date 2","Formation 3","Date3","Formation 4","Date 4","Formation 5","Date 5","Formation 6","Date 6","Formation 7","Date 7","Formation 8","Date 8","Formation 9","Date 9","Formation 10","Date 10","Formation 11","Date 11","Formation 12","Date 12","Formation 13","Date 13","Formation 14","Date 14","Contact mobile","Contact fixe","Contact d'urgence mobile","Contact d'urgence fixe","Numero visites a domicile mobile","Numero visites a domicile fixe","Lien"]

nomparlien = []
prenomparlien = []
prenom = []
lien = []
nom = []
Contactmobile = []
Contactfixe = []
Contactdurgencemobile = []
Contactdurgencefixe = []
Numerovisitesadomicilemobile = []
info = []
Numerovisitesadomicilefixe = []
total = []
for i in range(1205):
    inf = []
    try:
        lien.append(full_df["Lien"][i])
        b = full_df["Lien"][i].split('/')[6]
        if("?" in str(b)):
            text = str(b).split('?')[0]
            prenomparlien.append(str(text).split('-')[0])
            nomparlien.append(str(text).split('-')[1])
            tea = str(text).split('-')[0]
            bb = full_df[full_df['Nom']== str(tea).upper()]
            compteur = 0
            
            if(bb.empty == False and len(bb) >1):
                    print("TROOUUVVEEE")
                    for i in bb:
                        if(compteur == 37):
                            break
                        compteur+=1
                        inf.append(bb[i])
                        print(i)
                        print(b[i])
                        time.sleep(2)
            inf.append(full_df["Contact mobile"][i])
            inf.append(full_df["Contact fixe"][i])
            inf.append(full_df["Contact d'urgence mobile"][i])
            inf.append(full_df["Contact d'urgence fixe"][i])
            inf.append(full_df["Numero visites a domicile mobile"][i])
            inf.append(full_df["Numero visites a domicile fixe"][i])

            #print(str(text).split('-')[0])
            #print(str(text).split('-')[1])
            
                
        else:
            prenomparlien.append(str(b).split('-')[1])
            nomparlien.append(str(b).split('-')[0])
            tea = str(b).split('-')[0]
            bb = full_df[full_df['Nom']== str(tea).upper()]
            compteur = 0
            
            if(bb.empty == False and len(bb) >1):
                    print("TROOUUVVEEE")
                    for i in bb:
                        if(compteur == 37):
                            break
                        compteur+=1
                        print(b[i])
                        time.sleep(2)
                        inf.append(bb[i])
            inf.append(full_df["Contact mobile"][i])
            inf.append(full_df["Contact fixe"][i])
            inf.append(full_df["Contact d'urgence mobile"][i])
            inf.append(full_df["Contact d'urgence fixe"][i])
            inf.append(full_df["Numero visites a domicile mobile"][i])
            inf.append(full_df["Numero visites a domicile fixe"][i])
            
            #print(str(b).split('-')[0])
            #print(str(b).split('-')[1])
        
        info.append(inf)
    except:
        continue
        
        
            
    
    #print(i)
    #print(Contactmobile)
    #print(lien)
#print(info)
#aaa = pd.DataFrame(data=info)
#aaa.to_excel("Sortieclasseronverra.xlsx")
for i in range(len(prenomparlien)):
    bb = full_df[full_df['Nom']== str(prenomparlien[i]).upper()]
    compteur = 0
    inf = []
    if(bb.empty == False and len(bb) >1):
            for i in bb:
                if(compteur == 37):
                    break
                compteur+=1
                inf.append(bb[i])
    info.append(inf)


#full_df.to_excel("Scrappingville//Sortietest333334.xlsx")
