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
        """Retrouve l'indice qui va nous permettre de savoir si le bus est en 
        aller ou en retour pour connaitre quelle horaire nous devons utiliser
    
        Parameters
        ----------
        self : self
            l'objet lui-même
        BusStop : arriver
            l'arret sur lequel on veut arriver
        datetime  : heure
            l'heure du départ
        Returns
        -------
            tuple :
                le type horaire renvoyé sous forme d'int et l'indice de listHoraire
        """ 
        for i in range(len(self.listHoraires)):
            indic = self.listHoraires[i].findIndice(heure)
            indic2 = indic
            while arrivee.listHoraires[i].listHoraire[indic2] == "-":
                indic2 += 1
            if arrivee.listHoraires[i].listHoraire[indic2] > self.listHoraires[i].listHoraire[indic]:
                return (i, indic)
            