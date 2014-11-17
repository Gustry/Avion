#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

class Regle:

    def __init__(self,fenetre):
        self.fenetre = fenetre
        self.menu = pygame.image.load("menu/regle.png")
    
    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return -1
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return 1
            self.fenetre.blit(self.menu, (0,0))
            pygame.display.flip()