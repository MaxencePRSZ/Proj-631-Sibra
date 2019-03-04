# -*- coding: utf-8 -*-
from datetime import datetime

class Horaire:
    
    def __init__(self, typeHoraire, listHoraire):
        self.typeHoraire = typeHoraire
        for key, value in enumerate(listHoraire):
            if value == "-":
                continue
            listHoraire[key] = datetime.strptime(value, '%H:%M')
        self.listHoraire = listHoraire
        
    def findIndice(self, heure):
        """Retrouve l'indice qui va nous permettre de savoir quelle horaire le
        bus doit prendre pour être au plus tot
    
        Parameters
        ----------
        self : self
            l'objet lui-même
        datetime  : heure
            l'heure du départ
        Returns
        -------
            int :
                l'indice qui va nous permettre de retrouver l'horaire dans le liste
                des horaires
        """ 
        if type(heure) == str:
            heure = datetime.strptime(heure, '%H:%M')
        for count, i in enumerate(self.listHoraire):
            if i == "-":
                continue
            if heure <= i:
                return count
        return None
    
          
        
    
    
    
# =============================================================================
#     Type Horaire
# =============================================================================
# 0 -> Aller/Période scolaire
# 1 -> Retour/Période scolaire
# 2 -> Aller/Période Vacance
# 3 -> Retour/Période Vacance