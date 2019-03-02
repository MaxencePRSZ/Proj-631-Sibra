from BusStop import BusStop
from Trajet import Trajet
from collections import OrderedDict
from datetime import datetime, timedelta

# -*- coding: utf-8 -*-

class Reseau:
    
    def __init__(self):
        self.listBusStop = []
        self.listTrajet = []
        self.countLigne = 0
    MAXTIME = datetime.strptime("23:59", "%H:%M")
            
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
        ret = list(set(ret) - set([busStop]))
        return ret

    def findMinDateTime(self, dicTime, busStops):
        mini = self.MAXTIME
        busStop = None
        passe = False
        for key, value in dicTime.items():
            for i in busStops:
                if i == key:
                    passe = True
            if passe:
                passe = False
                continue
            if type(value) is str:
                value = datetime.strptime(value, "%H:%M")
            if value <= mini :
                mini = value
                busStop = key
        return (busStop, mini)
        
# =============================================================================
# https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
# =============================================================================
    def djikstra(self, depart, arrivee):
        distances = {busStop: float("inf") for busStop in self.listBusStop}
        precedents = {busStop: None for busStop in self.listBusStop}
        distances[depart] = 0
        busStops = self.listBusStop.copy()
        while busStops:
            current_busStop = min(busStops, key=lambda busStop: distances[busStop])
            print(len(distances), len(busStops))
#           test if the shortest distance among the unvisited busStop is inf
#           If yes, then break and let's pursue the algorithm with another BS
            if distances[current_busStop] == float("inf"):
                break    
            for i in self.getNeighbors(current_busStop):
                new_value = distances[current_busStop] + 1        
                if new_value < distances[i]:
                    distances[i] = new_value
                    precedents[i] = current_busStop            
            busStops.remove(current_busStop)
        ret = []
        busStop = arrivee
        while precedents[busStop] is not None:
            ret.append(busStop)
            busStop = precedents[busStop]
        ret.append(depart)
        return list(reversed(ret))
        
        
    def djikstraFastest(self, depart, arrivee, heure):
        distances = {busStop: self.MAXTIME for busStop in self.listBusStop}
        precedents = {busStop: None for busStop in self.listBusStop}
        typeHoraire, indice = depart.findTypeHoraire(arrivee, heure)
        distances[depart] = depart.listHoraires[typeHoraire].listHoraire[indice]
        busStops = []
        
        while len(busStops) != len(distances):
            current_busStop = self.findMinDateTime(distances, busStops)[0]
            if distances[current_busStop] == self.MAXTIME:
                break
            
            for i in self.getNeighbors(current_busStop):
                if i.listHoraires[typeHoraire].listHoraire[indice] == "-":
                    new_value = distances[current_busStop] + timedelta(seconds=6)
                else:
                    new_value = i.listHoraires[typeHoraire].listHoraire[indice]
                if new_value < distances[i]:
                    distances[i] = new_value
                    precedents[i] = current_busStop
            busStops.append(current_busStop)
        
        ret = []
        busStop = arrivee
        while precedents[busStop] is not None:
            ret.append(busStop.name)
            busStop = precedents[busStop]
        ret.append(depart.name)
        return list(reversed(ret))
        
        
        
        
        
        
        
        