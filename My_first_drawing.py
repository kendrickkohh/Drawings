import pygame
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
window = (0, 162, 237)
space = (29, 41, 81)
moon = (244, 241, 201)
star = (250, 253, 236)
mars = (201, 148, 227)
saturn = (255, 192, 203)
saturn_ring1 = (255, 218, 185)
saturn_ring2 = (177, 255, 255)
saturn_ring3 = (250, 128, 144)
fire1 = (255, 123, 0)
fire2 = (226, 88, 34)

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Kendrick's first drawing")

pi = 3.141592653
length = 0
width = 0

done = False

clock = pygame.time.Clock()

#----Main program loop----
while done == False:

    #ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
    #ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    screen.fill(space)

    for x in range(0,10): #drawing of stars
        length = random.randrange(0,700)
        breath = random.randrange(0,500)
        pygame.draw.polygon(screen, star, [[20+length,0+breath], [22+length,10+breath], [32+length,12+breath], [22+length,14+breath], [20+length,24+breath], [18+length,14+breath], [8+length,12+breath], [18+length, 10+breath]]) 
        
    pygame.draw.circle(screen, moon, [75, 75], 50) #drawing of moon
    
    pygame.draw.circle(screen, mars, [340, 100], 25) #drawing of mars
    
    pygame.draw.circle(screen, saturn, [550,150], 35)    #drawing of saturn
    pygame.draw.ellipse(screen, saturn_ring1, [500, 125, 100, 50], 3)
    pygame.draw.ellipse(screen, saturn_ring2, [475, 115, 150, 80], 3)
    pygame.draw.ellipse(screen, saturn_ring3, [450, 100, 200, 115], 3)

    pygame.draw.polygon(screen, red, [[350,250], [338, 300], [300,250]]) #drawing of rocket
    pygame.draw.polygon(screen, white, [[338,299], [235, 370], [195, 315], [299,249]])
    pygame.draw.polygon(screen, red, [[235,370], [267,350],[260,400]])
    pygame.draw.polygon(screen, red, [[196,315], [227, 295], [175, 285]])
    pygame.draw.circle(screen, window, [295,290], 22)
    pygame.draw.polygon(screen, fire1, [[190, 340], [160, 370], [120, 395]])
    pygame.draw.polygon(screen, fire2, [[190, 335], [150, 360], [110, 400]])
    pygame.draw.polygon(screen, yellow, [[200, 350], [170, 385], [130, 410]])
    pygame.draw.polygon(screen, fire1, [[210, 360], [180, 395], [140, 420]])
    pygame.draw.polygon(screen, fire2, [[220, 370], [190, 405], [150, 430]])
    
    pygame.display.flip()
    #ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    clock.tick(20)

pygame.quit()
