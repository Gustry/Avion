#!/usr/bin/env python
# -*- coding: utf-8 -*-
#I - INTRODUIRE PYGAME
import pygame
from pygame.locals import *
pygame.init()
import os

#I - 1 : On affiche la fenetre
fenetre = pygame.display.set_mode((640, 480))
pygame.display.flip()
pygame.time.wait(50)

#I - 2 : Les variables qu'on utilisera plus tard mais qu'on affiche maintenant par sécurité
continuer = 1
menufleche = 1
accueil = 0
niveau = 0
partie=0
temps=1
explosion=0
jeu=0
typeavion=1
typeavion2=1
typeavion3=1
mode2=0
debut=1
choixmenu=1
regle=0
clavier=0
azerty=1
nombrejoueurs=1
numeromine=""
tempsretour=0

#Notion temporelle
horloge=pygame.time.Clock()

nombreniveau=0

#Le For in qui va compter le nombre de dossier dans le repertoire "niveaux", ainsi on sait combien il y a de niveaux.
listeniveaux=os.listdir("niveaux")
for dossiers in listeniveaux:
		nombreniveau+=1
		
nombreavions=0

#Le For in qui va compter le nombre de dossier dans le repertoire "avions", ainsi on sait combien il y a d'avions.
listeavions=os.listdir("avion")
for dossiersavion in listeavions:
		nombreavions+=1

#musique = pygame.mixer.Sound("menu/musique.wav")
#musique.play()
musiquemenu=0

