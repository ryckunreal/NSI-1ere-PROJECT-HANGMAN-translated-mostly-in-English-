import pygame
import sys
import random
import re
import math 
from pygame.locals import *
from words import words_list

BLACK = (0,0,0)
WHITE = (255,255,255)
MARRON = (153,102,51)


pygame.init()

pygame.display.set_caption("Jeu du Pendu")

screen = pygame.display.set_mode((1600,900))

background = pygame.image.load('TEMPLATES/background_canyon.jpg')
background = pygame.transform.scale(background, (1600, 900))

banner = pygame.image.load('TEMPLATES/banner.png')
banner = pygame.transform.scale(banner, (750, 550))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

play_button = pygame.image.load('TEMPLATES/button_jouer.png')
play_button = pygame.transform.scale(play_button, (275, 100))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.5)
play_button_rect.y = math.ceil(screen.get_height() / 1.68)

rejouer = pygame.image.load('TEMPLATES/rejouer_button.png')
rejouer = pygame.transform.scale(rejouer, (75, 75))
rejouer_rect = rejouer.get_rect()
rejouer_rect.x = 10
rejouer_rect.y = 50


pendu1 = pygame.image.load('TEMPLATES/10.png')
pendu1 = pygame.transform.scale(pendu1, (550, 570))
pendu1_rect = pendu1.get_rect()
pendu1_rect.x = 200
pendu1_rect.y = 300

pendu2 = pygame.image.load('TEMPLATES/9.png')
pendu2 = pygame.transform.scale(pendu2, (550, 570))
pendu2_rect = pendu2.get_rect()
pendu2_rect.x = 200
pendu2_rect.y = 300

pendu3 = pygame.image.load('TEMPLATES/8.png')
pendu3 = pygame.transform.scale(pendu3, (550, 570))
pendu3_rect = pendu3.get_rect()
pendu3_rect.x = 200
pendu3_rect.y = 300

pendu4 = pygame.image.load('TEMPLATES/7.png')
pendu4 = pygame.transform.scale(pendu4, (550, 570))
pendu4_rect = pendu4.get_rect()
pendu4_rect.x = 200
pendu4_rect.y = 300

pendu5 = pygame.image.load('TEMPLATES/6.png')
pendu5 = pygame.transform.scale(pendu5, (550, 570))
pendu5_rect = pendu5.get_rect()
pendu5_rect.x = 200
pendu5_rect.y = 300

pendu6 = pygame.image.load('TEMPLATES/5.png')
pendu6 = pygame.transform.scale(pendu6, (550, 570))
pendu6_rect = pendu6.get_rect()
pendu6_rect.x = 200
pendu6_rect.y = 300

pendu7 = pygame.image.load('TEMPLATES/4.png')
pendu7 = pygame.transform.scale(pendu7, (550, 570))
pendu7_rect = pendu7.get_rect()
pendu7_rect.x = 200
pendu7_rect.y = 300

pendu8 = pygame.image.load('TEMPLATES/3.png')
pendu8 = pygame.transform.scale(pendu8, (550, 570))
pendu8_rect = pendu8.get_rect()
pendu8_rect.x = 200
pendu8_rect.y = 300

pendu9 = pygame.image.load('TEMPLATES/2.png')
pendu9 = pygame.transform.scale(pendu9, (550, 570))
pendu9_rect = pendu9.get_rect()
pendu9_rect.x = 200
pendu9_rect.y = 300

pendu10 = pygame.image.load('TEMPLATES/1.png')
pendu10 = pygame.transform.scale(pendu10, (550, 570))
pendu10_rect = pendu10.get_rect()
pendu10_rect.x = 200
pendu10_rect.y = 300

pendu11 = pygame.image.load('TEMPLATES/0.png')
pendu11 = pygame.transform.scale(pendu11, (550, 570))
pendu11_rect = pendu11.get_rect()
pendu11_rect.x = 200
pendu11_rect.y = 300


Font = pygame.font.Font("freesansbold.ttf",70)
Font2 = pygame.font.Font("freesansbold.ttf",40)

screen.blit(background, (0,0))



