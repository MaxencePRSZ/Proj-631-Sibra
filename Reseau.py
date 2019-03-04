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
    
    def sensBus(self, busStop1, busStop2):
        for i in self.listTrajet:
            if i.busStop1 == busStop1 and i.busStop2 == busStop2:
                return 0
            if i.busStop2 == busStop1 and i.busStop1 == busStop2:
                return 1
        return -1
    
    def getLigneId(self, busStop1, busStop2):
        return list(set(busStop1.idLignes).intersection(busStop2.idLignes))[0]
        
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
        print(typeHoraire)
#        dictLigne = dict({idLigne : (indice, typeHoraire) for idLigne in depart.idLignes})
        distances[depart] = depart.listHoraires[typeHoraire].listHoraire[indice]
        busStops = []
        
        while len(busStops) != len(distances):
            current_busStop, current_horaire = self.findMinDateTime(distances, busStops)
            if distances[current_busStop] == self.MAXTIME:
                break
            
            for i in self.getNeighbors(current_busStop):
#               Si on rencontre un horaire '-', on prétend que le bus y passera
#               dans un certain temps - à mieux gérer si j'ai le temps
                idLine = self.getLigneId(current_busStop, i)
                tH_voisin = self.sensBus(current_busStop, i)
                ind_voisin = i.listHoraires[tH_voisin].findIndice(distances[current_busStop])

                if len(i.idLignes) > 1:
                    tH_voisin = (idLine-1)*4 + tH_voisin

                while i.listHoraires[tH_voisin].listHoraire[ind_voisin] == "-":
                    ind_voisin += 1
                
                new_value = i.listHoraires[tH_voisin].listHoraire[ind_voisin]
                if new_value < distances[i]:
                    distances[i] = new_value
                    precedents[i] = current_busStop
            busStops.append(current_busStop)
        
        ret = {}
        busStopsDepart = []
        busStop = arrivee
        while precedents[busStop] is not None:
            ret.update({busStop.name : str(distances[busStop].time())})
            busStop = precedents[busStop]
            busStopsDepart.append(busStop)
            
        idLine = self.getLigneId(depart, busStopsDepart[len(busStopsDepart)-2])
        tH_depart = self.sensBus(depart, busStopsDepart[len(busStopsDepart)-2])
        if len(i.idLignes) > 1:
            tH_depart = (idLine-1)*4 + tH_voisin
        ind_depart = depart.listHoraires[tH_depart].findIndice(heure)
        distances[depart] = depart.listHoraires[tH_depart].listHoraire[ind_depart]
        
        ret.update({depart.name : str(distances[depart].time())})
        return ret
        
        
        