import pygame
import subprocess
import sys

pygame.init()

screen = pygame.display.set_mode((1024, 620))

game_over = pygame.image.load('assets/game_over.png')
Bubule = pygame.font.Font("Super Bubble.ttf", 24)
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            run = False

    texte_score = Bubule.render("Press any boutton", True, (0, 0, 0))

    screen.blit(game_over, (0, 0))
    screen.blit(texte_score, (0, 0))
    pygame.display.flip()

pygame.quit()

subprocess.Popen(['python', "menu.py"])
sys.exit()