import pygame 
import random

pygame.init()

fenetre = pygame.display.set_mode ((500,500))

image = []

for x in range (10):


    image += [pygame.image.load(f"pendu image {x}.jpg")]

    image[x] = pygame.transform.scale (image [x], (200, 200))
police_hang = pygame.font.SysFont('arial', 20)

def mots_trouve (mots , trouve):

    retour = ''
    for lettres in mots :
        if lettres in trouve: 

            retour += lettres   

        else: lettres 
        retour += "_"
    return retour

def trouve_mots ():

    fichier = open ("mots.txt",'r')

    mots = fichier.read ().split (", ")

    fichier .close ()

    return random.choice (mots)

lettres_trouve = []

erreurs = 0

def gagner ():
    for lettres in mots:
        if not (lettres in lettres_trouve):
            return False
    return True 

def ecran ():
    game = police_hang.render (mots_trouve (mots , lettres_trouve) , 1 , 'black')
    nombre_erreurs = police_hang.render (str (erreurs) , 1 , 'black')
    fenetre.blit (game, (0, 0) )

    fin_de_partie = police_hang.render ('Perdu' , 1 , 'red')
    partie_gagner = police_hang.render ('Gagné' , 1 , 'green')
    if erreurs > 10: 


        fenetre.blit (fin_de_partie, (100, 100) )

    if gagner ():

        fenetre.blit (partie_gagner, (100, 100) )




    fenetre.blit (nombre_erreurs, (50, 50) )
    if erreurs < 10 : 
        fenetre.blit (image[erreurs] , (250 , 250 ) )
mots = trouve_mots ()

def nouvelle_lettre (lettres , mots_cherche):

    global lettres_trouve, erreurs

    if lettres in mots_cherche:
        lettres_trouve += [lettres] 

    else:

        erreurs += 1
fenetre_etteint = True
while  fenetre_etteint:

    pygame.display.update ()
    fenetre.fill ((255 , 255 , 255))
    ecran ()
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
        
            fenetre_etteint = False
        if event.type == pygame. KEYDOWN:
        
            lettres = pygame.key .name(event.key)
            

            nouvelle_lettre (lettres , mots)

            print (lettres)


pygame.quit()