import pygame
from pygame.locals import *
 
pygame.init()
fenetre = pygame.display.set_mode((400, 400))
 
perso_img = pygame.image.load("anim_right_lite.png").convert_alpha()
frame = 0
WIDTH = 72
frame_rect = pygame.Rect(frame * WIDTH, 0, 72, 114)
 
clock = pygame.time.Clock()
 
continuer = True
while continuer:
     
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
 
    dt = clock.tick(20) # On raltentit la boucle à 30 FPS
 
    frame = (frame + 1) % 24
    frame_rect = pygame.Rect(frame * WIDTH, 0, 72, 114)
 
    fenetre.fill((255, 255, 255))
    fenetre.blit(perso_img, dest=(200, 200), area=frame_rect)
    pygame.display.flip()
 
pygame.quit()