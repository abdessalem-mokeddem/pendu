import pygame
from random import choice
import random

import string

ecran = pygame 
jeu = True
while jeu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False

pygame.init ()
choix = ["casserole", "cuillere", "patate", "souris"]
solution = random.choice(choix)

solution = "casserole"
tentatives = 7
affichage = ""
lettres_trouvees = ""

for l in solution:
  affichage = affichage + "_ "

print(">> Bienvenue dans le pendu <<")

while tentatives > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")[0:1].lower()

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    tentatives = tentatives - 1
    print("-> Nope\n")
    if tentatives==0:
        print(" ==========Y= ")
    if tentatives<=1:
        print(" ||/       |  ")
    if tentatives<=2:
        print(" ||        0  ")
    if tentatives<=3:
        print(" ||       /|\ ")
    if tentatives<=4:
        print(" ||       /|  ")
    if tentatives<=5:                    
        print("/||           ")
    if tentatives<=6:
        print("==============\n")

  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break
     
print("\n     Fin de la partie     ") 

def afficherRegles (self):
        self.regles = "Le Jeu du Pendu"
        x = 400

        for ligne in self.regles.splitlines():
            texteRegle =self.police.render(ligne,1,(146, 36,131))
            textRect = texteRegle.get_rect()
            textRect.top = x
            textRect.centerx = largeurScreen/2
            self.scr.blit(texteRegle,textRect)
            x = textRect.arial
 
def initialisation(self):
        self.boutons =  [Bouton(( 100, 540, 50, 50),'A'   ),
                            Bouton(( 175, 540, 50, 50),'B'   ),
                            Bouton(( 250, 540, 50, 50),'C'   ),
                            Bouton(( 325, 540, 50, 50),'D'   ),
                            Bouton(( 400, 540, 50, 50),'E'   ),
                            Bouton(( 475, 540, 50, 50),'F'   ),
                            Bouton(( 550, 540, 50, 50),'G'   ),
                            Bouton(( 625, 540, 50, 50),'H'   ),
                            Bouton(( 700, 540, 50, 50),'I'   ),
                            Bouton(( 775, 540, 50, 50),'J'   ),
                            Bouton(( 850, 540, 50, 50),'K'   ),
                            Bouton(( 925, 540, 50, 50),'L'   ),
                            Bouton((1000, 540, 50, 50),'M'   ),
                            Bouton(( 100, 615, 50, 50),'N'   ),
                            Bouton(( 175, 615, 50, 50),'O'   ),
                            Bouton(( 250, 615, 50, 50),'P'   ),
                            Bouton(( 325, 615, 50, 50),'Q'   ),
                            Bouton(( 400, 615, 50, 50),'R'   ),
                            Bouton(( 475, 615, 50, 50),'S'   ),
                            Bouton(( 550, 615, 50, 50),'T'   ),
                            Bouton(( 625, 615, 50, 50),'U'   ),
                            Bouton(( 700, 615, 50, 50),'V'   ),
                            Bouton(( 775, 615, 50, 50),'W'   ),
                            Bouton(( 850, 615, 50, 50),'X'   ),
                            Bouton(( 925, 615, 50, 50),'Y'   ),
                            Bouton((1000, 615, 50, 50),'Z'   )]
 
        self.scr = pygame.display.get_surface()
        pygame.display.update(self.scr.blit(self.clavierA,(100,540)))
 
    
def largeurScreen (): 
    def lire_touche(self,ev):
        if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
            index  = pygame.Rect(ev.pos,(1,1)).collidelist(self.boutons)
            if index > -1:
                bouton = self.boutons[index]
                r = self.scr.blit(self.clavierB,bouton,bouton.move(-100,-540))
                pygame.display.update(r)
                del self.boutons[index]
                return bouton.lettre
 

 
class Bouton(pygame.Rect,object):
    def __init__(self,rect,lettre,flag=0):
        pygame.Rect.__init__(self,rect)
        self.lettre = lettre
        self.flag   = flag



class BoutonDemarrer(object):
    
    def __init__(self):
        self.boutton = pygame.image.load("images/boutonDemarrer.png")
        self.position = (20,20)
        self.rect = self.boutton.get_rect(center =(95,45))
 
    def Afficher(self):
        BoutonDemarrer.scr = pygame.display.get_surface()
        pygame.display.update(self.scr.blit(self.boutton,self.rect))
 
    def clic(self,ev):
        if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                return True


class motATrouver:
    def __init__(self):
        self.masque = pygame.display.get_surface()
        self.imageMasque = pygame.image.load("images/boutonLettre.png")
        self.valeur = self.choixMot()
        self.longueur = len(self.valeur)
        self.espacement = 20
        self.largeur = 75
        self.largeurEcran = largeurScreen
        self.debut = (self.largeurEcran-self.largeur*self.longueur-(self.longueur-1)*self.espacement)/2
        self.police =  pygame.font.Font("images/BradBunR.ttf", 85)
 
    def liste_mots(self):
        "Cette fonction détermine le mot à trouver"
        return choice(list).upper()
 
    def afficherMasque (self,fond):
        
        self.masque.blit(fond,(0,400),(0,400,1150,120))
        for i in range (0,self.longueur):
            position = (self.debut + i*(self.largeur + self.espacement),400)
            self.masque.blit(self.imageMasque,position)
        pygame.display.update()
 
    def afficherMot (self,valeurLettre) :
        for indice , lettre in enumerate(self.valeur) :
            if valeurLettre == lettre :
                text = self.police.render(valeurLettre, 1, (255, 255, 255))
                textpos = text.get_rect()
                textpos.top= 383
                textpos.centerx = (self.debut) + indice *(self.largeur +self.espacement) + 37.5
                self.masque.blit(text,textpos)
        pygame.display.update()
 

pygame.quit()