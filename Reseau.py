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
      
    def getNeighbors(self, busStop):
        ret = []
        for i in self.listTrajet:
            if busStop == i.busStop1 or busStop == i.busStop2:
                ret.append(i.busStop1)
                ret.append(i.busStop2)
        ret = list(set(ret) - set([busStop]))
        return ret

    def findMinDateTime(self, dicTime, busStops):
        mini, busStop = self.MAXTIME, None
        for key, value in dicTime.items():
            if key in busStops:
                continue
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
<<<<<<< HEAD
        busStops = self.listBusStop
        
#        while busStops:
=======
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
        dictLigne = dict({idLigne : (indice, typeHoraire) for idLigne in depart.idLignes})
        distances[depart] = depart.listHoraires[typeHoraire].listHoraire[indice]
        busStops = []
        
        while len(busStops) != len(distances):
            current_busStop, current_horaire = self.findMinDateTime(distances, busStops)
            if distances[current_busStop] == self.MAXTIME:
                break
>>>>>>> c16814ebb488f7236d5ef0e76c1dcd86630f1c20
            
            for i in self.getNeighbors(current_busStop):
#               Si on rencontre un horaire '-', on prétend que le bus y passera
#               dans un certain temps - à mieux gérer si j'ai le temps
                if len(current_busStop.idLignes) > 1:
                    for j in current_busStop.idLignes:
                        if j not in list(dictLigne.keys()):
                            th, ind = current_busStop.findTypeHoraire(arrivee, distances[current_busStop])
                            dictLigne.update({j : (ind, th)})
                            
                ind_voisin, tH_voisin = dictLigne[i.idLignes[0]]
                
                if i.listHoraires[tH_voisin].listHoraire[ind_voisin] == "-":
                    new_value = distances[current_busStop] + timedelta(seconds=6)
                    
                else:
                    new_value = i.listHoraires[tH_voisin].listHoraire[ind_voisin]
                if new_value < distances[i]:
                    distances[i] = new_value
                    precedents[i] = current_busStop
            busStops.append(current_busStop)
        
        ret = {}
        busStop = arrivee
        while precedents[busStop] is not None:
            ret.update({busStop.name : str(distances[busStop].time())})
            busStop = precedents[busStop]
        ret.update({depart.name : str(distances[depart].time())})
        return ret
        
        
        