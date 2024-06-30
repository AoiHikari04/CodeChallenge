import pygame 
import random as rd

pygame.init()

SCREEN_WIDTH = 1240
SCREEN_HEIGHT = 800

BLACK = 0,0,0
WHITE = 255,255,255
GREEN = 0, 255, 0
RED = 255,0,0
BLUE = 0,0,255

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
image = pygame.image.load("burung.png").convert_alpha()
image_width, image_height = image.get_size()
image_width += 1

image_rect = image.get_rect()
image_rect.topleft = (200,SCREEN_HEIGHT/2 - image_height/2)
clock = pygame.time.Clock()


draw = pygame.draw

PillarVelocity = 10
Velocity = 2
x = SCREEN_WIDTH

pillar_gap = 200

def drawPillar():

    x = SCREEN_WIDTH
    random_y = rd.randint(0,3)
    gap = pillar_gap

    y_start = [
        200,
        400,
        540,
        120
    ]

    while True:
        PILLAR_WIDTH = 80
        
        x -= PillarVelocity
        y = SCREEN_HEIGHT - y_start[random_y]
        y2 = y - gap - SCREEN_HEIGHT

        if x == 0 - PILLAR_WIDTH:
            x = SCREEN_WIDTH
            random_y = rd.randint(0,3)

        pygame.draw.rect(screen, GREEN, (x, y, PILLAR_WIDTH, SCREEN_HEIGHT))
        pygame.draw.rect(screen, GREEN, (x, y2, PILLAR_WIDTH, SCREEN_HEIGHT))
        
        yield (x, y)

pillar_gen = drawPillar()

run = True
while run:
    screen.fill((0, 0, 0))  # Black
    
    Velocity += 0.25
    
    try:
        x_coord, y_coord = next(pillar_gen)
    except StopIteration:
        pass

    

    # PILLAR_WIDTH = 80
    # random_y = rd.randint(1,4)
    # x -= PillarVelocity
    # pygame.draw.rect(screen, GREEN, (x, SCREEN_HEIGHT/3, 80, SCREEN_HEIGHT))
        

    clock.tick(45) #fps

    screen.blit(image, image_rect)
    image_rect.y-=Velocity

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: 
                print("Move the character forwards") 

            elif event.key == pygame.K_SPACE:
                image_rect.y += 40
                Velocity = 0
                
            elif event.key == pygame.K_s: 
                print("Move the character backwards") 
            elif event.key == pygame.K_a: 
                print("Move the character left") 
            elif event.key == pygame.K_d: 
                print("Move the character right") 

        # if event.type == pygame.KEYUP:
        #     print(event.type)

    if x_coord == image_rect.x + image_width - 10 and (y_coord < image_rect.y or image_rect.y < (y_coord - 200) ):
        print("hitted")
        run = False

    
    # print(x_coord, y_coord)
    # print()
    # print(image_rect.x, image_rect.y)


    

    pygame.display.update()       


pygame.quit()