def motHasard(jouer):
    motHasard = 0
    if jouer == 1:
        motHasard = random.randint(0,len(words_list)-1)
    return motHasard


def List(nombre,jouer):
    if jouer == 1:
        Mot = words_list[nombre]   
    return Mot 



def Pendu(erreur):
    if (erreur == 0):
        print("Pas d'erreur")

    elif (erreur == 1):
        screen.blit(pendu1, pendu1_rect)

    elif (erreur == 2):
        screen.blit(pendu2, pendu2_rect)

    elif (erreur == 3):
        screen.blit(pendu3, pendu3_rect)

    elif (erreur == 4):
        screen.blit(pendu4, pendu4_rect)

    elif (erreur == 5):
        screen.blit(pendu5, pendu5_rect)

    elif (erreur == 6):
        screen.blit(pendu6, pendu6_rect)

    elif (erreur == 7):
        screen.blit(pendu7, pendu7_rect)

    elif (erreur == 8):
        screen.blit(pendu8, pendu8_rect)

    elif (erreur == 9):
        screen.blit(pendu9, pendu9_rect)

    elif (erreur == 10):
        screen.blit(pendu10, pendu10_rect)

    elif (erreur == 11):
        screen.blit(pendu11, pendu11_rect)

        

def sheriff():
    sheriff = pygame.image.load('TEMPLATES/sheriff.png')
    sheriff = pygame.transform.scale(sheriff, (500, 500))
    sheriff_rect = sheriff.get_rect()
    sheriff_rect.x = 1100
    sheriff_rect.y = 350
    screen.blit(sheriff, sheriff_rect)

def bulle():
    bulle = pygame.image.load('TEMPLATES/bulle.png')
    bulle = pygame.transform.scale(bulle, (500, 275))
    bulle_rect = bulle.get_rect()
    bulle_rect.x = 950
    bulle_rect.y = 150
    screen.blit(bulle, bulle_rect)

def bagcoin():
    bagcoin = pygame.image.load('TEMPLATES/bagcoin.png')
    bagcoin = pygame.transform.scale(bagcoin, (500, 450))
    bagcoin_rect = bagcoin.get_rect()
    bagcoin_rect.x = 100
    bagcoin_rect.y = 500
    screen.blit(bagcoin, bagcoin_rect)

def cercueil():
    cercueil = pygame.image.load('TEMPLATES/cercueil.png')
    cercueil = pygame.transform.scale(cercueil, (600, 250))
    cercueil_rect = cercueil.get_rect()
    cercueil_rect.x = 100
    cercueil_rect.y = 650
    screen.blit(cercueil, cercueil_rect)


def rejouer():
    rejouer = pygame.image.load('TEMPLATES/rejouer_button.png')
    rejouer = pygame.transform.scale(rejouer, (75, 75))
    rejouer_rect = rejouer.get_rect()
    rejouer_rect.x = 10
    rejouer_rect.y = 50
    screen.blit(rejouer, rejouer_rect)


def Menu():
    screen.blit(play_button, play_button_rect)
    screen.blit(banner, banner_rect)

