import pandas as pd
import openpyxl
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
a = pd.read_excel("C://Users//henri//Downloads//Non conventionné.xlsx")
for i in range(len(a["Lien"])):
    a["Lien"][i] = "https://www.doctolib.fr/"+str(a["Lien"][i])
print(a["Lien"])
for j in range(len(a["Rue"])):
    a["Rue"][j] = str(a["Rue"][j]).lower()
print(a["Rue"])
for j in range(len(a["Ville"])):
    a["Ville"][j] = str(a["Ville"][j])[0]+str(a["Ville"][j])[1:].lower()
print(a["Ville"])
for j in range(len(a["Contact"])):
    if(len(str(a["Contact"][j])) < 10):
        a["Contact"][j] == "NaN"
print(a["Contact"])
#a.to_excel("C://Users//henri//Downloads//Non conventionné.xlsx")