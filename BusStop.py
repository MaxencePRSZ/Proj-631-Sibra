from Horaire import Horaire
from datetime import datetime

# -*- coding: utf-8 -*-

class BusStop:
    
    def __init__(self):
        self.idLignes = []
        self.name = ""
        self.listHoraires = []
        
    def setName(self, name):
        self.name = name
        
    def addLigne(self, numLigne):
        self.idLignes.append(numLigne)
        
    def addHoraire(self, listHoraire, typeHoraire):
        horaire = Horaire(typeHoraire, listHoraire)
        self.listHoraires.append(horaire)
        
    def findTypeHoraire(self, arrivee, heure):
        print(range(len(self.listHoraires)-1))
        for i in range(len(self.listHoraires)):
            indic = self.listHoraires[i].findIndice(heure)
            datetime.strptime(self.listHoraires[i].listHoraire[indic], '%H:%M')
            print("Depart : " + str(self.listHoraires[i].listHoraire[indic]))
            print("Arrivee : " + str(arrivee.listHoraires[i].listHoraire[indic]))
            if datetime.strptime(arrivee.listHoraires[i].listHoraire[indic], '%H:%M') > datetime.strptime(self.listHoraires[i].listHoraire[indic], '%H:%M'):
                return (i, indic)
            