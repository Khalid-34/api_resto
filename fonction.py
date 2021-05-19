import csv
import logging
from unittest import result
import pandas
from datetime import datetime

def ouvrire_fichier():
    """fonction qui permet de ouvrire le fichier csv """
    # # fonction qui permet de ouvrire et de lire un fichier csv
    # f = open('rest_hours.csv')
    # f = csv.reader(f)
    # # for row in f:
    # #     print(row)
    # return f
    df = pandas.read_csv('rest_hours.csv',names=['resto','horaire'])
    logging.info("ouverture du fichier csv en pandas")
    return df

def resto_ouvert(date):
    """fonction qui permet de prendre en paramètre une horaire au format "Mon Dec 7 14:59:26 2010" et
     indique les restaurants disponibles à ce moment là """
    df = ouvrire_fichier()
    df = df.loc[df["resto"].isin([date].sort_values(["horaire"])
    resultat = {}
    resultat["resto"] = str(df.iloc[0][1])
    resultat["horaire"] = str(df.iloc[0][2])
    print(resultat)
    # return resultat


resto_ouvert('Mon Dec 7 14:59:26 2010')
# print(ouvrire_fichier())

# def nom_resto():
#     """fonction qui permet de selectionner les nom des restos """
#     df = ouvrire_fichier()
#     choix_resto = set(df['resto'].tolist())
#     return choix_resto
 

# def nom_horaire():
#     """fonction qui permet de selectionner les horaire"""
#     df = ouvrire_fichier()

#     choix_horaire = set(df['horaire'].tolist())
#     return choix_horaire
   



# print(nom_horaire())