#GRANDE BOUCLE
#La Grande Boucle est celle qui integre toutes les autres boucles du jeu
while continuer:
	horloge.tick(10)
	avion_x=32
	avion_y=12*16
	avion_x2=94
	avion_y2=12*16
	avion_x3=94+64
	avion_y3=12*16
	defilement_x0=0
	defilement_x1=0
	defilement_x2=0
	defilement_x3=0
	defilement_y0=0
	defilement_y1=0
	defilement_y2=0
	defilement_y3=0
	direction="droite"
	direction2="droite"
	direction3="droite"
	
	#II - Le Menu au debut
	#II - 1 : Le menu principal ou on peut choisir le nombre de joueur, les regles du jeu et le clavier...
	while debut:
		menu = pygame.image.load("menu/menu"+str(choixmenu)+".png")
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer=0
				debut=0
			if event.type == KEYDOWN:
				if event.key == K_UP:
					if choixmenu!=1:
						choixmenu-=1
					else:
						choixmenu=4
				if event.key == K_DOWN:
					if choixmenu!=4:
						choixmenu+=1
					else:
						choixmenu=1
				if event.key == K_RETURN:
					if choixmenu==1:
						accueil=1
						mode2=0
						accueil=1
						debut=0
						nombrejoueurs=1
					if choixmenu==2:
						accueil=1
						mode2=1
						accueil=1
						debut=0
						nombrejoueurs=2
					if choixmenu==3:
						accueil=1
						mode2=1
						accueil=1
						debut=0
						nombrejoueurs=3
					if choixmenu==4:
						regle=1
						debut=0
		fenetre.blit(menu, (0,0))
		pygame.display.flip()
		
	#II - 2 : Le menu regle, il est tres simple car composé d'une seule image.
	while regle:
		menu = pygame.image.load("menu/regle.png")
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer=0
				debut=0
				regle=0
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					regle=0
					debut=1
		fenetre.blit(menu, (0,0))
		pygame.display.flip()
	#II - 3 : Le menu clavier, tres simple aussi, autant que regle.	 IL N'EST PLUS UTILISE !!!			
	while clavier:
		if azerty:
			menu = pygame.image.load("menu/azerty.png")
			fenetre.blit(menu, (0,0))
			pygame.display.flip()
		if azerty==0:
			menu = pygame.image.load("menu/qwerty.png")
			fenetre.blit(menu, (0,0))
			pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer=0
				debut=0
				clavier=0
			if event.type == KEYDOWN:
				if event.key == K_UP:
					if azerty:
						azerty=0
					else:
						azerty=1
				if event.key == K_DOWN:
					if azerty:
						azerty=0
					else:
						azerty=1
				if event.key == K_ESCAPE:
					clavier=0
					debut=1
				if event.key == K_RETURN:
					clavier=0
					debut=1

	#II - 4 : Le 3eme sous menu est celui de selection des niveaux, il merite a lui seul une III partie.
	
	#III - Le menu de choix des niveaux (c'est le meme pour 1 joueur ou 2 joueurs)
	while accueil:
		
		#III - 1 : Au tout debut on choisi le niveau et l'avion avec les fleches, puis on valide avec entree.
		retour=0
		#if musiquemenu:
		#	musique = pygame.mixer.Sound("menu/musique.wav")
		#	musique.play()
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer=0
				accueil=0
			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					if menufleche!=nombreniveau:
						menufleche+=1
					elif menufleche==nombreniveau:
						menufleche=1			
				if event.key == K_LEFT:
					if menufleche!=1:
						menufleche-=1
					elif menufleche==1:
						menufleche=nombreniveau
				if event.key == K_RETURN:
					jeu=1
					niveau=1
					accueil=0
				if event.key == K_ESCAPE:
					accueil=0
					debut=1
				#Avion 1
				if event.key == K_UP:
					if typeavion!=1:
						typeavion-=1
					else:
						typeavion=nombreavions
				if event.key == K_DOWN:
					if typeavion!=nombreavions:
						typeavion+=1
					else:
						typeavion=1
				#Avion 2
				if event.key == K_w:
					if typeavion2!=1:
						typeavion2-=1
					else:
						typeavion2=nombreavions
				if event.key == K_s:
					if typeavion2!=nombreavions:
						typeavion2+=1
					else:
						typeavion2=1
				#Avion 3
				if event.key == K_t:
					if typeavion3!=1:
						typeavion3-=1
					else:
						typeavion3=nombreavions
				if event.key == K_g:
					if typeavion3!=nombreavions:
						typeavion3+=1
					else:
						typeavion3=1
		menu = pygame.image.load("niveaux/niv"+str(menufleche)+"/menu"+str(nombrejoueurs)+".png")
		fenetre.blit(menu, (0,0))
		if nombrejoueurs==1:
			menuavion = pygame.image.load("avion/avion"+str(typeavion)+"/droite.png")
			fenetre.blit(menuavion, (300,380))
		if nombrejoueurs==2:
			menuavion = pygame.image.load("avion/avion"+str(typeavion)+"/droitebleu.png")
			menuavion2 = pygame.image.load("avion/avion"+str(typeavion2)+"/droiterouge.png")
			fenetre.blit(menuavion, (400,380))
			fenetre.blit(menuavion2, (200,380))
		if nombrejoueurs==3:
			menuavion = pygame.image.load("avion/avion"+str(typeavion)+"/droitebleu.png")
			menuavion2 = pygame.image.load("avion/avion"+str(typeavion2)+"/droiterouge.png")
			menuavion3 = pygame.image.load("avion/avion"+str(typeavion3)+"/droitevert.png")
			fenetre.blit(menuavion, (435,380))
			fenetre.blit(menuavion2, (165,380))
			fenetre.blit(menuavion3, (300,380))
		pygame.display.flip()
	#III - 2 : On sort de la boucle Accueil et on crée toutes ces nouvelles variables qui sont mises a zero
	gravite=0
	mer=0
	terre=0
	vitesse=0
	ciel=0
	hydravion=0
	roulant=0
	chasse=0
	lourd=0
	vertigineux=0
	tordu=0
	hydravion2=0
	roulant2=0
	chasse2=0
	lourd2=0
	vertigineux2=0
	tordu2=0
	hydravion3=0
	roulant3=0
	chasse3=0
	lourd3=0
	vertigineux3=0
	tordu3=0
	fond0mouv=0
	fond1mouv=0
	fond2mouv=0
	fond3mouv=0
	
	#III - 3 : On ouvre le fichier integre dans le dossier du niveau choisi (menufleche)
	#On actionne les variables qu'on avait mis a zero juste avant
	with open("niveaux/niv"+str(menufleche)+"/particularites.txt", "r") as particularites:
			for codeligne in particularites:
				for code in codeligne:
					if code=="g":
						gravite=1
					if code=="v":
						vitesse=1
					if code=="m":
						mer=1
					if code=="t":
						terre=1
					if code=="c":
						ciel=1
					if code=="0":
						fond0mouv=1
					if code=="1":
						fond1mouv=1
					if code=="2":
						fond2mouv=1
					if code=="3":
						fond3mouv=1
	#III - 4 : On ouvre le fichier dans le dossier avion
	with open("avion/avion"+str(typeavion)+"/modele.txt", "r") as particularites:
			for codeligne in particularites:
				for code in codeligne:
					if code=="h":
						hydravion=1
					if code=="r":
						roulant=1
					if code=="c":
						chasse=1
					if code=="l":
						lourd=1
					if code=="v":
						vertigineux=1
					if code=="t":
						tordu=1
	#III - 5 : On ouvre le fichier pour le joueur2, qu'on soit en mode 1 joueur ou 2 joueurs, il le fera quand meme
	with open("avion/avion"+str(typeavion2)+"/modele.txt", "r") as particularites:
			for codeligne in particularites:
				for code in codeligne:
					if code=="h":
						hydravion2=1
					if code=="r":
						roulant2=1
					if code=="c":
						chasse2=1
					if code=="l":
						lourd2=1
					if code=="v":
						vertigineux2=1
					if code=="t":
						tordu2=1
	with open("avion/avion"+str(typeavion3)+"/modele.txt", "r") as particularites:
			for codeligne in particularites:
				for code in codeligne:
					if code=="h":
						hydravion3=1
					if code=="r":
						roulant3=1
					if code=="c":
						chasse3=1
					if code=="l":
						lourd3=1
					if code=="v":
						vertigineux3=1
					if code=="t":
						tordu3=1
	#IV - On lance enfin le jeu, avec decors, avion et obstacles... On sort du menu !
	while jeu:
		#On annonce les decors des niveaux
		musiquemenu=1
		#IV - 1 : Referencement des images de fond de niveau sans les afficher
		#On affiche tout qu'une fois dans cette boucle "niveau"
		pygame.mixer.stop()

		fond0=pygame.image.load("niveaux/niv"+str(menufleche)+"/fond0.png").convert()
		fond1=pygame.image.load("niveaux/niv"+str(menufleche)+"/fond1.png").convert()
		fond2=pygame.image.load("niveaux/niv"+str(menufleche)+"/fond2.png").convert()
		fond3=pygame.image.load("niveaux/niv"+str(menufleche)+"/fond3.png").convert()
		#musique=pygame.mixer.Sound("niveaux/niv"+str(menufleche)+"/musique.wav")
		if nombrejoueurs==1:
			aviondroite = "avion/avion"+str(typeavion)+"/droite.png"
			aviongauche = "avion/avion"+str(typeavion)+"/gauche.png"
			aviondroite2 = "avion/avion"+str(typeavion)+"/droite.png"
			aviongauche2 = "avion/avion"+str(typeavion)+"/gauche.png"
			aviondroite3 = "avion/avion"+str(typeavion)+"/droite.png"
			aviongauche3 = "avion/avion"+str(typeavion)+"/gauche.png"
		if nombrejoueurs==2:
			aviondroite = "avion/avion"+str(typeavion)+"/droitebleu.png"
			aviongauche = "avion/avion"+str(typeavion)+"/gauchebleu.png"
			aviondroite2 = "avion/avion"+str(typeavion2)+"/droiterouge.png"
			aviongauche2 = "avion/avion"+str(typeavion2)+"/gaucherouge.png"
			aviondroite3 = "avion/avion"+str(typeavion)+"/droitevert.png"
			aviongauche3 = "avion/avion"+str(typeavion)+"/gauchevert.png"
		if nombrejoueurs==3:
			aviondroite = "avion/avion"+str(typeavion)+"/droitebleu.png"
			aviongauche = "avion/avion"+str(typeavion)+"/gauchebleu.png"
			aviondroite2 = "avion/avion"+str(typeavion2)+"/droiterouge.png"
			aviongauche2 = "avion/avion"+str(typeavion2)+"/gaucherouge.png"
			aviondroite3 = "avion/avion"+str(typeavion)+"/droitevert.png"
			aviongauche3 = "avion/avion"+str(typeavion)+"/gauchevert.png"
				
		#musique.play()
		
		#IV - 2 : On affiche les variables qui seront utiles plus tard
		#ANNONCE DES VARIABLES DES DEPLACEMENTS DES OBSTACLES
		mouvx1=0
		mouvx2=0
		mouvy1=0
		mouvy2=0
			
		#Annonce des variables retour des obstacles
		mouvx1retour=0
		mouvx2retour=0
		mouvy1retour=0
		mouvy2retour=0
			
		partie=1
		niveau=0
		explosion=0
		
		#Vitesse des avions
		droiteapp1=0
		gaucheapp1=0
		droiteapp2=0
		gaucheapp2=0
		droiteapp3=0
		gaucheapp3=0
		
		
		#V - On va commencer a mettre en marche le niveau, cette boucle toujours pendant le jeu
		while partie:
			#V - 1 : On commence par creer les differents types de mouvement possibles
			#Mouvementy1 : L'obstacle descend puis monte
			if mouvy1retour:
				mouvy1-=2
				if mouvy1<0:
					mouvy1retour=0
			else:
				mouvy1+=2
				if mouvy1>300:
					mouvy1retour=1
					
			#Mouvementy2 : L'obstacle monte puis descend
			if mouvy2retour:
				mouvy2-=2
				if mouvy2<-300:
					mouvy2retour=0
			else:
				mouvy2+=2
				if mouvy2>0:
					mouvy2retour=1
			#Mouvementx1 : L'obstacle va a droite puis a gauche
			if mouvx1retour:
				mouvx1-=2
				if mouvx1<0:
					mouvx1retour=0
			else:
				mouvx1+=2
				if mouvx1>300:
					mouvx1retour=1
			#Mouvementx2: L'obstacle va a gauche puis a droite
			if mouvx2retour:
				mouvx2-=2
				if mouvx2<-300:
					mouvx2retour=0
			else:
				mouvx2+=2
				if mouvx2>0:
					mouvx2retour=1
			#Obstacle 5
			
				
			#LA LISTE DES EXPLOSIONS :		
			if explosion>0:
				#V - 2 : On fait exploser l'avion seulement si explosion vaut 1
				if explosion==1:
					#musique.stop()
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					pygame.display.update()
					musique = pygame.mixer.Sound("menu/bruit.wav")
					musique.play()
					pygame.time.wait(200)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion2.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion3.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion4.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion5.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion6.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					pygame.display.update()
					pygame.time.wait(100)
					musique.stop()
					
					jeu=0
					partie=0
					accueil=1
					defilement_x0=0
					defilement_x1=0
					defilement_x2=0
					defilement_x3=0
					defilement_y0=0
					defilement_y1=0
					defilement_y2=0
					defilement_y3=0
				
				
				#V - 3 : Pareil qu'avant mais pour le joueur 2
				if explosion==2:
					#musique.stop()
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					pygame.display.update()
					musique = pygame.mixer.Sound("menu/bruit.wav")
					musique.play()
					pygame.time.wait(200)
					
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion2.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion3.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion4.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion5.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion6.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					pygame.display.update()
					pygame.time.wait(100)
					musique.stop()
					
					jeu=0
					partie=0
					accueil=1
					defilement_x0=0
					defilement_x1=0
					defilement_x2=0
					defilement_x3=0
					defilement_y0=0
					defilement_y1=0
					defilement_y2=0
					defilement_y3=0
					
				if explosion==3:
					#musique.stop()
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					musique = pygame.mixer.Sound("menu/bruit.wav")
					musique.play()
					pygame.time.wait(200)
					
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion2.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion3.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion4.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion5.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion6.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					musique.stop()
					
					jeu=0
					partie=0
					accueil=1
					defilement_x0=0
					defilement_x1=0
					defilement_x2=0
					defilement_x3=0
					defilement_y0=0
					defilement_y1=0
					defilement_y2=0
					defilement_y3=0
					
				if explosion==4:
					#musique.stop()
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					pygame.display.update()
					musique = pygame.mixer.Sound("menu/bruit.wav")
					musique.play()
					pygame.time.wait(200)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion2.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion2.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion3.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion3.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion4.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion4.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion5.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion5.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion6.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion6.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					pygame.display.update()
					pygame.time.wait(100)
					musique.stop()
					
					jeu=0
					partie=0
					accueil=1
					defilement_x0=0
					defilement_x1=0
					defilement_x2=0
					defilement_x3=0
					defilement_y0=0
					defilement_y1=0
					defilement_y2=0
					defilement_y3=0
					
				if explosion==5:
					#musique.stop()
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					musique = pygame.mixer.Sound("menu/bruit.wav")
					musique.play()
					pygame.time.wait(200)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion2.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion2.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion3.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion3.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion4.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion4.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion5.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion5.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion=pygame.image.load("avion/avion"+str(typeavion)+"/explosion6.png").convert()
					fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion6.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					musique.stop()
					
					jeu=0
					partie=0
					accueil=1
					defilement_x0=0
					defilement_x1=0
					defilement_x2=0
					defilement_x3=0
					defilement_y0=0
					defilement_y1=0
					defilement_y2=0
					defilement_y3=0
					
				if explosion==6:
					#musique.stop()
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					musique = pygame.mixer.Sound("menu/bruit.wav")
					musique.play()
					pygame.time.wait(200)
					
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion2.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion2.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion3.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion3.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion4.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion4.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion5.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion5.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					
					avion2=pygame.image.load("avion/avion"+str(typeavion)+"/explosion6.png").convert()
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					avion3=pygame.image.load("avion/avion"+str(typeavion)+"/explosion6.png").convert()
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
					pygame.display.update()
					pygame.time.wait(100)
					musique.stop()
					
					jeu=0
					partie=0
					accueil=1
					defilement_x0=0
					defilement_x1=0
					defilement_x2=0
					defilement_x3=0
					defilement_y0=0
					defilement_y1=0
					defilement_y2=0
					defilement_y3=0
				
			#V - 4 : S'il n'y a pas d'explosion, on continue la partie !
			
			#VI - Les differentes notions durant le jeu quand l'avion n'explose pas !
			#VI - 1 : Le temps, chaque tour boucle vaut 1 temps, il existe 6 temps differents. Cela sert pour les mouvements d'obstacles
			
			if explosion==0:
				if temps>0:
					if tempsretour:
						if temps!=1:
							temps-=1
						else:
							tempsretour=0
							temps=2
						
					else:
						if temps!=6:
							temps+=1
						else:
							tempsretour=1
							temps=5
						
				#VI - Les fameux deplacements de l'avion, enfin !	
				#LISTE DES DEPLACEMENTS DE L'AVION !!!!!!!!!
				
				#VI - 1 : Les directions, ici on definit si l'avion regarde vers la droite ou la gauche
				if direction=="droite":
					avion=pygame.image.load(aviondroite).convert()
				if direction=="gauche":
					avion=pygame.image.load(aviongauche).convert()
				if direction2=="droite":
					avion2=pygame.image.load(aviondroite2).convert()
				if direction2=="gauche":
					avion2=pygame.image.load(aviongauche2).convert()
				if direction3=="droite":
					avion3=pygame.image.load(aviondroite3).convert()
				if direction3=="gauche":
					avion3=pygame.image.load(aviongauche3).convert()
					
				#VI - 2 : Les deplacements avec les touches
				for event in pygame.event.get():
					if event.type == QUIT:
						continuer=0
						partie=0
						jeu=0
				touches=pygame.key.get_pressed()
				if vitesse:
					avion_x+=3
					direction="droite"
					avion_x2+=3
					direction2="droite"
					avion_x3+=3
					direction3="droite"
					
				#VI - 3 : Toutes les touches de l'avion du joueur 1 !
				if droiteapp1<0:
					droiteapp1=0
				if gaucheapp1<0:
					gaucheapp1=0
				if touches[pygame.K_RIGHT]==0 and touches[pygame.K_LEFT]==0 and touches[pygame.K_UP]==0 and touches[pygame.K_DOWN]==0:
					if gravite==0:
						avion_y+=1
						if lourd:
							avion_y+=1
					if droiteapp1>0:
						droiteapp1-=2
					if gaucheapp1>0:
						gaucheapp1-=2
				if touches[pygame.K_RIGHT]==0 and touches[pygame.K_LEFT]==0 and touches[pygame.K_UP]==0 and touches[pygame.K_DOWN]==1:
					if tordu==0:
						avion_y+=2
					if tordu:
						avion_y-=2
						if vertigineux:
							avion_y-=2
					if droiteapp1>0:
						droiteapp1-=2
					if gaucheapp1>0:
						gaucheapp1-=2
				if touches[pygame.K_RIGHT]==0 and touches[pygame.K_LEFT]==0 and touches[pygame.K_UP]==1 and touches[pygame.K_DOWN]==0:
					if tordu==0:
						avion_y-=2
						if vertigineux:
							avion_y-=2
					if tordu:
						avion_y+=2
					if droiteapp1>0:
						droiteapp1-=2
					if gaucheapp1>0:
						gaucheapp1-=2
				if touches[pygame.K_RIGHT]==0 and touches[pygame.K_LEFT]==0 and touches[pygame.K_UP]==1 and touches[pygame.K_DOWN]==1:
					avion_y+=1
					if droiteapp1>0:
						droiteapp1-=2
					if gaucheapp1>0:
						gaucheapp1-=2
				if touches[pygame.K_RIGHT]==1 and touches[pygame.K_LEFT]==0 and touches[pygame.K_UP]==0 and touches[pygame.K_DOWN]==0:
					avion_x+=2
					if chasse:
						avion_x+=1
					droiteapp1+=1
					direction="droite"
					if gaucheapp1>0:
						gaucheapp1-=5
				if touches[pygame.K_RIGHT]==0 and touches[pygame.K_LEFT]==1 and touches[pygame.K_UP]==0 and touches[pygame.K_DOWN]==0:
					avion_x-=2
					if chasse:
						avion_x-=1
					gaucheapp1+=1
					if droiteapp1>0:
						droiteapp1-=5
					direction="gauche"
				if touches[pygame.K_RIGHT]==1 and touches[pygame.K_LEFT]==0 and touches[pygame.K_UP]==1 and touches[pygame.K_DOWN]==0:
					avion_x+=2
					if tordu==0:
						avion_y-=2
						if chasse:
							avion_x+=1
					if tordu:
						avion_y+=2
						if chasse:
							avion_x+=3
					if gaucheapp1>0:
						gaucheapp1-=5
					direction="droite"
				if touches[pygame.K_RIGHT]==1 and touches[pygame.K_LEFT]==0 and touches[pygame.K_UP]==0 and touches[pygame.K_DOWN]==1:
					avion_x+=2
					if tordu==0:
						avion_y+=2
						if chasse:
							avion_x+=3
					if tordu:
						avion_y-=2
						if chasse:
							avion_x+=1
					droiteapp1+=2
					direction="droite"
					if gaucheapp1>0:
						gaucheapp1-=5
				if touches[pygame.K_RIGHT]==0 and touches[pygame.K_LEFT]==1 and touches[pygame.K_UP]==1 and touches[pygame.K_DOWN]==0:
					avion_x-=2
					if tordu==0:
						avion_y-=2
						if chasse:
							avion_x-=1
					if tordu:
						avion_y+=2
						if chasse:
							avion_x-=3
					if droiteapp1>0:
						droiteapp1-=5
					direction="gauche"
				if touches[pygame.K_RIGHT]==0 and touches[pygame.K_LEFT]==1 and touches[pygame.K_UP]==0 and touches[pygame.K_DOWN]==1:
					avion_x-=2
					if tordu==0:
						avion_y+=2
						if chasse:
							avion_x-=3
					if tordu:
						avion_y-=2
						if chasse:
							avion_x-=1
					gaucheapp1+=2
					direction="gauche"
				if touches[pygame.K_RIGHT]==1 and touches[pygame.K_LEFT]==1:
					avion_x-=1
					direction="droite"
				if droiteapp1>10:
					avion_x+=1
					if chasse:
						avion_x+=1
				if droiteapp1>30:
					avion_x+=1
					if chasse:
						avion_x+=1
				if droiteapp1>50:
					avion_x+=1
					if chasse:
						avion_x+=1
				if droiteapp1>100:
					avion_x+=1
					if chasse:
						avion_x+=1
				if droiteapp1>200:
					avion_x+=1
					if chasse:
						avion_x+=1
				if droiteapp1>300:
					avion_x+=1
					if chasse:
						avion_x+=1
				if droiteapp1>500:
					avion_x+=1
					if chasse:
						avion_x+=1
				if droiteapp1>1000:
					avion_x+=1
					if chasse:
						avion_x+=1
				if droiteapp1>2000:
					if chasse:
						avion_x-=2
					
				if gaucheapp1>10:
					avion_x-=1
					if chasse:
						avion_x-=1
				if gaucheapp1>30:
					avion_x-=1
					if chasse:
						avion_x-=1
				if gaucheapp1>50:
					avion_x-=1
					if chasse:
						avion_x-=1
				if gaucheapp1>100:
					avion_x-=1
					if chasse:
						avion_x-=1
				if gaucheapp1>200:
					avion_x-=1
					if chasse:
						avion_x-=1
				if gaucheapp1>300:
					avion_x-=1
					if chasse:
						avion_x-=1
				if gaucheapp1>500:
					avion_x-=1
					if chasse:
						avion_x-=1
				if gaucheapp1>1000:
					avion_x-=1
					if chasse:
						avion_x-=1
				if gaucheapp1>2000:
					if chasse:
						avion_x-=2
				#VI - 4 : Les limites de l'avion du joueur 1
				if avion_x<0:
					avion_x=0
				if avion_y<0:
					avion_y=0
				if avion_y>430:
					if ciel:
						if avion_y>460:
							avion_y=460
					if terre:
						avion_y=430
						if roulant==0:
							explosion=1
					if mer:
						avion_y=430
						if hydravion==0:
							explosion=1
				if avion_x>6000-40:
					avion_x=6000-40
					fond = pygame.image.load("menu/gagner.png").convert()
					fenetre.blit(fond, (0,0))
					pygame.display.flip()
					pygame.time.wait(2000)
					jeu=0
					partie=0
					accueil=1
					explosion=0
					pygame.mixer.stop()
					
				elif avion_x>300:
					defilement_x0=(avion_x-300)*2
					defilement_x1=avion_x-300
					defilement_x2=(avion_x-300)/2
					defilement_x3=(avion_x-300)/3
					if defilement_x1>6000-640:
						defilement_x1=6000-640
						defilement_x2=(defilement_x1)/2
						defilement_x3=(defilement_x1)/3
						defilement_x0=(defilement_x1)*2
				elif avion_x<300:
					defilement_x0=0#(avion_x-640)*2
					defilement_x1=0#(avion_x-640)
					defilement_x2=0#(avion_x-640)/2
					defilement_x3=0#(avion_x-640)/3
					
					
				#VI - 5 : Toutes les touches de l'avion du joueur 2
					
				if nombrejoueurs>1:	
					if droiteapp2<0:
						droiteapp2=0
					if gaucheapp2<0:
						gaucheapp2=0
					if touches[pygame.K_d]==0 and touches[pygame.K_a]==0 and touches[pygame.K_w]==0 and touches[pygame.K_s]==0:
						if gravite==0:
							avion_y2+=1
							if lourd2:
								avion_y2+=1
						if droiteapp2>0:
							droiteapp2-=2
						if gaucheapp2>0:
							gaucheapp2-=2
					if touches[pygame.K_d]==0 and touches[pygame.K_a]==0 and touches[pygame.K_w]==0 and touches[pygame.K_s]==1:
						if tordu2==0:
							avion_y2+=2
						if tordu2:
							avion_y2-=2
							if vertigineux2:
								avion_y2-=2
						if droiteapp2>0:
							droiteapp2-=2
						if gaucheapp2>0:
							gaucheapp2-=2
					if touches[pygame.K_d]==0 and touches[pygame.K_a]==0 and touches[pygame.K_w]==1 and touches[pygame.K_s]==0:
						if tordu2==0:
							avion_y2-=2
							if vertigineux2:
								avion_y2-=2
						if tordu2:
							avion_y2+=2
						if droiteapp2>0:
							droiteapp2-=2
						if gaucheapp2>0:
							gaucheapp2-=2
					if touches[pygame.K_d]==0 and touches[pygame.K_a]==0 and touches[pygame.K_w]==1 and touches[pygame.K_s]==1:
						avion_y2+=1
						if droiteapp2>0:
							droiteapp2-=2
						if gaucheapp2>0:
							gaucheapp2-=2
					if touches[pygame.K_d]==1 and touches[pygame.K_a]==0 and touches[pygame.K_w]==0 and touches[pygame.K_s]==0:
						avion_x2+=2
						if chasse2:
							avion_x2+=1
						droiteapp2+=1
						direction2="droite"
						if gaucheapp2>0:
							gaucheapp2-=5
					if touches[pygame.K_d]==0 and touches[pygame.K_a]==1 and touches[pygame.K_w]==0 and touches[pygame.K_s]==0:
						avion_x2-=2
						if chasse2:
							avion_x2-=1
						gaucheapp2+=1
						if droiteapp2>0:
							droiteapp2-=5
						direction2="gauche"
					if touches[pygame.K_d]==1 and touches[pygame.K_a]==0 and touches[pygame.K_w]==1 and touches[pygame.K_s]==0:
						avion_x2+=2
						if tordu2==0:
							avion_y2-=2
							if chasse2:
								avion_x2+=1
						if tordu2:
							avion_y2+=2
							if chasse2:
								avion_x2+=3
						if gaucheapp2>0:
							gaucheapp2-=5
						direction2="droite"
					if touches[pygame.K_d]==1 and touches[pygame.K_a]==0 and touches[pygame.K_w]==0 and touches[pygame.K_s]==1:
						avion_x2+=2
						if tordu2==0:
							avion_y2+=2
							if chasse2:
								avion_x2+=3
						if tordu2:
							avion_y2-=2
							if chasse2:
								avion_x2+=1
						droiteapp2+=2
						direction2="droite"
						if gaucheapp2>0:
							gaucheapp2-=5
					if touches[pygame.K_d]==0 and touches[pygame.K_a]==1 and touches[pygame.K_w]==1 and touches[pygame.K_s]==0:
						avion_x2-=2
						if tordu2==0:
							avion_y2-=2
							if chasse2:
								avion_x2-=1
						if tordu2:
							avion_y2+=2
							if chasse2:
								avion_x2-=3
						if droiteapp2>0:
							droiteapp2-=5
						direction2="gauche"
					if touches[pygame.K_d]==0 and touches[pygame.K_a]==1 and touches[pygame.K_w]==0 and touches[pygame.K_s]==1:
						avion_x2-=2
						if tordu2==0:
							avion_y2+=2
							if chasse2:
								avion_x2-=3
						if tordu2:
							avion_y2-=2
							if chasse2:
								avion_x2-=1
						gaucheapp2+=2
						direction2="gauche"
					if touches[pygame.K_d]==1 and touches[pygame.K_a]==1:
						avion_x2-=1
						direction2="droite"
					if droiteapp2>10:
						avion_x2+=1
						if chasse2:
							avion_x2+=1
					if droiteapp2>30:
						avion_x2+=1
						if chasse2:
							avion_x2+=1
					if droiteapp2>50:
						avion_x2+=1
						if chasse2:
							avion_x2+=1
					if droiteapp2>100:
						avion_x2+=1
						if chasse2:
							avion_x2+=1
					if droiteapp2>200:
						avion_x2+=1
						if chasse2:
							avion_x2+=1
					if droiteapp2>300:
						avion_x2+=1
						if chasse2:
							avion_x2+=1
					if droiteapp2>500:
						avion_x2+=1
						if chasse2:
							avion_x2+=1
					if droiteapp2>1000:
						avion_x2+=1
						if chasse2:
							avion_x2+=1
					if droiteapp2>2000:
						if chasse2:
							avion_x2-=2
						
					if gaucheapp2>10:
						avion_x2-=1
						if chasse2:
							avion_x2-=1
					if gaucheapp2>30:
						avion_x2-=1
						if chasse2:
							avion_x2-=1
					if gaucheapp2>50:
						avion_x2-=1
						if chasse2:
							avion_x2-=1
					if gaucheapp2>100:
						avion_x2-=1
						if chasse2:
							avion_x2-=1
					if gaucheapp2>200:
						avion_x2-=1
						if chasse2:
							avion_x2-=1
					if gaucheapp2>300:
						avion_x2-=1
						if chasse2:
							avion_x2-=1
					if gaucheapp2>500:
						avion_x2-=1
						if chasse2:
							avion_x2-=1
					if gaucheapp2>1000:
						avion_x2-=1
						if chasse2:
							avion_x2-=1
					if gaucheapp2>2000:
						if chasse2:
							avion_x2-=2
					
					#VI - 6 : Les limites de l'avion du joueur 2
					if avion_x2<0:
						avion_x2=0
					if avion_y2<0:
						avion_y2=0
					if avion_y2>430:
						if ciel:
							if avion_y2>460:
								avion_y2=460
						if terre:
							avion_y2=430
							if roulant2==0:
								if nombrejoueurs==2:
									explosion=2
						if mer:
							avion_y2=430
							if hydravion2==0:
								if nombrejoueurs==2:
									explosion=2
					if avion_x2>6000-40:
						avion_x2=6000-40
						fond = pygame.image.load("menu/gagner.png").convert()
						fenetre.blit(fond, (0,0))
						pygame.display.flip()
						pygame.time.wait(2000)
						jeu=0
						partie=0
						accueil=1
						explosion=0
						pygame.mixer.stop()
					
					
					if nombrejoueurs>2:	
						if droiteapp3<0:
							droiteapp3=0
						if gaucheapp3<0:
							gaucheapp3=0
						if touches[pygame.K_h]==0 and touches[pygame.K_f]==0 and touches[pygame.K_t]==0 and touches[pygame.K_g]==0:
							if gravite==0:
								avion_y3+=1
								if lourd3:
									avion_y3+=1
							if droiteapp3>0:
								droiteapp3-=2
							if gaucheapp3>0:
								gaucheapp3-=2
						if touches[pygame.K_h]==0 and touches[pygame.K_f]==0 and touches[pygame.K_t]==0 and touches[pygame.K_g]==1:
							if tordu3==0:
								avion_y3+=2
							if tordu3:
								avion_y3-=2
								if vertigineux3:
									avion_y3-=2
							if droiteapp3>0:
								droiteapp3-=2
							if gaucheapp3>0:
								gaucheapp3-=2
						if touches[pygame.K_h]==0 and touches[pygame.K_f]==0 and touches[pygame.K_t]==1 and touches[pygame.K_g]==0:
							if tordu3==0:
								avion_y3-=2
								if vertigineux3:
									avion_y3-=2
							if tordu3:
								avion_y3+=2
							if droiteapp3>0:
								droiteapp3-=2
							if gaucheapp3>0:
								gaucheapp3-=2
						if touches[pygame.K_h]==0 and touches[pygame.K_f]==0 and touches[pygame.K_t]==1 and touches[pygame.K_g]==1:
							avion_y3+=1
							if droiteapp3>0:
								droiteapp3-=2
							if gaucheapp3>0:
								gaucheapp3-=2
						if touches[pygame.K_h]==1 and touches[pygame.K_f]==0 and touches[pygame.K_t]==0 and touches[pygame.K_g]==0:
							avion_x3+=2
							if chasse3:
								avion_x3+=1
							droiteapp3+=1
							direction3="droite"
							if gaucheapp3>0:
								gaucheapp3-=5
						if touches[pygame.K_h]==0 and touches[pygame.K_f]==1 and touches[pygame.K_t]==0 and touches[pygame.K_g]==0:
							avion_x3-=2
							if chasse3:
								avion_x3-=1
							gaucheapp3+=1
							if droiteapp3>0:
								droiteapp3-=5
							direction3="gauche"
						if touches[pygame.K_h]==1 and touches[pygame.K_f]==0 and touches[pygame.K_t]==1 and touches[pygame.K_g]==0:
							avion_x3+=2
							if tordu3==0:
								avion_y3-=2
								if chasse3:
									avion_x3+=1
							if tordu3:
								avion_y3+=2
								if chasse3:
									avion_x3+=3
							if gaucheapp3>0:
								gaucheapp3-=5
							direction3="droite"
						if touches[pygame.K_h]==1 and touches[pygame.K_f]==0 and touches[pygame.K_t]==0 and touches[pygame.K_g]==1:
							avion_x3+=2
							if tordu3==0:
								avion_y3+=2
								if chasse3:
									avion_x3+=3
							if tordu3:
								avion_y3-=2
								if chasse3:
									avion_x3+=1
							droiteapp3+=2
							direction3="droite"
							if gaucheapp3>0:
								gaucheapp3-=5
						if touches[pygame.K_h]==0 and touches[pygame.K_f]==1 and touches[pygame.K_t]==1 and touches[pygame.K_g]==0:
							avion_x3-=2
							if tordu3==0:
								avion_y3-=2
								if chasse3:
									avion_x3-=1
							if tordu3:
								avion_y3+=2
								if chasse3:
									avion_x3-=3
							if droiteapp3>0:
								droiteapp3-=5
							direction3="gauche"
						if touches[pygame.K_h]==0 and touches[pygame.K_f]==1 and touches[pygame.K_t]==0 and touches[pygame.K_g]==1:
							avion_x3-=2
							if tordu3==0:
								avion_y3+=2
								if chasse3:
									avion_x3-=3
							if tordu3:
								avion_y3-=2
								if chasse3:
									avion_x3-=1
							gaucheapp3+=2
							direction3="gauche"
						if touches[pygame.K_h]==1 and touches[pygame.K_f]==1:
							avion_x3-=1
							direction3="droite"
						if droiteapp3>10:
							avion_x3+=1
							if chasse3:
								avion_x3+=1
						if droiteapp3>30:
							avion_x3+=1
							if chasse3:
								avion_x3+=1
						if droiteapp3>50:
							avion_x3+=1
							if chasse3:
								avion_x3+=1
						if droiteapp3>100:
							avion_x3+=1
							if chasse3:
								avion_x3+=1
						if droiteapp3>200:
							avion_x3+=1
							if chasse3:
								avion_x3+=1
						if droiteapp3>300:
							avion_x3+=1
							if chasse3:
								avion_x3+=1
						if droiteapp3>500:
							avion_x3+=1
							if chasse3:
								avion_x3+=1
						if droiteapp3>1000:
							avion_x3+=1
							if chasse3:
								avion_x3+=1
						if droiteapp3>2000:
							if chasse3:
								avion_x3-=2
							
						if gaucheapp3>10:
							avion_x3-=1
							if chasse3:
								avion_x3-=1
						if gaucheapp3>30:
							avion_x3-=1
							if chasse3:
								avion_x3-=1
						if gaucheapp3>50:
							avion_x3-=1
							if chasse3:
								avion_x3-=1
						if gaucheapp3>100:
							avion_x3-=1
							if chasse3:
								avion_x3-=1
						if gaucheapp3>200:
							avion_x3-=1
							if chasse3:
								avion_x3-=1
						if gaucheapp3>300:
							avion_x3-=1
							if chasse3:
								avion_x3-=1
						if gaucheapp3>500:
							avion_x3-=1
							if chasse3:
								avion_x3-=1
						if gaucheapp3>1000:
							avion_x3-=1
							if chasse3:
								avion_x3-=1
						if gaucheapp3>2000:
							if chasse3:
								avion_x3-=2
						
						#VI - 6 : Les limites de l'avion du joueur 3
						if avion_x3<0:
							avion_x3=0
						if avion_y3<0:
							avion_y3=0
						if avion_y3>430:
							if ciel:
								if avion_y3>460:
									avion_y3=460
							if terre:
								avion_y3=430
								if roulant3==0:
									if nombrejoueurs==3:
										explosion=3
							if mer:
								avion_y3=430
								if hydravion3==0:
									if nombrejoueurs==3:
										explosion=3
						if avion_x3>6000-40:
							avion_x3=6000-40
							fond = pygame.image.load("menu/gagner.png").convert()
							fenetre.blit(fond, (0,0))
							pygame.display.flip()
							pygame.time.wait(2000)
							jeu=0
							partie=0
							accueil=1
							explosion=0
							pygame.mixer.stop()	
				
					
					

					
				
					
				#VI - 7 : Pour quitter le niveau, la touche ECHAP	
				if touches[pygame.K_ESCAPE]==1:
					jeu=0
					partie=0
					accueil=1
					explosion=0
					pygame.mixer.stop()
					
				#VII - Les differentes fonctionnalites d'affichage
				#VII - 1 : On affiche les fonds et les avions, enfin ! Ce ne qye maintenant que les fonds vont apparaitre a l'ecran
				fenetre.blit(fond3,[0,0],[defilement_x3,0,640,480])
				fenetre.blit(fond2,[0,0],[defilement_x2,0,640,480])
				fenetre.blit(fond1,[0,0],[defilement_x1,0,640,480])
				fenetre.blit(avion, (avion_x-defilement_x1,avion_y))
				if nombrejoueurs==2:
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
				if nombrejoueurs==3:
					fenetre.blit(avion2, (avion_x2-defilement_x1,avion_y2))
					fenetre.blit(avion3, (avion_x3-defilement_x1,avion_y3))
				if avion_x <1000:
					zonemine=1
				elif avion_x >=1000 and avion_x <2000:
					zonemine=2
				elif avion_x >=2000 and avion_x <3000:
					zonemine=3
				elif avion_x >=3000 and avion_x <4000:
					zonemine=4
				elif avion_x >=4000 and avion_x <5000:
					zonemine=5
				elif avion_x >=5000 and avion_x <6000:
					zonemine=6
				#Liste des obstacles
				#VII - 2 : Ensuite, c'est l'heure tous les obstacles
				with open("niveaux/niv"+str(menufleche)+"/mines/mines"+str(zonemine)+".txt", "r") as fichier:
					for ligne in fichier:
						minex=""
						miney=""
						deplacementx=""
						deplacementy=""
						mouvx=0
						mouvy=0
						forinmine=0
						numeromine=""
						for numero in ligne :
							if numero =="a":
								forinmine+=1
							if forinmine==0 and numero!="a":
								minex = minex+numero
							if forinmine==1 and numero!="a":
								miney = miney+numero
							if forinmine==2 and numero!="a":
								deplacementx=deplacementx+numero
							if forinmine==3 and numero!="a":
								deplacementy=deplacementy+numero
							if forinmine==4 and numero!="a":
								numeromine=numeromine+numero
								if deplacementx=="0":
									mouvx=0
								if deplacementx=="1":
									mouvx=mouvx1
								if deplacementx=="2":
									mouvx=mouvx2
								if deplacementy=="0":
									mouvy=0
								if deplacementy=="1":
									mouvy=mouvy1
								if deplacementy=="2":
									mouvy=mouvy2
						obstacle=pygame.image.load("mines/mine"+numeromine+"/mine"+str(temps)+".png").convert()
						with open("mines/mine"+numeromine+"/taille.txt", "r") as fichiertaille:
							for lignetaille in fichiertaille:
								tailley=""
								taillex=""
								forintaille=0
								for codetaille in lignetaille:
									if codetaille =="a":
										forintaille+=1
									if forintaille==0 and codetaille!="a":
										taillex=taillex+codetaille
									if forintaille==1 and codetaille!="a":
										tailley=tailley+codetaille
						fenetre.blit(obstacle,(-defilement_x1+int(minex)+mouvx, int(miney)+mouvy))
						if avion_x<int(minex)+int(taillex)+mouvx and avion_x>int(minex)-35+mouvx and avion_y<int(miney)+int(tailley)+mouvy and avion_y>int(miney)-20+mouvy:
							explosion=1
						if nombrejoueurs>1:
							if avion_x2<int(minex)+20+mouvx and avion_x2>int(minex)-35+mouvx and avion_y2<int(miney)+20+mouvy and avion_y2>int(miney)-20+mouvy:
								explosion=2
							if nombrejoueurs==3:
								if avion_x3<int(minex)+20+mouvx and avion_x3>int(minex)-35+mouvx and avion_y3<int(miney)+20+mouvy and avion_y3>int(miney)-20+mouvy:
									explosion=3	
						
				with open("niveaux/niv"+str(menufleche)+"/mines/mines"+str(zonemine-1)+".txt", "r") as fichier:
					for ligne in fichier:
						minex=""
						miney=""
						deplacementx=""
						deplacementy=""
						mouvx=0
						mouvy=0
						forinmine=0
						numeromine=""
						for numero in ligne :
							if numero =="a":
								forinmine+=1
							if forinmine==0 and numero!="a":
								minex = minex+numero
							if forinmine==1 and numero!="a":
								miney = miney+numero
							if forinmine==2 and numero!="a":
								deplacementx=deplacementx+numero
							if forinmine==3 and numero!="a":
								deplacementy=deplacementy+numero
							if forinmine==4 and numero!="a":
								numeromine=numeromine+numero
								if deplacementx=="0":
									mouvx=0
								if deplacementx=="1":
									mouvx=mouvx1
								if deplacementx=="2":
									mouvx=mouvx2
								if deplacementy=="0":
									mouvy=0
								if deplacementy=="1":
									mouvy=mouvy1
								if deplacementy=="2":
									mouvy=mouvy2
						obstacle=pygame.image.load("mines/mine"+numeromine+"/mine"+str(temps)+".png").convert()
						with open("mines/mine"+numeromine+"/taille.txt", "r") as fichiertaille:
							for lignetaille in fichiertaille:
								tailley=""
								taillex=""
								forintaille=0
								for codetaille in lignetaille:
									if codetaille =="a":
										forintaille+=1
									if forintaille==0 and codetaille!="a":
										taillex=taillex+codetaille
									if forintaille==1 and codetaille!="a":
										tailley=tailley+codetaille
						fenetre.blit(obstacle,(-defilement_x1+int(minex)+mouvx, int(miney)+mouvy))
						if avion_x<int(minex)+int(taillex)+mouvx and avion_x>int(minex)-35+mouvx and avion_y<int(miney)+int(tailley)+mouvy and avion_y>int(miney)-20+mouvy:
							explosion=1
						if nombrejoueurs>1:
							if avion_x2<int(minex)+20+mouvx and avion_x2>int(minex)-35+mouvx and avion_y2<int(miney)+20+mouvy and avion_y2>int(miney)-20+mouvy:
								explosion=2
							if nombrejoueurs==3:
								if avion_x3<int(minex)+20+mouvx and avion_x3>int(minex)-35+mouvx and avion_y3<int(miney)+20+mouvy and avion_y3>int(miney)-20+mouvy:
									explosion=3
							
						
						
				with open("niveaux/niv"+str(menufleche)+"/mines/mines"+str(zonemine+1)+".txt", "r") as fichier:
					for ligne in fichier:
						minex=""
						miney=""
						deplacementx=""
						deplacementy=""
						mouvx=0
						mouvy=0
						forinmine=0
						numeromine=""
						for numero in ligne :
							if numero =="a":
								forinmine+=1
							if forinmine==0 and numero!="a":
								minex = minex+numero
							if forinmine==1 and numero!="a":
								miney = miney+numero
							if forinmine==2 and numero!="a":
								deplacementx=deplacementx+numero
							if forinmine==3 and numero!="a":
								deplacementy=deplacementy+numero
							if forinmine==4 and numero!="a":
								numeromine=numeromine+numero
								if deplacementx=="0":
									mouvx=0
								if deplacementx=="1":
									mouvx=mouvx1
								if deplacementx=="2":
									mouvx=mouvx2
								if deplacementy=="0":
									mouvy=0
								if deplacementy=="1":
									mouvy=mouvy1
								if deplacementy=="2":
									mouvy=mouvy2
						obstacle=pygame.image.load("mines/mine"+numeromine+"/mine"+str(temps)+".png").convert()
						with open("mines/mine"+numeromine+"/taille.txt", "r") as fichiertaille:
							for lignetaille in fichiertaille:
								tailley=""
								taillex=""
								forintaille=0
								for codetaille in lignetaille:
									if codetaille =="a":
										forintaille+=1
									if forintaille==0 and codetaille!="a":
										taillex=taillex+codetaille
									if forintaille==1 and codetaille!="a":
										tailley=tailley+codetaille
						fenetre.blit(obstacle,(-defilement_x1+int(minex)+mouvx, int(miney)+mouvy))
						#VII - 3 : En plus de l'afficher, on dit si l'avion est dans la zone qu'il explose
						if avion_x<int(minex)+int(taillex)+mouvx and avion_x>int(minex)-35+mouvx and avion_y<int(miney)+int(tailley)+mouvy and avion_y>int(miney)-20+mouvy:
							explosion=1
						if nombrejoueurs>1:
							if avion_x2<int(minex)+20+mouvx and avion_x2>int(minex)-35+mouvx and avion_y2<int(miney)+20+mouvy and avion_y2>int(miney)-20+mouvy:
								explosion=2
							if nombrejoueurs==3:
								if avion_x3<int(minex)+20+mouvx and avion_x3>int(minex)-35+mouvx and avion_y3<int(miney)+20+mouvy and avion_y3>int(miney)-20+mouvy:
									explosion=3
				#if avion_x2<avion_x+1 and avion_x2>avion_x-40:#and avion_y2<avion_y+40 and avion_y2>avion_y-40:
								#explosion=2
				if nombrejoueurs==2:
					if avion_x<avion_x2+40 and avion_x>avion_x2-35 and avion_y<avion_y2+20 and avion_y>avion_y2-20:
						explosion=4
				if nombrejoueurs==3:
					if avion_x<avion_x2+40 and avion_x>avion_x2-35 and avion_y<avion_y2+20 and avion_y>avion_y2-20:
						explosion=4
					if avion_x<avion_x3+40 and avion_x>avion_x3-35 and avion_y<avion_y3+20 and avion_y>avion_y3-20:
						explosion=5
					if avion_x2<avion_x3+40 and avion_x2>avion_x3-35 and avion_y2<avion_y3+20 and avion_y2>avion_y3-20:
						explosion=6
				
				#VII - 4 : On affiche le dernier fond, le fond0 qui est par dessus tout le monde
				fenetre.blit(fond0,[0,0],[defilement_x0,0,640,480])
				pygame.display.update()
				horloge.tick(2000)
		