import pygame

background_image = "ciel.jpg"

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 455))

run = True
while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
pygame.display.set_caption("Hanged")
background = pygame.image.load(background_image).convert()


x, y = 0, 0
move_x, move_y = 0, 0
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -10
            elif event.key == K_RIGHT:
                move_x = +10
            elif event.key == K_UP:
                move_y = -10
            elif event.key == K_DOWN:
                move_y = +10
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            elif event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP:
                move_y = 0
            elif event.key == K_DOWN:
                move_y = 0
        x += move_x
        y += move_y
        screen.fill((0, 0, 0))
        screen.blit(background, (x, y))
        pygame.display.update()


pygame.init()

import random
choix = ["casserole", "cuillere", "patate", "souris"]
choix = random.choice(choix)

choix = "casserole"
essais = 7
affichage = ""
lettres_trouvees = ""

for l in choix:
  affichage = affichage + "_ "

print(">> Le Jeu <<")

while essais > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")[0:1].lower()

  if proposition in choix:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    essais = essais - 1
    print("-> hanged\n")
    if essais==0:
        print(" ==========Y= ")
    if essais<=1:
        print(" ||/       |  ")
    if essais<=2:
        print(" ||        0  ")
    if essais<=3:
        print(" ||       /|\ ")
    if essais<=4:
        print(" ||       /|  ")
    if essais<=5:                    
        print("/||           ")
    if essais<=6:
        print("==============\n")

  affichage = ""
  for x in choix:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break

     
print("\n    Partie Terminé     ")

pygame.quit()
quit()                                                                                   