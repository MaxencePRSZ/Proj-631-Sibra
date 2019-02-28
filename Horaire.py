# -*- coding: utf-8 -*-
from datetime import datetime

class Horaire:
    
    def __init__(self, typeHoraire, listHoraire):
        self.typeHoraire = typeHoraire
        self.listHoraire = listHoraire
        
    def findIndice(self, heure):
        hour = datetime.strptime(heure, '%H:%M')
        for count, i in enumerate(self.listHoraire):
            if i == "-":
                continue
            horaire = datetime.strptime(i, '%H:%M')
            if hour <= horaire:
                return count
        return None
            
        
    
    
    
# =============================================================================
#     Type Horaire
# =============================================================================
# 0 -> Aller/Période scolaire
# 1 -> Retour/Période scolaire
# 2 -> Aller/Période Vacance
# 3 -> Retour/Période Vacance