#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Avion import Avion
import pygame

class Joueur:
    
    i = 1

    def __init__(self,idAvion):
        self.id = Joueur.i
        Joueur.i += 1
        
        self.avion = Avion(idAvion)
        self.avance = True
        self.positionX = 32
        self.positionY = 12*16
        self.numExplosion = 0
        self.explose = False
        self.getTouches()
        
    def getAvion(self):
        if self.avance:
            return self.avion.droite
        else:
            return self.avion.gauche

    def getExplosion(self):
        self.numExplosion +=1
        if self.numExplosion > 6:
            return False
        return self.avion.getExplosion(self.numExplosion)
        
    def getTouches(self):
        with open("touches.txt", "r") as touches:
            for i,ligne in enumerate(touches):
                if i+1 == self.id:
                    csv = ligne.split(",")
                    self.touches = {"LEFT" : eval("pygame.K_" + csv[0]), "RIGHT" : eval("pygame.K_" + csv[1]), "UP" : eval("pygame.K_" + csv[2]),"DOWN" : eval("pygame.K_" + csv[3])}