#import pandas as pd
#import openpyxl
#def is_number(s):
#    try:
#        float(s)
#        return True
#    except ValueError:
#        pass
# 
#    try:
#        import unicodedata
#        unicodedata.numeric(s)
#        return True
#    except (TypeError, ValueError):
 #       pass
# 
#    return False
#a = pd.read_excel("Scrappingville\ExcelbrutHenri.xlsx")

#
#for j in range(len(a["Ville"])):
#    a["Ville"][j] = str(a["Ville"][j])[0]+str(a["Ville"][j])[1:].lower()
#for j in range(len(a["Contact"])):
#    if(len(str(a["Contact"][j])) < 10):
#        a["Contact"][j] == "NaN"

#a.to_excel("Sortienettoyage.xlsx")

# %%
import pandas as pd
import csv
import numpy as np

# %%
full_df=pd.read_excel("C://Users//henri//Downloads//petitevilledefrance22.xlsx")
full_df.head()
for i in range(len(full_df["Lien"])):
    full_df["Lien"][i] = "https://www.doctolib.fr/"+str(full_df["Lien"][i])
for j in range(len(full_df["Rue"])):
    full_df["Rue"][j] = str(full_df["Rue"][j]).lower()

# %%
def numero_formatting(numero):
    if(len(numero)>0 and numero[0]=='0'):
        numero='+33 '+numero[1:]
    #print('numero formatté : '+numero)
    return numero

# %%
def contact_formatting(contact):
    contact=str(contact)
    print('avant : ',contact, len(contact))
    if(len(contact)>17):
        #print('avant :',print(contact))
        contact=contact[18:32]
    contact=numero_formatting(contact)
    print('apres :',contact)

    return contact

# %%
def adeli_formatting(adeli):
    if(type(adeli)==float and not np.isnan(adeli)):
        #print(adeli)
        adeli=int(adeli)
    return adeli

# %%
full_df['Contact']=full_df['Contact'].apply(contact_formatting)
full_df.head()


# %%
full_df['No ADELI']=full_df['No ADELI'].apply(adeli_formatting)


# %%

# %%
def change_paying_format(payment):
    if('carte bancaire' in payment):
        payment='OUI'
    else:
        payment='NON'
    return payment

# %%
#full_df['Moyens de paiement']=full_df['Moyens de paiement'].apply(change_paying_format)
full_df.rename(columns={'Visites a domicile': 'Numero visites a domicile'}, inplace=True)
full_df.insert(11,'Visites a domicile',pd.Series(['NON' if num=='n/a' else 'OUI' for index,num in full_df['Numero visites a domicile'].items()]))

# %%
max_len=0
max_index=-1
#for index, item in full_df['Formations et experiences'].iteritems():
#    if(len(item)>max_len):
#        max_len=len(item)
#        max_index=index

#print(max_len)
#print(full_df['Lien'][max_index])

# %%
formations=[]
for i in range(10):
    formations.append([])
print(len(formations))

for index, item in full_df['Formations et experiences'].iteritems():
    for i in range(10):
        if( i>=len(str(item).split(')'))):
            formations[i].append('')
        else:
            formations[i].append(str(item).split(')')[i])

for i in range(10):
    full_df.insert(9+i,'Formations '+str(i),pd.Series(formations[i]))
del full_df['Formations et experiences']

# %%
#contact
full_df.to_excel("Scrappingville\Sortieintermédiaire.xlsx")
contact_fixe=[]
contact_mobile=[]
for index, item in full_df['Contact'].iteritems():
    if(item=='n/a'):
        #print('na case')
        contact_fixe.append('')
        contact_mobile.append('')

    else:
        if(len(str(item))<5 or str(item[4])=='1' or str(item[4])=='2' or str(item[4])=='3' or str(item[4])=='4' or str(item[4])=='5'):
            contact_fixe.append(item)
            contact_mobile.append('')
        else:
            contact_mobile.append(item)
            contact_fixe.append('')
full_df.insert(10,'Contact mobile',pd.Series(contact_mobile))
full_df.insert(11,'Contact fixe',pd.Series(contact_fixe))
del full_df['Contact']

#contact d'urgence
contact_emer_fixe=[]
contact_emer_mobile=[]
for index, item in full_df['Contact d_urgence'].iteritems():
    item = str(item)
    if(item=='n/a'):
        contact_emer_fixe.append('')
        contact_emer_mobile.append('')

    else:
        if(len(str(item))<5 or str(item)[4]=='1' or str(item)[4]=='2' or str(item)[4]=='3' or str(item)[4]=='4' or str(item)[4]=='5'):
            contact_emer_fixe.append(item)
            contact_emer_mobile.append('')
        else:
            contact_emer_mobile.append(item)
            contact_emer_fixe.append('')
full_df.insert(11,'Contact d_urgence mobile',pd.Series(contact_emer_mobile))
full_df.insert(12,'Contact d_urgence fixe',pd.Series(contact_emer_fixe))
del full_df['Contact d_urgence']

#contact d'urgence
dom_fixe=[]
dom_mobile=[]
for index, item in full_df['Numero visites a domicile'].iteritems():
    if(item=='n/a'):
        dom_fixe.append('n/a')
        dom_mobile.append('n/a')

    else:
        if(len(str(item))<5 or str(item)[4]=='1' or str(item)[4]=='2' or str(item)[4]=='3' or str(item)[4]=='4' or str(item)[4]=='5'):
            dom_fixe.append(item)
            dom_mobile.append('n/a')
        else:
            dom_mobile.append(item)
            dom_fixe.append('n/a')
full_df.insert(14,'Numero visites a domicile mobile',pd.Series(dom_mobile))
full_df.insert(15,'Numero visites a domicile fixe',pd.Series(dom_fixe))
del full_df['Numero visites a domicile']
     

# %%
full_df.head()

# %%
full_df.to_csv("Scrappingville/all_jobs_2_cleaned_changed.csv",quoting=csv.QUOTE_ALL )