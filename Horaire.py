# -*- coding: utf-8 -*-

class Horaire:
    
    def __init__(self, typeHoraire, listHoraire):
        self.typeHoraire = typeHoraire
        self.listHoraire = listHoraire
        
    
    
    
# =============================================================================
#     Type Horaire
# =============================================================================
# 0 -> Aller/Période scolaire
# 1 -> Retour/Période scolaire
# 2 -> Aller/Période Vacance
# 3 -> Retour/Période Vacance