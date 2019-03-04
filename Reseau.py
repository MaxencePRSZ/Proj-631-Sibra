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
        """Recupère le nombre de ligne de bus contenu dans l'objet reseau
    
        Parameters
        ----------
        self : self
            l'objet lui-même
    
        Returns
        -------
        int
            nombre de ligne contenu dans l'attribut countLigne de l'objet reseau
        """        
        return self.countLigne
    
    def incrementCountLigne(self):
        """incrémente le nombre de ligne de bus contenu dans l'objet reseau
    
        Parameters
        ----------
        self : self
            l'objet lui-même
    
        Returns
        -------
        """ 
        self.countLigne +=1
                
    def addBusStops(self, busStops, numLigne):
        """Ajout d'un arret de bus dans la liste des arret du reseau et création 
            des connexions entre les arrets
    
        Parameters
        ----------
        self : self
            l'objet lui-même
        list<busStops> : busStops
            liste des arrets de bus à ajouter
        int : numLigne
            numéro de ligne des arrets qu'on ajoute
    
        Returns
        -------
        """ 
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
        """Complete les arcs entre les noeuds (representés par les arrets de bus)
            l'ordre des arrets va determiner les connexions entre eux
    
        Parameters
        ----------
        self : self
            l'objet lui-même
        int : idLigne
            l'id de la ligne sur laquelle on connecte les arrets
        list<busStops> : listBusStop
            une liste des arrets de bus qui doivent être connecté entre eux
        Returns
        -------
        """ 
        for i in range(len(listBusStop)-1):
            trajet = Trajet(idLigne, listBusStop[i], listBusStop[i+1])
            self.listTrajet.append(trajet)
            
    def fillHoraires(self, dic, typeHoraire):
        """rempli les horaires de chaque arret de bus
    
        Parameters
        ----------
        self : self
            l'objet lui-même
        dict : dic
            dictionnaire contenant les horaires
        int : typeHoraire
            type de l'horaire qui va etre renseigné (voir commentaire dans Horaire.py)
        Returns
        -------
        """
        for busStop in self.listBusStop:
            for key in dic.keys():
                if key == busStop.name:
                    busStop.addHoraire(dic.get(key), typeHoraire)
                    break;
        
    def getBusStopByName(self, name):
        """recupère l'objet busStop en renseignant en paramètre son nom
    
        Parameters
        ----------
        self : self
            l'objet lui-même
        string : name
            nom de l'arret recherché
        Returns
        -------
        BusStop:    
            l'objet busStop ayant le nom passé en paramètre, ou none si non existant
        """    
        for i in self.listBusStop:
            if i.name == name:
                return i
        return None
      
    def getNeighbors(self, busStop):
        """recupère les voisins de l'arret passé en paramètre
    
        Parameters
        ----------
        self : self
            l'objet lui-même
        BusStop : busStop
            l'objet BusStop auquel on cherche ses voisins
        int : typeHoraire
            type de l'horaire qui va etre renseigné (voir commentaire dans Horaire.py)
        Returns
        -------
        list<BusStop>
            liste d'arret qui sont les voisins de l'objet passé en paramètre
        """   
        ret = []
        for i in self.listTrajet:
            if busStop == i.busStop1 or busStop == i.busStop2:
                ret.append(i.busStop1)
                ret.append(i.busStop2)
        ret = list(set(ret) - set([busStop]))
        return ret

    def findMinDateTime(self, dicTime, busStops):
        """Recherche l'arret de bus ayant le plus petit horaire,
        utile pour savoir quel element sera le suivant pour DjikstraForemost
    
        Parameters
        ----------
        self : self
            l'objet lui-même
        dict : dicTime
            dictionnaire avec pour key-> busStop et value -> datetime
        list<busStop> : busStops
            liste des arrets qui ont été visité d'ores et deja
        Returns
            tuple :
                l'arret avec l'horaire minimum
        -------
        """   
        mini, busStop = self.MAXTIME, None
        for key, value in dicTime.items():
            if key in busStops:
                continue
            if value <= mini :
                mini = value
                busStop = key
        return (busStop, mini)
    
    def sensBus(self, busStop1, busStop2):
        """Retourne le sens dans lequel le bus se déplace, dépendant des 
        arrets qu'il a pris
    
        Parameters
        ----------
        self : self
            l'objet lui-même
        BusStop : busStop1
            premier arret que le bus va visiter
        BusStop  : busStop2
            second arret que le bus va visiter
        Returns
            int :
                0 si le bus est sur l'aller
                1 si le bus est sur le retour
               -1 si les arrets ne sont pas connectés
        -------
        """ 
        for i in self.listTrajet:
            if i.busStop1 == busStop1 and i.busStop2 == busStop2:
                return 0
            if i.busStop2 == busStop1 and i.busStop1 == busStop2:
                return 1
        return -1
    
    def getLigneId(self, busStop1, busStop2):
        """Retourne la ligne de bus qu'ont en commun les deux arrets
    
        Parameters
        ----------
        self : self
            l'objet lui-même
        BusStop : busStop1
            premier arret que le bus va visiter
        BusStop  : busStop2
            second arret que le bus va visiter
        Returns
            int :
                l'id de la ligne en commun sur les deux arrets
        -------
        """ 
        return list(set(busStop1.idLignes).intersection(busStop2.idLignes))[0]
        
# =============================================================================
# https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
# =============================================================================
    def djikstraShortest(self, depart, arrivee):
        """Calcule le chemin le plus court entre 2 arrets
    
        Parameters
        ----------
        self : self
            l'objet lui-même
        BusStop : depart
            l'arret à partir duquel on veut partir
        BusStop  : arrivee
            l'arret sur lequel on veut arriver
        Returns
            list :
                la liste des arrets que l'on doit traverser pour aller du départ
                à l'arrivée (dans l'ordre)
        -------
        """ 
        distances = {busStop: float("inf") for busStop in self.listBusStop}
        precedents = {busStop: None for busStop in self.listBusStop}
        distances[depart] = 0

        busStops = self.listBusStop.copy()
        while busStops:
            current_busStop = min(busStops, key=lambda busStop: distances[busStop])
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
        
        
    def djikstraForemost(self, depart, arrivee, heure):
        """Calcule le chemin qui nous fait arriver au plus tot depuis un départ
        vers une arrivée à partir d'une heure indiquée
    
        Parameters
        ----------
        self : self
            l'objet lui-même
        BusStop : depart
            l'arret à partir duquel on veut partir
        BusStop  : arrivee
            l'arret sur lequel on veut arriver
        str : heure
            string indiquant l'heure à laquelle on veut partir, dans le format
            "MM:SS"
        Returns
            dict :
                le dictionnaire des arrets que l'on doit traverser pour aller du départ
                à l'arrivée avec les horaires respectives (dans l'ordre inverse)
        -------
        """ 
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
        
        
        