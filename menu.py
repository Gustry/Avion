#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import os
import re

class Menu:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        
        self.nbMenu = 0
        for menu in os.listdir("menu"):
            if re.search("menu[0-9].png",menu):
                self.nbMenu += 1
                
        self.choixmenu = 1
        
    def loop(self):
        while True:
            menu = pygame.image.load("menu/menu"+str(self.choixmenu)+".png")
            for event in pygame.event.get():
                if event.type == QUIT:
                    return -1
                
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE:
                        return 0
                    
                    if event.key == K_UP:
                        self.choixmenu -= 1
                        if self.choixmenu == 0:
                            self.choixmenu = self.nbMenu
                            
                    if event.key == K_DOWN:
                        self.choixmenu+=1
                        if self.choixmenu == self.nbMenu + 1:
                            self.choixmenu = 1
                            
                    if event.key == K_RETURN:
                        return self.choixmenu
                    
            self.fenetre.blit(menu, (0,0))
            pygame.display.flip()