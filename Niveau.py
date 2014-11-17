#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

class Niveau:

    def __init__(self, idNiveau):
        idNiveau = str(idNiveau)
        self.fond0 = pygame.image.load("niveaux/niv"+idNiveau+"/fond0.png")
        self.fond1 = pygame.image.load("niveaux/niv"+idNiveau+"/fond1.png")
        self.fond2 = pygame.image.load("niveaux/niv"+idNiveau+"/fond2.png")
        self.fond3 = pygame.image.load("niveaux/niv"+idNiveau+"/fond3.png")
        
        self.sol = 460
        self.surface = None
        self.plafond = 0
        self.gravite = 1
        self.vitesse = 0
        
        with open("niveaux/niv"+ idNiveau +"/particularites.txt", "r") as particularites:
            for i,codeligne in enumerate(particularites):
                elements = codeligne.split("=")
                
                if i == 0:
                    self.sol = int(elements[1])
                
                if i == 1:
                    self.surface = elements[1].replace("\n", " ")
                    self.surface = self.surface.strip()
                
                if i == 2:
                    self.plafond = int(elements[1])
                    
                if i == 3:
                    self.gravite = int(elements[1])
                    
                if i == 4:
                    self.vitesse = int(elements[1])
