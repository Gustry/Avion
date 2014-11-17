#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Avion:

    def __init__(self, idAvion):
        self.idAvion = str(idAvion)
        self.droite = "avion/avion"+ self.idAvion+"/droite1.png"
        
        self.gauche = "avion/avion"+ self.idAvion+"/gauche1.png"
        
        self.roulant = False
        self.hydravion = False
        self.vitesse = 0
        self.lourd = 0
        self.vertigineux = 0
        self.inverseV = False
        self.inverseH = False
        
        with open("avion/avion"+ self.idAvion +"/modele.txt", "r") as particularites:
            for i,codeligne in enumerate(particularites):
                elements = codeligne.split("=")
                
                if i == 0:
                    self.roulant = eval(elements[1])
                
                if i == 1:
                    self.hydravion = eval(elements[1])
                
                if i == 2:
                    self.vitesse = int(elements[1])
                    
                if i == 3:
                    self.lourd = int(elements[1])
                    
                if i == 4:
                    self.vertigineux = int(elements[1])

                if i == 5:
                    self.inverseV = eval(elements[1])

                if i == 6:
                    self.inverseH = eval(elements[1])
                        
    def getExplosion(self,num):
        return "avion/avion"+ self.idAvion+"/explosion" + str(num) + ".png"