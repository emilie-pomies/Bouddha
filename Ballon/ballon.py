import pygame
import time
from random import * 
import sqlite3

blue = (113,177,227)
white = (255,255,255)

pygame.init()
# Donnees = "C:/Users/epomi/Desktop/Ballon/Donnees.sq3"
# conn = sqlite3.connect(Donnees)
# cur = conn.cursor()


surfaceW = 800
surfaceH = 500
ballonW = 50
ballonH = 66
nuageW = 300
nuageH = 300

surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("Ballon Volant")
horloge = pygame.time.Clock()


img = pygame.image.load("moine.png")
img_nuagehaut = pygame.image.load("nuagehaut.png")
img_nuagebas = pygame.image.load("nuagebas.png")

def rejoueOuQuitte() :
	for event in pygame.event.get ([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
		if event.type == pygame.QUIT :
			pygame.quit()
			quit()
		elif event.type == pygame.KEYUP : 
			continue
		return event.key
	return None


def creaTexteObj(texte, Police):
	texteSurface = Police.render(texte,True,white)
	return texteSurface, texteSurface.get_rect()

def message (texte) :
	GOTexte = pygame.font.Font("Bumper Sticker DEMO.otf", 150)
	petitTexte = pygame.font.Font("Bumper Sticker DEMO.otf", 20)
	petitTexteRect=0.0
	GOTexteRect=0.0

	GOTexteSurface, GOTexteRect = creaTexteObj(texte, GOTexte)
	GOTexteRect.center = int(surfaceW/2), int(((surfaceH/2)-50))
	surface.blit(GOTexteSurface, GOTexteRect)


	petitTexteSurface, petitTexteRect = creaTexteObj("appuyer sur une touche pour continuer" , petitTexte)
	petitTexteRect.center = int(surfaceW/2), int(((surfaceH/2)+50))
	surface.blit(petitTexteSurface, petitTexteRect)

	pygame.display.update()
	time.sleep(2)

	while rejoueOuQuitte() == None : 
		horloge.tick()

	principale()

def score(compte):
	police = pygame.font.Font("Bumper Sticker DEMO.otf", 16)
	texte = police.render("Score : " + str(compte), True, white)
	surface.blit(texte, [10,0]) 

# def Hscore(compte):
# 	police = pygame.font.Font("Bumper Sticker DEMO.otf", 16)
# 	texte = police.render("Meilleur Score : " + str(compte), True, white)
# 	surface.blit(texte, [650,0]) 

def nuage(x_nuage, y_nuage, espace):
	surface.blit(img_nuagebas, (x_nuage,y_nuage))
	surface.blit(img_nuagehaut, (x_nuage,y_nuage+nuageW+espace))

def gameOver(score_actuel): 
	a = list(str(score_actuel))

	# Donnees = "C:/Users/epomi/Desktop/Ballon/Donnees.sq3"
	# conn = sqlite3.connect(Donnees)
	# cur = conn.cursor()
	# cur.execute("SELECT * FROM membres")
	# liste = list(cur)

	# hscore = []
	# for i in range(0, len(liste)):
	# 	hscore += liste[i]


	# if (int(hscore[-1]) < score_actuel) : 
	# 	cur.execute("INSERT INTO membres(score) VALUES (?)", a)
	# 	conn.commit()
	# 	cur.close()
	# 	conn.close()

	message("Perdu")


def ballon (x,y,image):
	surface.blit(image, (x,y))

def principale(): 
	x = 150
	y = 200
	y_mouvement = 0


	x_nuage = surfaceW
	y_nuage = randint(-300,20)
	espace = ballonH*3
	nuage_vitesse = 1
	score_actuel = 0


	game_over = False

	while not game_over :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_UP : 
					y_mouvement = -1

			if event.type == pygame.KEYUP : 
				y_mouvement = 1

		y+= y_mouvement

		surface.fill(blue)
		ballon(x,y,img)

		nuage(x_nuage, y_nuage, espace)

		# score(score_actuel)

		# cur.execute("SELECT * FROM membres")
		# liste = list(cur)

		# hscore = []
		# for i in range (0, len(liste)) : 
		# 	hscore += liste[i]
		# print(hscore)

		# Hscore(hscore[-1])

		x_nuage -= nuage_vitesse

		if y >surfaceH -40 or y < -10 : 
 			gameOver(score_actuel)
 
		# if 3 <= score_actuel < 5 :
		# 	nuage_vitesse = 3
		# 	espace = ballonH * 2.5

		# if 5 <= score_actuel < 8 :
		# 	nuage_vitesse = 5
		# 	espace = ballonH * 2.3

		# if 7 <= score_actuel < 10 :
		# 	nuage_vitesse = 6
		# 	espace = ballonH * 2

		# if 10 <= score_actuel < 15 :
		# 	nuage_vitesse = 7
		# 	espace = ballonH * 1.8



		if x + ballonW > x_nuage +40 : 
			if y < y_nuage + nuageH -50 :
				if x-ballonW < x_nuage + nuageW -20 :
					gameOver(score_actuel)

		if x + ballonW > x_nuage + 40 :
			if y + ballonH > y_nuage + nuageH + espace + 50 :
				if x - ballonW < x_nuage + nuageW - 20 : 
					gameOver(score_actuel)

		if x_nuage < (-1*nuageW) : 
			x_nuage = surfaceW
			y_nuage = randint (-300,20)

		if x_nuage < (x-nuageW) < x_nuage + nuage_vitesse :
			score_actuel +=1

		pygame.display.update() 





principale()
pygame.quit()
quit()

