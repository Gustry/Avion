#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from menu import Menu
from regle import Regle
from Niveau import Niveau
from joueur import Joueur
from partie import Partie

class Game:

    def __init__(self):
        self.fenetre = pygame.display.set_mode((640,480))
        
    def start(self):
        pygame.display.flip()
        
        menu = Menu(self.fenetre)
        
        askToExit = False
        while not askToExit:
            for event in pygame.event.get():
                if event.type == QUIT:
                    askToExit = True
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        askToExit = True
            
            choix = menu.loop()
            if choix <=0:
                askToExit = True
            
            if choix == 4:
                regle = Regle(self.fenetre)
                regle = regle.loop()
                if regle <=0:
                    askToExit = True
            
            if choix == 1:                
                niveau = Niveau(1)
                joueurs = [Joueur(1),Joueur(1)]
                partie = Partie(self.fenetre,niveau,joueurs)
                askToExit = partie.start()
                Joueur.i = 1