from Horaire import Horaire
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