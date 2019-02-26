from BusStop import BusStop
from Trajet import Trajet
from collections import OrderedDict
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
            for existingStop in self.listBusStop:
                if i == existingStop.name:
                    exist = True
                    existingStop.addLigne(numLigne)
                    listTampon.append(existingStop)
            if not exist :
                busStop = BusStop()
                busStop.setName(i)
                busStop.addLigne(numLigne)
                listTampon.append(busStop)                
        self.fillListTrajet(numLigne, listTampon)
        self.listBusStop += listTampon
        self.listBusStop = list(OrderedDict.fromkeys(self.listBusStop))
        
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
    
    
    def breadthFirstSearch(self, depart):
#        Créer la liste des busStop visités
        visited = [False] * len(self.listBusStop)
#        Créer la liste des busStop à visiter (vide pour le moment)
        queue = []
#        Le noeud de départ doit être dans visité
        queue.append(depart)
        visited[0] = True
      
    def getNeighbors(self, busStop):
        ret = []
        for i in self.listTrajet:
            if busStop == i.busStop1 or busStop == i.busStop2:
                ret.append(i.busStop1)
                ret.append(i.busStop2)
        ret = set(ret) - set([busStop])
        return ret

        
# =============================================================================
# https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
# =============================================================================
    def djikstra(self, depart, arrivee):
        distances = {busStop: float("inf") for busStop in self.listBusStop}
        precedents = {busStop: None for busStop in self.listBusStop}
        distances[depart] = 0
        busStops = self.listBusStop
        
#        while busStops:
            
        
        
        
        
        
        
        
        
        
        
        
        