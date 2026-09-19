import pygame
import pygame_menu
import subprocess
import json

pygame.init()

with open("data.json", "r") as fichier:
    donnees = json.load(fichier)

score = donnees["score"]

def play():

    subprocess.call(['python', "main.py"])
    exit()

def stop():
    pygame.quit()
    exit()

screen = pygame.display.set_mode((500, 500))

menu = pygame_menu.Menu('Flappy Slime', 500, 500, theme=pygame_menu.themes.THEME_BLUE) 



label_score = menu.add.label("dernier score : " + str(score))
menu.add.label("")
menu.add.button("Jouer", play)
menu.add.button("Stop", stop)
menu.mainloop(screen)