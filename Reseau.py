from BusStop import BusStop
from Trajet import Trajet
# -*- coding: utf-8 -*-

class Reseau:
    
    def __init__(self):
        self.listBusStop = []
        self.listTrajet = []
        self.countLigne = 0
            
    def getCountLigne(self):
        return self.countLigne
    
    def incrementCountLigne(self):
        self.countLigne +=1
        
    def addBusStops(self, busStops, numLigne):
        listTampon = []
        for i in busStops:
            exist = False
            for existingStops in self.listBusStop:
                if i == existingStops.name:
                    exist = True
                    existingStops.addLigne(numLigne)
            if not exist :
                busStop = BusStop()
                busStop.setName(i)
                busStop.addLigne(numLigne)
                listTampon.append(busStop)                
        self.fillListTrajet(numLigne, listTampon)
        self.listBusStop += listTampon
        
    def fillListTrajet(self, idLigne, listBusStop):
        for i in range(len(listBusStop)-1):
            trajet = Trajet(idLigne, listBusStop[i], listBusStop[i+1])
            self.listTrajet.append(trajet)
            
    def fillHoraires(self, dic, typeHoraire):
        for busStop in self.listBusStop:
            for key in dic.keys():
                if key == busStop.name:
                    
                    busStop.addHoraire(dic.get(key), typeHoraire)
                    break;
        
    def getBusStopByName(self, name):
        for i in self.listBusStop:
            if i.name == name:
                return i
        return None