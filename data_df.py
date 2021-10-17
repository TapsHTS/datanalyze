class bcolors: #Pour avoir des couleurs dans la console
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

import os
from os import system
import pandas as pd #On importe pandas (pip install pandas).

data_df = pd.read_csv("./revenues/revenues.csv", sep=',') #On lit le fichier revenues.csv contenu dans le dossier ./revenues et on lui indique que les séparations sont des ";".

data_want = data_df[[
        "ad_share_gross", 
        "sub_share_gross", 
        "bits_share_gross", 
        "bits_developer_share_gross", 
        "bits_extension_share_gross", 
        "prime_sub_share_gross", 
        "bit_share_ad_gross",
        "fuel_rev_gross", 
        "bb_rev_gross"
        ]]

data_want["total_money"] = data_want.sum(axis=1) #Retourne la somme des valeurs de l'axe des salaires.
system('cls')#Efface la console

result = pd.DataFrame(columns=['ID', 'Total']) #Créer une nouvelle DataFrame avec comme colonnes 'ID' et 'Argent Total'

print(bcolors.OKCYAN + "Generation..." + bcolors.ENDC)

for x in data_df.index: #Cette fonction permet d'ajouter une ligne contenant le ID et l'Argent Total en fonction du nombre de ligne
    result.loc[x] = [data_df["user_id"][x], round(data_want["total_money"], 2)[x]]

result.to_csv("./revenues/result.csv", sep=';', index=False) #Cela créer le nouveau fichier avec les valeurs au dessus
print(bcolors.OKGREEN + "Données structurées dans " + bcolors.OKBLUE + bcolors.BOLD + os.path.join("./revenues/result.csv") +  bcolors.ENDC)
