#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from joueur import Joueur

class Partie:

    def __init__(self, fenetre,niveau,joueurs):
        self.fenetre = fenetre
        
        self.niveau = niveau
        self.joueurs = joueurs
        
        self.joueurCamera = self.joueurs[0]
        
        self.defilementX0 = 0
        self.defilementX1 = 0
        self.defilementX2 = 0
        self.defilementX3 = 0
    
    def start(self):
        
        #print self.niveau.surface
        for i, joueur in enumerate(self.joueurs):
            #print joueur.avion.hydravion
            joueur.positionX = joueur.positionX * (i+i)
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return -1
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return 0
            
            self.fenetre.blit(self.niveau.fond3,[0,0],[self.defilementX3,0,640,480])
            self.fenetre.blit(self.niveau.fond2,[0,0],[self.defilementX2,0,640,480])
            self.fenetre.blit(self.niveau.fond1,[0,0],[self.defilementX1,0,640,480])
            
            te=pygame.key.get_pressed()
            
            for joueur in self.joueurs:
                
                joueur.positionX += self.niveau.vitesse
                
                #No key pressed
                if te[joueur.touches['RIGHT']]==0 and te[joueur.touches['LEFT']]==0 and te[joueur.touches['UP']]==0 and te[joueur.touches['DOWN']]==0:
                    joueur.positionY += self.niveau.gravite + joueur.avion.lourd
     
                #Single key pressed
                if te[joueur.touches['RIGHT']]==1 and te[joueur.touches['LEFT']]==0 and te[joueur.touches['UP']]==0 and te[joueur.touches['DOWN']]==0:
                    if joueur.avion.inverseH:
                        joueur.positionX -=2 + joueur.avion.vitesse
                        joueur.avance = False
                    else:
                        joueur.positionX +=2 + joueur.avion.vitesse
                        joueur.avance = True           
    
                if te[joueur.touches['RIGHT']]==0 and te[joueur.touches['LEFT']]==1 and te[joueur.touches['UP']]==0 and te[joueur.touches['DOWN']]==0:
                    if joueur.avion.inverseH:
                        joueur.positionX +=2  + joueur.avion.vitesse
                        joueur.avance = True
                    else:
                        joueur.positionX -=2  + joueur.avion.vitesse
                        joueur.avance = False
    
                if te[joueur.touches['RIGHT']]==0 and te[joueur.touches['LEFT']]==0 and te[joueur.touches['UP']]==1 and te[joueur.touches['DOWN']]==0:
                    if joueur.avion.inverseV:
                        joueur.positionY +=2 + joueur.avion.vertigineux
                    else:
                        joueur.positionY -=2 + joueur.avion.vertigineux
    
                if te[joueur.touches['RIGHT']]==0 and te[joueur.touches['LEFT']]==0 and te[joueur.touches['UP']]==0 and te[joueur.touches['DOWN']]==1:
                    if joueur.avion.inverseV:
                        joueur.positionY -=2 + joueur.avion.lourd
                    else:
                        joueur.positionY +=2 + joueur.avion.lourd
    
                #Two key pressed : right
                if te[joueur.touches['RIGHT']]==1 and te[joueur.touches['LEFT']]==1 and te[joueur.touches['UP']]==0 and te[joueur.touches['DOWN']]==0:
                    if joueur.avion.inverseH:
                        joueur.positionX -=1  + joueur.avion.vitesse
                        joueur.avance = False  
                    else:
                        joueur.positionX +=1  + joueur.avion.vitesse
                        joueur.avance = True
    
                if te[joueur.touches['RIGHT']]==1 and te[joueur.touches['LEFT']]==0 and te[joueur.touches['UP']]==1 and te[joueur.touches['DOWN']]==0:
                    if joueur.avion.inverseH:
                        joueur.positionX -=1 + joueur.avion.vitesse
                        
                        joueur.avance = False
                    else:
                        joueur.positionX +=1 + joueur.avion.vitesse
                        joueur.avance = True
                    if joueur.avion.inverseV:
                        joueur.positionY +=1 + joueur.avion.vertigineux
                    else:
                        joueur.positionY -=1 + joueur.avion.vertigineux
                    
                if te[joueur.touches['RIGHT']]==1 and te[joueur.touches['LEFT']]==0 and te[joueur.touches['UP']]==0 and te[joueur.touches['DOWN']]==1:
                    if joueur.avion.inverseH:
                        joueur.positionX -=1 + joueur.avion.vitesse
                        joueur.avance = False
                    else:
                        joueur.positionX +=1 + joueur.avion.vitesse
                        joueur.avance = True
                    if joueur.avion.inverseV:
                        joueur.positionY -=1 + joueur.avion.lourd
                    else:
                        joueur.positionY +=1 + joueur.avion.lourd
    
                #Two key pressed : left
                if te[joueur.touches['RIGHT']]==0 and te[joueur.touches['LEFT']]==1 and te[joueur.touches['UP']]==1 and te[joueur.touches['DOWN']]==0:
                    if joueur.avion.inverseH:
                        joueur.positionX +=1 + joueur.avion.vitesse
                        joueur.avance = True
                    else:
                        joueur.positionX -=1 + joueur.avion.vitesse
                        joueur.avance = False
                    if joueur.avion.inverseV:
                        joueur.positionY +=1 + joueur.avion.vertigineux
                    else:
                        joueur.positionY -=1 + joueur.avion.vertigineux
     
                if te[joueur.touches['RIGHT']]==0 and te[joueur.touches['LEFT']]==1 and te[joueur.touches['UP']]==0 and te[joueur.touches['DOWN']]==1:
                    if joueur.avion.inverseH:
                        joueur.positionX +=1 + joueur.avion.vitesse
                        joueur.avance = True
                    else:
                        joueur.positionX -=1 + joueur.avion.vitesse
                        joueur.avance = False
                    if joueur.avion.inverseV:
                        joueur.positionY -=1 + joueur.avion.lourd
                    else:
                        joueur.positionY +=1 + joueur.avion.lourd
    
                #Two key pressed : up
                if te[joueur.touches['RIGHT']]==0 and te[joueur.touches['LEFT']]==0 and te[joueur.touches['UP']]==1 and te[joueur.touches['DOWN']]==1:
                    joueur.positionY += self.niveau.gravite + joueur.avion.lourd + joueur.avion.vertigineux
                
                if joueur.positionX > 6000 - 40:
                    joueur.positionX = 6000 - 40
                
                if joueur.positionX < 0:
                    joueur.positionX = 0
                    
                if joueur.positionY < self.niveau.plafond:
                    joueur.positionY = self.niveau.plafond
                    
                if joueur.positionY > self.niveau.sol:
                    joueur.positionY = self.niveau.sol
                    
                    if not((self.niveau.surface == "terre" and joueur.avion.roulant) or (self.niveau.surface == "mer" and joueur.avion.hydravion)):
                        joueur.explose = True
                
                #gestion du fond uniquement avec joueur0
                if joueur.positionX > 300 and joueur == self.joueurCamera:
                    self.defilementX0 = (joueur.positionX - 300) * 2
                    self.defilementX1 = (joueur.positionX - 300) * 1
                    self.defilementX2 = (joueur.positionX - 300) / 2
                    self.defilementX3 = (joueur.positionX - 300) / 3
                    
                    if self.defilementX1 > 6000-640:
                        self.defilementX1 = 6000-640
                        self.defilementX2 = self.defilementX1 / 2
                        self.defilementX3 = self.defilementX1 / 3
                        self.defilementX0 = self.defilementX1 * 2
                
                elif joueur.positionX < 300 and joueur == self.joueurCamera:
                    self.defilementX0 = 0
                    self.defilementX1 = 0
                    self.defilementX2 = 0
                    self.defilementX3 = 0

                for j in self.joueurs:
                    if not j.explose and j != joueur:
                        if joueur.positionX < (j.positionX + 40) and joueur.positionX > (j.positionX - 35) and joueur.positionY < (j.positionY + 20) and joueur.positionY > (j.positionY -20):
                            j.explose = True
                            joueur.explose = True

                if joueur.explose:
                    avion = joueur.getExplosion()
                    if not avion:
                        self.joueurs.remove(joueur)
                        if len(self.joueurs) >= 1:
                            self.joueurCamera = self.joueurs[0]
                        else:
                            return 0
                    else:
                        self.fenetre.blit(pygame.image.load(avion).convert(),(joueur.positionX - self.defilementX1,joueur.positionY))
                else:    
                    avion = joueur.getAvion()
                    self.fenetre.blit(pygame.image.load(avion).convert(),(joueur.positionX - self.defilementX1,joueur.positionY))

            self.fenetre.blit(self.niveau.fond0,[0,0],[self.defilementX0,0,640,480])
            
            pygame.display.flip()