def main():
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    MARRON = (153,102,51)

    PlayGame = 0
	
    Menu()
		
    
    Running = True
    while Running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    PlayGame = 1
                    Running = False
                    break


        if PlayGame == 1:
            screen.blit(background, (0,0))
            
        pygame.display.update()
        

    Numéro = motHasard(PlayGame)                      
    MotCache = List(Numéro, PlayGame)

    ListeVide = []
    Letter_Used = []

    for i in range(len(MotCache)):
        ListeVide.append('-') 

    
    pygame.draw.rect(screen,MARRON,(300,150,400,110)) 
    Trait = Font.render("".join(ListeVide),True,WHITE) 
    TraitRect = Trait.get_rect()
    TraitRect.center = (500,215)
    screen.blit(Trait,TraitRect)

    Erreur = 0 
    FinDuJeu = 0 



    while True:

        if len(MotCache) <= 4 :
          total_erreur = 7
        elif len(MotCache) > 4 and len(MotCache) <= 7 :
          total_erreur = 10
        else :
          total_erreur = math.ceil(len(MotCache) * 1.2)
        etat_pendu = round(Erreur / total_erreur * 10)
        if etat_pendu == 10 and Erreur != 0:
          etat_pendu = etat_pendu - 1
        
        Pendu(etat_pendu)
        sheriff()
        bulle()
        
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == KEYDOWN:
 

                
                if re.search("[a-z]",chr(event.key)):
                    pygame.draw.rect(screen,MARRON,(300,150,400,110)) 
                    
                    screen.blit(pygame.font.Font("freesansbold.ttf",30).render("Letters already used:",True,BLACK),(30,40))

                    
                    if chr(event.key) not in Letter_Used :
                      Letter_Used.append(chr(event.key))
                    Word1 = Font2.render(" ".join(Letter_Used),True,BLACK)
                    Word1Rect = Word1.get_rect()
                    Word1Rect.x = 440
                    Word1Rect.y = 30
                    screen.blit(Word1,Word1Rect)
                    
    
                    if ((chr(event.key).upper() in MotCache) or (chr(event.key).lower() in MotCache)):
                        for i in range(len(MotCache)):
                            if ((MotCache[i] == (chr(event.key)).upper()) or (MotCache[i] == (chr(event.key)).lower())):
                                ListeVide[i] = MotCache[i]


                    elif chr(event.key).upper not in Letter_Used or chr(event.key).lower not in Letter_Used :
                        Erreur = Erreur + 1
                      
                      
                    Trait = Font.render("".join(ListeVide),True,WHITE)
                    TraitRect = Trait.get_rect()
                    TraitRect.center = (500,215)
                    screen.blit(Trait,TraitRect)

                    
        if (Erreur/total_erreur == 1):
            screen.blit(background, (0,0))

            sheriff()
            cercueil()
            rejouer()
            

            

            screen.blit(pygame.font.Font("freesansbold.ttf",30).render("Go back to menu",True,BLACK),(90,70))

            bulle_perdu = pygame.image.load('TEMPLATES/bulle_lost.png')
            bulle_perdu = pygame.transform.scale(bulle_perdu, (500, 275))
            bulle_perdu_rect = bulle_perdu.get_rect()
            bulle_perdu_rect.x = 950
            bulle_perdu_rect.y = 150
            screen.blit(bulle_perdu, bulle_perdu_rect)

            Word = Font2.render("The word was:",True,BLACK)
            WordRect = Word.get_rect()
            WordRect.center = (650,250)
            screen.blit(Word,WordRect)

            Word2 = Font.render(MotCache,True,BLACK)
            Word2Rect = Word2.get_rect()
            Word2Rect.center = (650,315)
            screen.blit(Word2,Word2Rect)

            FinDuJeu = 1


        elif (MotCache == "".join(ListeVide)): 
            screen.blit(background, (0,0))
            
            sheriff()
            bagcoin()
            rejouer()
            
            screen.blit(pygame.font.Font("freesansbold.ttf",30).render("Go back to menu",True,BLACK),(90,70))
         
            bulle_gagne = pygame.image.load('TEMPLATES/bulle_win.png')
            bulle_gagne = pygame.transform.scale(bulle_gagne, (500, 275))
            bulle_gagne_rect = bulle_gagne.get_rect()
            bulle_gagne_rect.x = 950
            bulle_gagne_rect.y = 150
            screen.blit(bulle_gagne, bulle_gagne_rect)
            
            
            Word = Font2.render("The word is:",True,BLACK)
            WordRect = Word.get_rect()
            WordRect.center = (650,250)
            screen.blit(Word,WordRect)

            Word2 = Font.render(MotCache,True,BLACK)
            Word2Rect = Word2.get_rect()
            Word2Rect.center = (650,315)
            screen.blit(Word2,Word2Rect)
            
            
            FinDuJeu = 1



        pygame.display.update()


        if (FinDuJeu == 1):

            for event in pygame.event.get():
              if event.type == QUIT:
                pygame.quit()
                sys.exit()

              elif event.type == MOUSEBUTTONDOWN:
                if rejouer_rect.collidepoint(event.pos):
                    
                    screen.blit(background, (0,0))
                    main()

                  
main()

