import pygame
import json
import subprocess
pygame.init()
pygame.display.set_caption("flappy slime")
screen = pygame.display.set_mode((1080, 620))
phond = pygame.image.load('assets/phond.png').convert_alpha()
slime_vert = pygame.image.load('assets/slime_vert.png').convert_alpha()
slime_vert = pygame.transform.scale(slime_vert, (150, 150))
block = pygame.image.load('assets/bloc_bleu.jpg').convert_alpha()
block = pygame.transform.scale(block, (50, 250))
block2 = pygame.transform.scale(block, (50, 250))
block3 = pygame.transform.scale(block, (50, 250))
Bubule = pygame.font.Font("Super Bubble.ttf", 24)

with open("data.json", "r") as fichier:
    donnees = json.load(fichier)

run = True
mlr = donnees['mlr']
g = 75
v = 3  
s = 3
x3 = 1681
y3 = 130
x2 = 1381
y2 = 230
x1 = 1081
y1 = 0
x = 0
y = 150
saut = 330
hauteur_max = -620
clock = pygame.time.Clock()
score = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y = y - g
    if score == 1000:
         s = s * 2
         v = v * 2
         g = g + 15

    if score == 2000:
             s = s + 3
             v = v + 3
             g = g + 15
             
    if score == 3000:
                 s = s + 3
                 v = v + 3
                 g = g + 15

    if y < saut:
        y += v
       
    if y < -75 :
         y = -75
    
    x1 = x1 - s
    x2 = x2 - s
    x3 = x3 - s
    if x1 < 0:
         x1 = 1080
    if x2 < 0:
         x2 = 1080
    if x3 < 0:
             x3 = 1080
    
    score = score + 1
    if score > mlr:
          mlr = score + 0
          print("mlr")
    texte_score = Bubule.render("Score" + str(score), True, (255, 0, 0))
    screen.blit(phond, (0, 0))
    screen.blit(block, (x1, y1))
    screen.blit(block2, (x2, y2))
    screen.blit(block3, (x3, y3))
    screen.blit(slime_vert, (x, y))
    screen.blit(texte_score, (0, 0))
    slime_rect = slime_vert.get_rect(topleft=(x, y))
    slime_rect = slime_rect.inflate(-50, -50)
    slime_rect.center = (x + 75, y + 100)
    block_rect = block.get_rect(topleft=(x1, y1))
    block_rect2 = block2.get_rect(topleft=(x2, y2))
    block_rect3 = block3.get_rect(topleft=(x3, y3))
    
    if slime_rect.colliderect(block_rect):
         subprocess.Popen(['python', "game_over.py"])
         run = False
    if slime_rect.colliderect(block_rect2):
         subprocess.Popen(['python', "game_over.py"])
         run = False
    if slime_rect.colliderect(block_rect3):
         subprocess.Popen(['python', "game_over.py"])
         run = False
    pygame.display.flip()
    clock.tick(30)
with open ("data.json", "w") as fichier:
      json.dump({"score": score, "mlr": mlr}, fichier)
pygame.quit()