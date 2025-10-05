import pygame
import time
pygame.init()
screen = pygame.display.set_mode((800,800))
b = pygame.image.load("b.png")
c = pygame.transform.scale(b,(800,800))
d = pygame.image.load("d.jpg")
e = pygame.transform.scale(d,(800,800))
f = pygame.image.load("f.jpg")
g = pygame.transform.scale(f,(800,800))
while True:
    for p in pygame.event.get():
        if p.type == pygame.QUIT:
            pygame.quit()
    screen.blit(c,(0,0))
    font = pygame.font.SysFont("Comic Sans MS", 50)
    text = font.render("Reyaan", True, "green")
    screen.blit(text, (300,600))
    pygame.display.update()
    time.sleep(5)
    screen.blit(e,(0,0))
    pygame.display.update()
    time.sleep(5)
    screen.blit(g,(0,0))
    pygame.display.update()
    time.sleep(5)