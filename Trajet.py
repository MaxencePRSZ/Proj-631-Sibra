from BusStop import BusStop
# -*- coding: utf-8 -*-

class Trajet:
    
    def __init__(self, idLigne, bstp1, bstp2):
        self.idLigne = idLigne
        self.busStop1 = bstp1
        self.busStop2 = bstp2
        
    def setIdLigne(self, idLigne):
        self.idLigne = idLigne
        
    def setBusStop1(self, busStop):
        self.busStop1 = busStop
        
    def setBusStop2(self, busStop):
        self.busStop2 = busStop