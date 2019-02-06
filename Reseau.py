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
        for i in busStops:
            exist = False
            for existingStops in self.listBusStop:
                if i == existingStops.name:
                    exist = True
            if not exist :
                busStop = BusStop()
                busStop.setName(i)
                busStop.addLigne(numLigne)
                self.listBusStop.append(busStop)
            else :
                
        self.fillListTrajet(numLigne)
        
    def fillListTrajet(self, idLigne):
        for i in range(len(self.listBusStop)-1):
            trajet = Trajet(idLigne, self.listBusStop[i], self.listBusStop[i+1])
            self.listTrajet.append(trajet)
            
    def fillHoraires(self, dic, typeHoraire):
        for busStop in self.listBusStop:
            for key in dic.keys():
                if key == busStop.name:
                    busStop.addHoraire(dic.get(key), typeHoraire)
                    break;
        
    def getBusStopByName(self, name):
        return