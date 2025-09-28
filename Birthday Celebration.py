import pygame
import time
pygame.init()
screen = pygame.display.set_mode((800,800))
i = pygame.image.load("i.jpg")
j = pygame.transform.scale(i,(800,800))
k = pygame.image.load("k.jpg")
l = pygame.transform.scale(k,(800,800))
m = pygame.image.load("m.png")
n = pygame.transform.scale(m,(800,800))
while True:
    for p in pygame.event.get():
        if p.type == pygame.QUIT:
            pygame.quit()
    screen.blit(j,(0,0))
    font = pygame.font.SysFont("Comic Sans MS", 50)
    text = font.render("Arlavya",True, "green")
    screen.blit(text, (300,600))
    pygame.display.update()
    time.sleep(5)
    screen.blit(l,(0,0))
    pygame.display.update()
    time.sleep(5)
    screen.blit(n,(0,0))
    pygame.display.update()
    time.sleep(5)